import unittest
from crm_contract_smoke import stable_id, consent_allows, route_mission, release_eligibility, canonical_hash

class CRMContractSmokeTests(unittest.TestCase):
    def test_id_is_deterministic(self):
        self.assertEqual(stable_id('CRM-PTY','Avery','Example'),stable_id('CRM-PTY',' avery ','example'))
    def test_hash_is_order_independent(self):
        self.assertEqual(canonical_hash({'a':1,'b':2}),canonical_hash({'b':2,'a':1}))
    def test_consent_requires_all_controls(self):
        self.assertTrue(consent_allows('granted','not_suppressed',True))
        self.assertFalse(consent_allows('revoked','not_suppressed',True))
        self.assertFalse(consent_allows('granted','suppressed',True))
    def test_support_route_requires_human(self):
        m=route_mission('support.overdue'); self.assertTrue(m['requires_human_approval']); self.assertIn('CorrectionGate',m['required_gates'])
    def test_learning_route_is_bounded(self):
        m=route_mission('learner.stalled'); self.assertFalse(m['requires_human_approval']); self.assertIn('AccessibilityGate',m['required_gates'])
    def test_partner_route_has_revenue_integrity(self):
        self.assertIn('RevenueIntegrityGate',route_mission('affiliate.disclosure_missing')['required_gates'])
    def test_no_route_grants_financial_or_identity_authority(self):
        for event in ['lead.qualified','learner.stalled','support.overdue','affiliate.disclosure_missing','privacy.requested']:
            prohibited=route_mission(event)['prohibited_actions']; self.assertIn('financial_action',prohibited); self.assertIn('identity_merge',prohibited)
    def test_q2_is_not_release_eligible(self):
        gates=[{'gate_name':'HumanApprovalGate','critical':True,'status':'Pending','reviewer_type':'human'}]
        ok,reasons=release_eligibility(gates,'Q2','Yellow'); self.assertFalse(ok); self.assertIn('minimum Q4 required',reasons)
    def test_human_q4_can_be_eligible(self):
        gates=[{'gate_name':'HumanApprovalGate','critical':True,'status':'Approved','reviewer_type':'human'}]
        ok,reasons=release_eligibility(gates,'Q4','Green'); self.assertTrue(ok); self.assertEqual(reasons,[])
    def test_ai_cannot_satisfy_human_approval(self):
        gates=[{'gate_name':'HumanApprovalGate','critical':True,'status':'Approved','reviewer_type':'ai'}]
        ok,reasons=release_eligibility(gates,'Q4','Green'); self.assertFalse(ok); self.assertTrue(any('HumanApprovalGate' in r for r in reasons))

if __name__=='__main__': unittest.main()
