import unittest

from crm_evolution_engine import (
    CRITICAL_GATES,
    canonical_json,
    compile_review,
    gate_blockers,
    pilot_eligible,
    propose_evolution,
    quality_score,
    release_eligible,
    stable_id,
)


class CrmEvolutionEngineTests(unittest.TestCase):
    def test_canonical_json_is_deterministic(self):
        self.assertEqual(canonical_json({"b": 2, "a": 1}), canonical_json({"a": 1, "b": 2}))

    def test_stable_id_is_deterministic(self):
        self.assertEqual(stable_id("SIG", {"a": 1}), stable_id("SIG", {"a": 1}))

    def test_quality_score(self):
        metrics = {
            "evidence": 90,
            "tests": 90,
            "data_quality": 80,
            "consent": 90,
            "privacy_security": 85,
            "service_learning": 80,
            "accessibility_fairness": 75,
            "correction_provider": 80,
        }
        self.assertEqual(quality_score(metrics), 84.75)

    def test_quality_score_rejects_missing_metric(self):
        with self.assertRaises(ValueError):
            quality_score({"evidence": 100})

    def test_compile_review_is_human_controlled(self):
        mission = compile_review({
            "signal_id": "SIG-001",
            "correlation_id": "COR-001",
            "required_gates": ["PrivacyGate"],
        })
        self.assertTrue(mission["review_only"])
        self.assertEqual(mission["human_approval"], "Pending")
        self.assertIn("HumanApprovalGate", mission["required_gates"])

    def test_evolution_proposal_is_sandbox_only(self):
        signal = {"signal_id": "SIG-001", "correlation_id": "COR-001", "event_type": "quality"}
        mission = compile_review(signal)
        proposal = propose_evolution(signal, mission)
        self.assertTrue(proposal["sandbox_only"])
        self.assertFalse(proposal["auto_deploy"])
        self.assertEqual(proposal["human_approval"], "Pending")

    def test_gate_blockers(self):
        gates = {gate: "Pass" for gate in CRITICAL_GATES}
        gates["SecurityGate"] = "Pending"
        self.assertEqual(gate_blockers(gates), ["SecurityGate"])

    def test_pilot_requires_human_approval(self):
        gates = {gate: "Pass" for gate in CRITICAL_GATES}
        proposal = {"risk_gate": "Yellow", "sandbox_only": True, "auto_deploy": False}
        self.assertFalse(pilot_eligible(proposal, gates, "Pending"))
        self.assertTrue(pilot_eligible(proposal, gates, "Approved"))

    def test_release_requires_q4(self):
        gates = {gate: "Pass" for gate in CRITICAL_GATES}
        self.assertFalse(release_eligible("Q3", "Yellow", gates, "Approved"))
        self.assertTrue(release_eligible("Q4", "Yellow", gates, "Approved"))

    def test_red_risk_blocks_pilot_and_release(self):
        gates = {gate: "Pass" for gate in CRITICAL_GATES}
        proposal = {"risk_gate": "Red", "sandbox_only": True, "auto_deploy": False}
        self.assertFalse(pilot_eligible(proposal, gates, "Approved"))
        self.assertFalse(release_eligible("Q4", "Red", gates, "Approved"))


if __name__ == "__main__":
    unittest.main()
