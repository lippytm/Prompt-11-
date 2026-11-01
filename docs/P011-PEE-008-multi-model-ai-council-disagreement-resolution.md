# P-011-PEE-008 — Multi-Model AI Council & Disagreement Resolution Layer

## 1. Purpose

P-011-PEE-008 coordinates independent analysis from ChatGPT, Claude, Gemini AI, and Jarvis specialist agents without treating model consensus as proof.

The council is advisory. HumanApprovalGate remains external.

## 2. Council members

Core model lines:
- ChatGPT;
- Claude;
- Gemini AI;
- Jarvis specialist agents.

Jarvis specialist examples:
- Prompt Architect;
- Context Engineer;
- Copilot Engineer;
- Test Engineer;
- Evidence Officer;
- Red Team;
- Evaluator;
- Evolution Engineer;
- Hermes Dispatcher;
- MemPalace Librarian;
- Release Manager.

## 3. Independence rule

Where comparison matters, each model/member should receive the same task contract and authoritative evidence set without seeing other first-pass conclusions.

After independent first pass:
1. normalize claims;
2. map evidence;
3. identify agreement;
4. identify disagreement;
5. identify unsupported claims;
6. route unresolved disputes to additional evidence, testing, red-team, or owner review.

One model repeating another is not independent verification.

## 4. Council position record

Each member records:
- member_id;
- model/provider/role;
- task_id;
- position;
- confidence;
- evidence references;
- assumptions;
- uncertainties;
- recommended action;
- prohibited/unsafe action warnings;
- unresolved questions.

## 5. Disagreement classes

- FACTUAL: members disagree about a verifiable fact.
- INTERPRETATION: same evidence, different interpretation.
- DESIGN: different architecture or implementation choice.
- RISK: disagreement over severity/likelihood/control.
- EVIDENCE: disagreement over source sufficiency or provenance.
- POLICY: disagreement over authority, approval, privacy, or governance.
- COST_PERFORMANCE: tradeoff disagreement.
- UNKNOWN: unresolved classification.

## 6. Resolution rules

### Critical policy/security disagreement
Do not vote. Route to STOP/owner review or authoritative policy evidence.

### Factual disagreement
Seek primary/authoritative evidence or deterministic test.

### Design disagreement
Run bounded comparison or ablation against declared rubric.

### Risk disagreement
Use the more conservative unresolved risk state until evidence resolves it.

### Evidence disagreement
Collect better evidence; do not average confidence.

### Cost/performance disagreement
Measure actual cost/latency/quality where possible.

## 7. Consensus levels

- VERIFIED_CONSENSUS: members agree and claim is supported by independent evidence/test.
- PROVISIONAL_CONSENSUS: members agree but evidence remains incomplete.
- SPLIT_DECISION: material disagreement remains.
- BLOCKED_DISAGREEMENT: disagreement touches critical authority/security/privacy/gate.
- INSUFFICIENT_EVIDENCE: no defensible resolution.

Consensus never equals approval.

## 8. Council scorecard

Track:
- participating members;
- independent first-pass completeness;
- evidence coverage;
- supported claims;
- unsupported claims;
- disagreement count by class;
- high-severity disagreement count;
- red-team objections;
- deterministic test results;
- recommended resolution route;
- owner-review requirement.

## 9. Anti-groupthink controls

- preserve minority positions;
- do not weight confidence by eloquence;
- do not use majority vote for factual truth;
- do not let the producer be sole evaluator;
- rotate evaluator roles where practical;
- require evidence links for material claims;
- retain dissent through owner review;
- allow “insufficient evidence” as a valid outcome.

## 10. Integration with Quantum Sandboxes

- IF: council compares hypotheses and test designs.
- MAYBE: council exposes uncertainty and alternative explanations.
- WHY NOT: council proposes competing architectures.
- DONT_DO_THAT: council red-teams risks and authority violations.
- I_TOLD_YOU_NOT_TO_DO_THAT: council compares incident root-cause hypotheses and recovery proposals.

## 11. Integration with P11-PEE-007

P11-PEE-007 receives council state:
- unresolved critical disagreement -> STOP_AND_ESCALATE;
- unresolved noncritical disagreement -> RESOLVE_MODEL_DISAGREEMENT;
- insufficient evidence -> COLLECT_EVIDENCE;
- verified consensus with gates passing -> continue owner-review path.

## 12. Acceptance criteria

P11-PEE-008 v0.1 is review-ready when:
1. council position schema exists;
2. deterministic resolver exists;
3. majority vote cannot override critical disagreement;
4. unsupported consensus remains provisional/insufficient;
5. factual disagreement routes to evidence/test;
6. risk disagreement is conservatively handled;
7. minority positions are preserved;
8. resolver never activates production;
9. HumanApprovalGate remains external.
