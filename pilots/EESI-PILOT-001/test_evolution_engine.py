import copy
import unittest

from evolution_engine import (
    ClonePassport,
    EvaluationRecord,
    EvolutionEngine,
    ValidationError,
    canonical_hash,
)


PASSPORT = {
    "clone_id": "CLONE-CEL-001",
    "display_name": "Charles Earl Lipshay Evolutionary Clone Interface",
    "legal_owner": "Charles Earl Lipshay",
    "identity_class": "authorized_ai_interface",
    "model_line": "chatgpt",
    "version": "0.1.0",
    "status": "sandbox",
    "permitted_actions": [
        "organize_public_project_information",
        "draft_educational_material",
        "propose_reviewable_mutations",
    ],
    "prohibited_actions": [
        "impersonate_legal_person",
        "fabricate_personal_memory",
        "autonomous_financial_action",
        "autonomous_contracting",
        "bypass_human_approval",
    ],
    "permitted_privacy_classes": ["public", "internal"],
    "human_approval_required": True,
}

EVALUATIONS = [
    {
        "evaluation_id": "EVAL-001",
        "clone_id": "CLONE-CEL-001",
        "capability": "python_testing",
        "score": 62,
        "target_score": 85,
        "evidence_ids": ["TST-001", "TST-002"],
        "evaluator": "human-reviewer",
        "evaluated_at": "2026-08-22T20:00:00+00:00",
    },
    {
        "evaluation_id": "EVAL-002",
        "clone_id": "CLONE-CEL-001",
        "capability": "source_provenance",
        "score": 90,
        "target_score": 90,
        "evidence_ids": ["SRC-001"],
        "evaluator": "human-reviewer",
        "evaluated_at": "2026-08-22T20:01:00+00:00",
    },
]


def build_engine():
    passport = ClonePassport.from_dict(copy.deepcopy(PASSPORT))
    evaluations = [EvaluationRecord.from_dict(copy.deepcopy(item)) for item in EVALUATIONS]
    return EvolutionEngine(passport, evaluations)


class EvolutionEngineTests(unittest.TestCase):
    def test_canonical_hash_is_deterministic(self):
        self.assertEqual(canonical_hash({"b": 2, "a": 1}), canonical_hash({"a": 1, "b": 2}))

    def test_passport_requires_mandatory_prohibitions(self):
        passport = copy.deepcopy(PASSPORT)
        passport["prohibited_actions"].remove("autonomous_financial_action")
        with self.assertRaises(ValidationError):
            ClonePassport.from_dict(passport)

    def test_restricted_data_requires_human_approval(self):
        passport = copy.deepcopy(PASSPORT)
        passport["permitted_privacy_classes"].append("restricted")
        passport["human_approval_required"] = False
        with self.assertRaises(ValidationError):
            ClonePassport.from_dict(passport)

    def test_scores_must_be_bounded(self):
        evaluation = copy.deepcopy(EVALUATIONS[0])
        evaluation["score"] = 101
        with self.assertRaises(ValidationError):
            EvaluationRecord.from_dict(evaluation)

    def test_capability_gaps_only_include_unmet_targets(self):
        gaps = build_engine().capability_gaps()
        self.assertEqual(len(gaps), 1)
        self.assertEqual(gaps[0]["capability"], "python_testing")
        self.assertEqual(gaps[0]["gap"], 23.0)

    def test_mutation_is_deterministic_for_same_inputs(self):
        engine = build_engine()
        first = engine.propose_mutation("python_testing", "Add a bounded test-training exercise")
        second = engine.propose_mutation("python_testing", "Add a bounded test-training exercise")
        self.assertEqual(first.mutation_id, second.mutation_id)

    def test_red_risk_detects_autonomous_payment(self):
        engine = build_engine()
        proposal = engine.propose_mutation(
            "python_testing", "Add autonomous payment after test completion"
        )
        self.assertEqual(proposal.risk_gate, "red")

    def test_ai_cannot_approve(self):
        proposal = build_engine().propose_mutation(
            "python_testing", "Add a bounded test-training exercise"
        )
        with self.assertRaises(ValidationError):
            EvolutionEngine.approve(
                proposal,
                approver="Hermes",
                approver_type="ai",
                passed_gates=proposal.required_gates,
            )

    def test_missing_gate_blocks_human_approval(self):
        proposal = build_engine().propose_mutation(
            "python_testing", "Add a bounded test-training exercise"
        )
        with self.assertRaises(ValidationError):
            EvolutionEngine.approve(
                proposal,
                approver="Charles Earl Lipshay",
                approver_type="human",
                passed_gates=["IdentityGate"],
            )

    def test_red_risk_blocks_human_approval(self):
        proposal = build_engine().propose_mutation(
            "python_testing", "Add autonomous payment after test completion"
        )
        with self.assertRaises(ValidationError):
            EvolutionEngine.approve(
                proposal,
                approver="Charles Earl Lipshay",
                approver_type="human",
                passed_gates=proposal.required_gates,
            )

    def test_bounded_green_mutation_can_be_approved_for_pilot(self):
        proposal = build_engine().propose_mutation(
            "python_testing", "Add a bounded test-training exercise"
        )
        approved = EvolutionEngine.approve(
            proposal,
            approver="Charles Earl Lipshay",
            approver_type="human",
            passed_gates=proposal.required_gates,
            conditions=["sandbox only", "no production deployment"],
        )
        self.assertEqual(approved.status, "approved_for_bounded_pilot")
        self.assertTrue(EvolutionEngine.release_eligible(approved, approved.required_gates))

    def test_evaluation_for_other_clone_is_rejected(self):
        passport = ClonePassport.from_dict(copy.deepcopy(PASSPORT))
        evaluation = copy.deepcopy(EVALUATIONS[0])
        evaluation["clone_id"] = "CLONE-OTHER"
        record = EvaluationRecord.from_dict(evaluation)
        with self.assertRaises(ValidationError):
            EvolutionEngine(passport, [record])


if __name__ == "__main__":
    unittest.main()
