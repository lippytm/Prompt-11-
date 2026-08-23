from __future__ import annotations

import hashlib
import json
from typing import Any

QUALITY_WEIGHTS = {
    "evidence": 0.15,
    "tests": 0.15,
    "data_quality": 0.15,
    "consent": 0.10,
    "privacy_security": 0.15,
    "service_learning": 0.10,
    "accessibility_fairness": 0.10,
    "correction_provider": 0.10,
}

CRITICAL_GATES = [
    "PurposeGate",
    "ConsentGate",
    "IdentityGate",
    "PrivacyGate",
    "SecurityGate",
    "ProviderCertificationGate",
    "AccessibilityGate",
    "FairnessGate",
    "CorrectionGate",
    "HumanApprovalGate",
]


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def stable_hash(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def stable_id(prefix: str, value: Any) -> str:
    return f"{prefix}-{stable_hash(value)[:16].upper()}"


def quality_score(metrics: dict[str, float]) -> float:
    missing = sorted(set(QUALITY_WEIGHTS) - set(metrics))
    if missing:
        raise ValueError(f"missing metrics: {missing}")
    total = 0.0
    for key, weight in QUALITY_WEIGHTS.items():
        value = float(metrics[key])
        if value < 0 or value > 100:
            raise ValueError(f"{key} outside 0..100")
        total += value * weight
    return round(total, 2)


def compile_review(signal: dict[str, Any]) -> dict[str, Any]:
    review = {
        "signal_id": signal["signal_id"],
        "correlation_id": signal["correlation_id"],
        "assigned_swarm": signal.get("assigned_swarm", "Prompt #11 Quality Swarm"),
        "privacy_class": signal.get("privacy_class", "Internal"),
        "required_gates": sorted(set(signal.get("required_gates", []) + ["HumanApprovalGate"])),
        "state": "Review",
        "human_approval": "Pending",
        "review_only": True,
    }
    review["mission_id"] = stable_id("MIS", review)
    return review


def propose_evolution(signal: dict[str, Any], mission: dict[str, Any]) -> dict[str, Any]:
    proposal = {
        "signal_id": signal["signal_id"],
        "mission_id": mission["mission_id"],
        "capability_gap": signal.get("capability_gap", signal.get("event_type", "quality")),
        "proposed_mutation": signal.get("proposed_mutation", "Create a bounded, testable improvement"),
        "risk_gate": signal.get("risk_gate", "Yellow"),
        "sandbox_only": True,
        "tests_required": signal.get("tests_required", ["functional", "privacy", "security", "regression", "rollback"]),
        "human_approval": "Pending",
        "auto_deploy": False,
        "state": "Proposed",
    }
    proposal["proposal_id"] = stable_id("EVO", proposal)
    return proposal


def gate_blockers(gates: dict[str, str]) -> list[str]:
    return [gate for gate in CRITICAL_GATES if gates.get(gate) not in {"Pass", "Approved", "Not Applicable"}]


def pilot_eligible(proposal: dict[str, Any], gates: dict[str, str], human_approval: str) -> bool:
    return (
        proposal.get("risk_gate") != "Red"
        and proposal.get("sandbox_only") is True
        and proposal.get("auto_deploy") is False
        and human_approval == "Approved"
        and not gate_blockers(gates)
    )


def release_eligible(q_stage: str, risk_gate: str, gates: dict[str, str], human_approval: str) -> bool:
    return q_stage == "Q4" and risk_gate not in {"Red", "Orange"} and human_approval == "Approved" and not gate_blockers(gates)
