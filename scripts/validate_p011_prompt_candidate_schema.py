#!/usr/bin/env python3
import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "p011-prompt-candidate.schema.json"
DRAFT = ROOT / "examples" / "P011-PEE-002.prompt-candidate.draft.example.json"
APPROVED = ROOT / "examples" / "P011-XPIO-001.prompt-candidate.approved-fixture.json"

schema = json.loads(SCHEMA.read_text())
validator = Draft202012Validator(schema)

def errors(record):
    return list(validator.iter_errors(record))

draft = json.loads(DRAFT.read_text())
approved = json.loads(APPROVED.read_text())

assert not errors(draft), errors(draft)
assert not errors(approved), errors(approved)

failed_gate = copy.deepcopy(approved)
failed_gate["evaluation"]["critical_gates_passed"] = False
assert errors(failed_gate), "approved record with failed critical gates must be rejected"

missing_approver = copy.deepcopy(approved)
missing_approver["human_approval"]["approver"] = None
assert errors(missing_approver), "approved record without approver must be rejected"

missing_audit = copy.deepcopy(approved)
missing_audit["human_approval"]["audit_reference"] = ""
assert errors(missing_audit), "approved record without audit reference must be rejected"

draft_without_eval = copy.deepcopy(draft)
draft_without_eval.pop("evaluation", None)
assert not errors(draft_without_eval), "draft must not require fabricated evaluation"

evaluated_without_eval = copy.deepcopy(draft)
evaluated_without_eval["state"] = "evaluated"
assert errors(evaluated_without_eval), "evaluated state must require evaluation"

print("Prompt #11 candidate schema tests passed")
