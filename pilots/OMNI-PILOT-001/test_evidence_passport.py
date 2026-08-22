"""Unit tests for the beginner Evidence Passport lab."""

import unittest

from evidence_passport import content_hash, example_passport, release_decision, validate_passport


class EvidencePassportTests(unittest.TestCase):
    def test_q3_sample_is_review_only(self) -> None:
        report = release_decision(example_passport())
        self.assertEqual(report["decision"], "REVIEW_ONLY")

    def test_verified_fact_requires_source(self) -> None:
        passport = example_passport()
        passport.update({"truth_label": "VF", "fiction_disclosure": False})
        issues = validate_passport(passport)
        self.assertTrue(any("source_url" in issue for issue in issues))

    def test_fiction_requires_disclosure(self) -> None:
        passport = example_passport()
        passport["fiction_disclosure"] = False
        issues = validate_passport(passport)
        self.assertIn("FD content requires fiction_disclosure=true", issues)

    def test_restricted_content_cannot_publish(self) -> None:
        passport = example_passport()
        passport["privacy_class"] = "Restricted"
        report = release_decision(passport)
        self.assertEqual(report["decision"], "BLOCKED")

    def test_red_risk_blocks(self) -> None:
        passport = example_passport()
        passport["risk_gate"] = "Red"
        report = release_decision(passport)
        self.assertEqual(report["decision"], "BLOCKED")

    def test_q4_still_requires_human_approval(self) -> None:
        passport = example_passport()
        passport.update({
            "product_stage": "Q4",
            "risk_gate": "Green",
            "critical_gates_passed": True,
            "human_approval": "Pending",
        })
        report = release_decision(passport)
        self.assertEqual(report["decision"], "REVIEW_ONLY")

    def test_approved_q4_is_only_eligible_for_human_release(self) -> None:
        passport = example_passport()
        passport.update({
            "product_stage": "Q4",
            "risk_gate": "Green",
            "critical_gates_passed": True,
            "human_approval": "Approved",
        })
        report = release_decision(passport)
        self.assertEqual(report["decision"], "ELIGIBLE_FOR_AUTHORIZED_HUMAN_RELEASE")

    def test_hash_is_stable_across_key_order(self) -> None:
        passport = example_passport()
        reversed_passport = dict(reversed(list(passport.items())))
        self.assertEqual(content_hash(passport), content_hash(reversed_passport))


if __name__ == "__main__":
    unittest.main()
