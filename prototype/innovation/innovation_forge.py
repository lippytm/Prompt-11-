from __future__ import annotations
import hashlib, json

WEIGHTS = {"strategic_value":0.20,"customer_value":0.20,"learning_value":0.18,"reuse_value":0.14,"feasibility":0.14,"evidence_readiness":0.14}
CRITICAL_GATES = {"IdentityGate","ConsentGate","PrivacyGate","SecurityGate","RightsGate","MutationSafetyGate","HumanApprovalGate"}

def content_hash(record: dict) -> str:
    return hashlib.sha256(json.dumps(record,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def score_innovation(record: dict) -> float:
    raw=sum(float(record[k])*w for k,w in WEIGHTS.items())*10-float(record.get("risk_penalty",0))*2
    return round(max(0,min(100,raw)),1)

def recommendation(record: dict) -> str:
    if record.get("risk_gate")=="Red": return "STOP"
    if record.get("risk_gate")=="Orange": return "RESEARCH_OR_SANDBOX"
    score=score_innovation(record)
    if score>=75 and record.get("evidence_readiness",0)>=6: return "PRIORITY_PILOT"
    if score>=60: return "STRUCTURE_AND_TEST"
    return "RESEARCH"

def release_eligible(q_stage: str, risk_gate: str, gate_results: dict[str,str], human_approval: str) -> bool:
    if q_stage not in {"Q4","Q5","Q6","Q7"}: return False
    if risk_gate=="Red" or human_approval!="Approved": return False
    for gate in CRITICAL_GATES:
        if gate_results.get(gate) not in {"Pass","Approved","Not Applicable"}: return False
    return True
