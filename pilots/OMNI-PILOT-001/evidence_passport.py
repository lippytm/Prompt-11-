"""Beginner-friendly Evidence Passport validator for Prompt #11.

This educational program teaches dictionaries, functions, conditionals, loops,
JSON, tests, and SHA-256 integrity hashes. It does not certify truth, legal
compliance, medical safety, investment value, or commercial release.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

TRUTH_LABELS = {"VF", "OA", "CT", "AL", "WH", "FD", "CX"}
PRIVACY_CLASSES = {"Public", "Internal", "Confidential", "Restricted"}
RISK_GATES = {"Green", "Yellow", "Orange", "Red"}
PRODUCT_STAGES = {"Q0", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"}

REQUIRED_FIELDS = {
    "passport_id",
    "title",
    "truth_label",
    "privacy_class",
    "risk_gate",
    "product_stage",
    "human_approval",
    "critical_gates_passed",
    "publish_requested",
}


def canonical_json(passport: dict[str, Any]) -> str:
    """Return deterministic JSON so the same content produces the same hash."""
    return json.dumps(passport, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def content_hash(passport: dict[str, Any]) -> str:
    """Return a SHA-256 integrity hash for the passport's current content."""
    return hashlib.sha256(canonical_json(passport).encode("utf-8")).hexdigest()


def validate_passport(passport: dict[str, Any]) -> list[str]:
    """Return plain-language validation issues. An empty list means structurally valid."""
    issues: list[str] = []

    missing = sorted(field for field in REQUIRED_FIELDS if field not in passport)
    for field in missing:
        issues.append(f"Missing required field: {field}")

    if missing:
        return issues

    if not str(passport["passport_id"]).strip():
        issues.append("passport_id must not be blank")
    if not str(passport["title"]).strip():
        issues.append("title must not be blank")

    truth_label = passport["truth_label"]
    if truth_label not in TRUTH_LABELS:
        issues.append(f"truth_label must be one of {sorted(TRUTH_LABELS)}")

    privacy_class = passport["privacy_class"]
    if privacy_class not in PRIVACY_CLASSES:
        issues.append(f"privacy_class must be one of {sorted(PRIVACY_CLASSES)}")

    risk_gate = passport["risk_gate"]
    if risk_gate not in RISK_GATES:
        issues.append(f"risk_gate must be one of {sorted(RISK_GATES)}")

    product_stage = passport["product_stage"]
    if product_stage not in PRODUCT_STAGES:
        issues.append(f"product_stage must be one of {sorted(PRODUCT_STAGES)}")

    human_approval = passport["human_approval"]
    if human_approval not in {"Pending", "Approved", "Rejected", "Revoked"}:
        issues.append("human_approval must be Pending, Approved, Rejected, or Revoked")

    if not isinstance(passport["critical_gates_passed"], bool):
        issues.append("critical_gates_passed must be true or false")
    if not isinstance(passport["publish_requested"], bool):
        issues.append("publish_requested must be true or false")

    if truth_label in {"VF", "OA", "CT", "AL", "CX"}:
        source_url = str(passport.get("source_url", "")).strip()
        if not source_url.startswith(("https://", "http://")):
            issues.append("This truth label requires a source_url beginning with http:// or https://")

    if truth_label == "FD" and passport.get("fiction_disclosure") is not True:
        issues.append("FD content requires fiction_disclosure=true")

    if privacy_class == "Restricted" and passport["publish_requested"] is True:
        issues.append("Restricted content cannot be sent to a public publishing route")

    if risk_gate == "Red":
        issues.append("Red RiskGate requires stop-work and blocks release")

    return issues


def release_decision(passport: dict[str, Any]) -> dict[str, Any]:
    """Explain the current release state without performing any release action."""
    issues = validate_passport(passport)
    if issues:
        return {"decision": "BLOCKED", "reasons": issues}

    if passport["publish_requested"] is False:
        return {"decision": "NOT_REQUESTED", "reasons": ["No publication was requested"]}

    if passport["product_stage"] not in {"Q4", "Q5", "Q6", "Q7"}:
        return {
            "decision": "REVIEW_ONLY",
            "reasons": ["Q4 or higher is required for approved inventory"],
        }

    if passport["risk_gate"] in {"Orange", "Red"}:
        return {
            "decision": "BLOCKED",
            "reasons": ["Orange or Red RiskGate blocks ordinary release"],
        }

    if passport["critical_gates_passed"] is not True:
        return {
            "decision": "BLOCKED",
            "reasons": ["All applicable critical gates must pass"],
        }

    if passport["human_approval"] != "Approved":
        return {
            "decision": "REVIEW_ONLY",
            "reasons": ["HumanApprovalGate is not approved"],
        }

    return {
        "decision": "ELIGIBLE_FOR_AUTHORIZED_HUMAN_RELEASE",
        "reasons": ["The record is structurally eligible; an authorized human still controls release"],
    }


def example_passport() -> dict[str, Any]:
    """Return a safe Q3 sample that is intentionally not releasable."""
    return {
        "passport_id": "PASS-LK9-LESSON-001",
        "title": "Lippy Killjoy and the Evidence Passport",
        "truth_label": "FD",
        "fiction_disclosure": True,
        "privacy_class": "Public",
        "risk_gate": "Yellow",
        "product_stage": "Q3",
        "human_approval": "Pending",
        "critical_gates_passed": False,
        "publish_requested": True,
        "learning_goal": "Practice Python validation and responsible release logic",
    }


def load_passport(path: Path | None) -> dict[str, Any]:
    if path is None:
        return example_passport()
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Prompt #11 Evidence Passport")
    parser.add_argument("json_file", nargs="?", type=Path, help="Optional passport JSON file")
    args = parser.parse_args()

    passport = load_passport(args.json_file)
    report = {
        "passport_id": passport.get("passport_id", "UNKNOWN"),
        "content_sha256": content_hash(passport),
        "validation_issues": validate_passport(passport),
        "release": release_decision(passport),
    }
    print(json.dumps(report, indent=2))
    return 0 if report["release"]["decision"] != "BLOCKED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
