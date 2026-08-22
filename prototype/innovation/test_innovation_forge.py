import unittest
from innovation_forge import content_hash, score_innovation, recommendation, release_eligible

BASE={"strategic_value":9,"customer_value":8,"learning_value":9,"reuse_value":9,"feasibility":7,"evidence_readiness":6,"risk_penalty":4,"risk_gate":"Yellow"}

class InnovationForgeTests(unittest.TestCase):
    def test_hash_deterministic(self): self.assertEqual(content_hash({"a":1,"b":2}),content_hash({"b":2,"a":1}))
    def test_score_range(self): self.assertTrue(0<=score_innovation(BASE)<=100)
    def test_risk_penalty_lowers_score(self):
        high=dict(BASE); high["risk_penalty"]=9
        self.assertLess(score_innovation(high),score_innovation(BASE))
    def test_red_stops(self):
        x=dict(BASE); x["risk_gate"]="Red"
        self.assertEqual(recommendation(x),"STOP")
    def test_orange_sandbox(self):
        x=dict(BASE); x["risk_gate"]="Orange"
        self.assertEqual(recommendation(x),"RESEARCH_OR_SANDBOX")
    def test_priority_pilot(self):
        high=dict(BASE); high.update({"strategic_value":10,"customer_value":10,"learning_value":10,"reuse_value":10,"feasibility":9,"evidence_readiness":8,"risk_penalty":2})
        self.assertEqual(recommendation(high),"PRIORITY_PILOT")
    def test_q3_not_release(self): self.assertFalse(release_eligible("Q3","Green",{},"Approved"))
    def test_human_required(self): self.assertFalse(release_eligible("Q4","Green",{},"Pending"))
    def test_red_not_release(self): self.assertFalse(release_eligible("Q4","Red",{},"Approved"))
    def test_all_critical_gates_required(self): self.assertFalse(release_eligible("Q4","Green",{"IdentityGate":"Pass"},"Approved"))
    def test_complete_release(self):
        gates={g:"Pass" for g in ["IdentityGate","ConsentGate","PrivacyGate","SecurityGate","RightsGate","MutationSafetyGate","HumanApprovalGate"]}
        self.assertTrue(release_eligible("Q4","Green",gates,"Approved"))

if __name__=="__main__": unittest.main()
