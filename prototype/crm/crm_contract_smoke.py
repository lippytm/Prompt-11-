from __future__ import annotations

import hashlib
import json
from typing import Iterable

CRITICAL_GATES = {
    'PurposeGate','ConsentGate','DataMinimizationGate','IdentityResolutionGate','DuplicateGate',
    'AccuracyGate','FreshnessGate','PrivacyGate','SecurityGate','AccessibilityGate','FairnessGate',
    'CommunicationGate','ServiceQualityGate','LearningOutcomeGate','AttributionGate',
    'RevenueIntegrityGate','RetentionGate','CorrectionGate','FinancialAuthorityGate','HumanApprovalGate'
}


def stable_id(prefix: str, *parts: object) -> str:
    canonical='|'.join(str(p).strip().lower() for p in parts)
    return f"{prefix}-{hashlib.sha256(canonical.encode()).hexdigest()[:16].upper()}"


def consent_allows(status: str, suppression_status: str, verified_contact: bool) -> bool:
    return status in {'granted','not_required'} and suppression_status=='not_suppressed' and verified_contact


ROUTES = {
    'lead.qualified': ('lead_followup', True, ['PurposeGate','ConsentGate','CommunicationGate','HumanApprovalGate']),
    'learner.stalled': ('learner_success', False, ['PurposeGate','AccessibilityGate','LearningOutcomeGate']),
    'support.overdue': ('support_escalation', True, ['ServiceQualityGate','CorrectionGate','HumanApprovalGate']),
    'affiliate.disclosure_missing': ('partner_review', True, ['AttributionGate','RevenueIntegrityGate','HumanApprovalGate']),
    'privacy.requested': ('privacy_rights', True, ['PrivacyGate','IdentityResolutionGate','HumanApprovalGate']),
}


def route_mission(event_type: str) -> dict:
    mission_type, human, gates = ROUTES.get(event_type,('quality_review',True,['PurposeGate','HumanApprovalGate']))
    return {
        'mission_id': stable_id('CRM-MSN',event_type,mission_type),
        'mission_type': mission_type,
        'requires_human_approval': human,
        'required_gates': gates,
        'prohibited_actions': ['financial_action','identity_merge','consent_change','high_impact_decision'],
    }


def release_eligibility(gate_results: Iterable[dict], q_stage: str, risk_gate: str) -> tuple[bool,list[str]]:
    latest={g['gate_name']:g for g in gate_results}
    reasons=[]
    if q_stage!='Q4': reasons.append('minimum Q4 required')
    if risk_gate.lower()=='red': reasons.append('Red RiskGate')
    for gate in CRITICAL_GATES:
        result=latest.get(gate)
        if result and result.get('critical') and result.get('status') not in {'Pass','Approved'}:
            reasons.append(f"{gate}:{result.get('status')}")
    human=latest.get('HumanApprovalGate')
    if not human or human.get('status')!='Approved' or human.get('reviewer_type')!='human':
        reasons.append('HumanApprovalGate not validly approved')
    return not reasons,reasons


def canonical_hash(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
