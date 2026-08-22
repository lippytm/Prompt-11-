"""Prompt #11 Evolution Engine prototype.

This module proposes reviewable capability mutations for an authorized AI clone.
It deliberately does not modify its own source code, deploy agents, access networks,
move money, publish content, or pass HumanApprovalGate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ALLOWED_PRIVACY_CLASSES = {"public", "internal", "confidential", "restricted"}
ALLOWED_RISK_GATES = {"green", "yellow", "orange", "red"}
DEPLOYABLE_RISK_GATES = {"green", "yellow"}
AI_APPROVER_MARKERS = {"ai", "agent", "bot", "model", "clone", "swarm"}


class ValidationError(ValueError):
    """Raised when a record violates the prototype contract."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def canonical_hash(payload: Any) -> str:
    """Return a deterministic SHA-256 hash for a JSON-compatible payload."""
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _validate_score(value: float, field_name: str) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValidationError(f"{field_name} must be numeric")
    if not 0 <= float(value) <= 100:
        raise ValidationError(f"{field_name} must be between 0 and 100")


@dataclass(frozen=True)
class ClonePassport:
    clone_id: str
    display_name: str
    legal_owner: str
    identity_class: str
    model_line: str
    version: str
    status: str
    permitted_actions: tuple[str, ...]
    prohibited_actions: tuple[str, ...]
    permitted_privacy_classes: tuple[str, ...]
    human_approval_required: bool = True
    parent_clone_id: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ClonePassport":
        required = {
            "clone_id",
            "display_name",
            "legal_owner",
            "identity_class",
            "model_line",
            "version",
            "status",
            "permitted_actions",
            "prohibited_actions",
            "permitted_privacy_classes",
        }
        missing = sorted(required - data.keys())
        if missing:
            raise ValidationError(f"clone passport missing: {', '.join(missing)}")

        privacy = tuple(data["permitted_privacy_classes"])
        invalid_privacy = sorted(set(privacy) - ALLOWED_PRIVACY_CLASSES)
        if invalid_privacy:
            raise ValidationError(f"invalid privacy classes: {', '.join(invalid_privacy)}")
        if "restricted" in privacy and not data.get("human_approval_required", True):
            raise ValidationError("restricted access requires human approval")

        prohibited = tuple(data["prohibited_actions"])
        mandatory_blocks = {
            "impersonate_legal_person",
            "fabricate_personal_memory",
            "autonomous_financial_action",
            "autonomous_contracting",
            "bypass_human_approval",
        }
        if not mandatory_blocks.issubset(set(prohibited)):
            missing_blocks = sorted(mandatory_blocks - set(prohibited))
            raise ValidationError(
                "clone passport must prohibit: " + ", ".join(missing_blocks)
            )

        return cls(
            clone_id=str(data["clone_id"]),
            display_name=str(data["display_name"]),
            legal_owner=str(data["legal_owner"]),
            identity_class=str(data["identity_class"]),
            model_line=str(data["model_line"]),
            version=str(data["version"]),
            status=str(data["status"]),
            permitted_actions=tuple(data["permitted_actions"]),
            prohibited_actions=prohibited,
            permitted_privacy_classes=privacy,
            human_approval_required=bool(data.get("human_approval_required", True)),
            parent_clone_id=data.get("parent_clone_id"),
        )


@dataclass(frozen=True)
class EvaluationRecord:
    evaluation_id: str
    clone_id: str
    capability: str
    score: float
    target_score: float
    evidence_ids: tuple[str, ...]
    evaluator: str
    evaluated_at: str
    notes: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "EvaluationRecord":
        for field_name in (
            "evaluation_id",
            "clone_id",
            "capability",
            "score",
            "target_score",
            "evidence_ids",
            "evaluator",
        ):
            if field_name not in data:
                raise ValidationError(f"evaluation missing {field_name}")
        _validate_score(data["score"], "score")
        _validate_score(data["target_score"], "target_score")
        evidence = tuple(data["evidence_ids"])
        if not evidence:
            raise ValidationError("evaluation requires at least one evidence ID")
        return cls(
            evaluation_id=str(data["evaluation_id"]),
            clone_id=str(data["clone_id"]),
            capability=str(data["capability"]),
            score=float(data["score"]),
            target_score=float(data["target_score"]),
            evidence_ids=evidence,
            evaluator=str(data["evaluator"]),
            evaluated_at=str(data.get("evaluated_at") or utc_now()),
            notes=str(data.get("notes", "")),
        )


@dataclass
class MutationProposal:
    mutation_id: str
    clone_id: str
    capability: str
    current_score: float
    target_score: float
    gap: float
    proposed_change: str
    evidence_ids: list[str]
    risk_gate: str
    required_gates: list[str]
    status: str = "proposed"
    human_approval_status: str = "pending"
    human_approver: str | None = None
    approval_conditions: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=utc_now)
    content_hash: str = ""

    def seal(self) -> None:
        payload = asdict(self)
        payload["content_hash"] = ""
        self.content_hash = canonical_hash(payload)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class EvolutionEngine:
    """Evidence-driven mutation planner with non-automatable human approval."""

    def __init__(self, passport: ClonePassport, evaluations: Iterable[EvaluationRecord]):
        self.passport = passport
        self.evaluations = list(evaluations)
        self._validate_evaluations()

    def _validate_evaluations(self) -> None:
        ids: set[str] = set()
        for record in self.evaluations:
            if record.clone_id != self.passport.clone_id:
                raise ValidationError(
                    f"evaluation {record.evaluation_id} belongs to another clone"
                )
            if record.evaluation_id in ids:
                raise ValidationError(f"duplicate evaluation ID: {record.evaluation_id}")
            ids.add(record.evaluation_id)

    def latest_by_capability(self) -> dict[str, EvaluationRecord]:
        latest: dict[str, EvaluationRecord] = {}
        for record in sorted(self.evaluations, key=lambda item: item.evaluated_at):
            latest[record.capability] = record
        return latest

    def capability_gaps(self, minimum_gap: float = 1.0) -> list[dict[str, Any]]:
        if minimum_gap < 0:
            raise ValidationError("minimum_gap cannot be negative")
        gaps: list[dict[str, Any]] = []
        for record in self.latest_by_capability().values():
            gap = max(0.0, record.target_score - record.score)
            if gap >= minimum_gap:
                gaps.append(
                    {
                        "capability": record.capability,
                        "current_score": record.score,
                        "target_score": record.target_score,
                        "gap": round(gap, 2),
                        "evidence_ids": list(record.evidence_ids),
                        "evaluation_id": record.evaluation_id,
                    }
                )
        return sorted(gaps, key=lambda item: (-item["gap"], item["capability"]))

    @staticmethod
    def assign_risk_gate(capability: str, proposed_change: str) -> str:
        text = f"{capability} {proposed_change}".lower()
        red_terms = {
            "private key",
            "seed phrase",
            "weapon",
            "impersonate",
            "bypass approval",
            "autonomous payment",
            "autonomous contract",
        }
        orange_terms = {
            "restricted data",
            "medical diagnosis",
            "legal conclusion",
            "financial advice",
            "production deployment",
            "identity cloning",
        }
        yellow_terms = {
            "external connector",
            "customer-facing",
            "public release",
            "synthetic voice",
            "paid offer",
            "model update",
        }
        if any(term in text for term in red_terms):
            return "red"
        if any(term in text for term in orange_terms):
            return "orange"
        if any(term in text for term in yellow_terms):
            return "yellow"
        return "green"

    def propose_mutation(
        self,
        capability: str,
        proposed_change: str,
        required_gates: list[str] | None = None,
    ) -> MutationProposal:
        record = self.latest_by_capability().get(capability)
        if record is None:
            raise ValidationError(f"no evaluation for capability: {capability}")
        gap = max(0.0, record.target_score - record.score)
        if gap <= 0:
            raise ValidationError(f"capability already meets target: {capability}")
        required = required_gates or [
            "IdentityGate",
            "ConsentGate",
            "EvaluationGate",
            "MutationSafetyGate",
            "PrivacyGate",
            "SecurityGate",
            "HumanApprovalGate",
        ]
        mutation_id = "MUT-" + canonical_hash(
            {
                "clone_id": self.passport.clone_id,
                "capability": capability,
                "evaluation_id": record.evaluation_id,
                "proposed_change": proposed_change,
            }
        )[:12].upper()
        proposal = MutationProposal(
            mutation_id=mutation_id,
            clone_id=self.passport.clone_id,
            capability=capability,
            current_score=record.score,
            target_score=record.target_score,
            gap=round(gap, 2),
            proposed_change=proposed_change,
            evidence_ids=list(record.evidence_ids),
            risk_gate=self.assign_risk_gate(capability, proposed_change),
            required_gates=required,
        )
        proposal.seal()
        return proposal

    @staticmethod
    def approve(
        proposal: MutationProposal,
        approver: str,
        approver_type: str,
        passed_gates: Iterable[str],
        conditions: Iterable[str] = (),
    ) -> MutationProposal:
        normalized_type = approver_type.strip().lower()
        if normalized_type != "human" or normalized_type in AI_APPROVER_MARKERS:
            raise ValidationError("HumanApprovalGate requires an identified human approver")
        if proposal.risk_gate not in DEPLOYABLE_RISK_GATES:
            raise ValidationError(
                f"{proposal.risk_gate} RiskGate cannot be approved for deployment"
            )
        passed = set(passed_gates)
        missing = sorted(set(proposal.required_gates) - passed)
        if missing:
            raise ValidationError("missing required gates: " + ", ".join(missing))
        proposal.status = "approved_for_bounded_pilot"
        proposal.human_approval_status = "approved"
        proposal.human_approver = approver
        proposal.approval_conditions = list(conditions)
        proposal.seal()
        return proposal

    @staticmethod
    def release_eligible(proposal: MutationProposal, passed_gates: Iterable[str]) -> bool:
        return (
            proposal.status == "approved_for_bounded_pilot"
            and proposal.human_approval_status == "approved"
            and proposal.risk_gate in DEPLOYABLE_RISK_GATES
            and set(proposal.required_gates).issubset(set(passed_gates))
        )


def load_json(path: str | Path) -> Any:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: str | Path, payload: Any) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")


def build_engine(passport_path: str, evaluations_path: str) -> EvolutionEngine:
    passport = ClonePassport.from_dict(load_json(passport_path))
    evaluations_raw = load_json(evaluations_path)
    if not isinstance(evaluations_raw, list):
        raise ValidationError("evaluations file must contain a JSON array")
    evaluations = [EvaluationRecord.from_dict(item) for item in evaluations_raw]
    return EvolutionEngine(passport, evaluations)


def main() -> int:
    parser = argparse.ArgumentParser(description="Prompt #11 Evolution Engine prototype")
    parser.add_argument("--passport", required=True, help="Clone Passport JSON file")
    parser.add_argument("--evaluations", required=True, help="Evaluation records JSON file")
    parser.add_argument("--output", required=True, help="Output mutation proposals JSON file")
    parser.add_argument("--minimum-gap", type=float, default=5.0)
    args = parser.parse_args()

    try:
        engine = build_engine(args.passport, args.evaluations)
        proposals: list[dict[str, Any]] = []
        for gap in engine.capability_gaps(args.minimum_gap):
            proposal = engine.propose_mutation(
                gap["capability"],
                (
                    "Create a bounded training, evaluation, and documentation experiment "
                    f"for {gap['capability']}; do not auto-deploy or modify the clone runtime."
                ),
            )
            proposals.append(proposal.to_dict())
        write_json(
            args.output,
            {
                "clone_id": engine.passport.clone_id,
                "generated_at": utc_now(),
                "release_authority": "human_only",
                "proposals": proposals,
            },
        )
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
