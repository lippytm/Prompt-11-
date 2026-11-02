# P-011-PEE-009 — Evidence Arbitration & Council Orchestration Engine

## 1. Purpose

P-011-PEE-009 turns evidence from ChatGPT, ChatGPT Business, Claude, Gemini AI, GitHub, and Jarvis specialist agents into structured claim/evidence packets that can be compared without collapsing independent reasoning.

It provides two layers:

1. AI Sandbox Communications Workflow — controlled exchange of structured packets.
2. Evidence Arbitration Engine — deterministic comparison and routing of claims.

Neither layer executes production actions or passes HumanApprovalGate.

## 2. Communications workflow

Participants may include:
- ChatGPT;
- ChatGPT Business;
- Claude;
- Gemini AI;
- GitHub/GitHub Copilot evidence producers;
- Jarvis specialist agents;
- deterministic test runners;
- Evidence Officer;
- Red Team;
- Evaluator.

Each first-pass analysis remains isolated until its independent position is recorded.

After first-pass freeze, structured messages may be exchanged through a sandbox envelope.

## 3. Sandbox message envelope

Each message records:
- message_id;
- conversation/work packet;
- sender;
- recipient(s);
- sender type/model/role;
- prompt module/version;
- phase: FIRST_PASS, EVIDENCE_EXCHANGE, REBUTTAL, ARBITRATION, REVIEW;
- claim IDs referenced;
- evidence IDs referenced;
- payload type;
- payload summary;
- independence_preserved;
- production_activation=false.

FIRST_PASS messages may not contain another member's conclusion.

## 4. Claim record

Each material claim records:
- claim_id;
- claimant;
- claim text;
- claim type;
- confidence;
- evidence references;
- assumptions;
- falsification/test condition;
- status.

Claim types:
- FACT;
- INTERPRETATION;
- DESIGN;
- RISK;
- POLICY;
- COST_PERFORMANCE;
- PREDICTION;
- UNKNOWN.

## 5. Evidence record

Each evidence item records:
- evidence_id;
- source type;
- source locator;
- source version/date when available;
- evidence class;
- independence group;
- freshness;
- directness;
- verification state;
- limitations.

Evidence classes include:
- DETERMINISTIC_TEST;
- PRIMARY_SOURCE;
- REPOSITORY_ARTIFACT;
- TOOL_OUTPUT;
- SECONDARY_SOURCE;
- MODEL_ASSERTION;
- USER_PROVIDED;
- SYNTHETIC_TEST_FIXTURE.

A MODEL_ASSERTION cannot independently verify another model assertion.

## 6. Arbitration rules

### Supported claim
A claim is SUPPORTED only when it has qualifying evidence and no unresolved contradictory higher-priority evidence.

### Unsupported agreement
Multiple models agreeing without independent evidence is PROVISIONAL, not verified.

### Contradictory evidence
Route according to conflict:
- deterministic test conflict -> rerun/reproduce;
- primary-source conflict -> verify version/date/context;
- factual claim conflict -> collect authoritative evidence;
- risk conflict -> conservative state + red-team;
- policy conflict -> STOP_AND_ESCALATE / owner review;
- design conflict -> bounded comparative evaluation.

### Stale evidence
Evidence known to be stale cannot establish current-state truth without revalidation.

### Circular evidence
Evidence chains that ultimately cite the same model output/source are one independence group, not multiple confirmations.

## 7. Evidence strength ordering

Default ordering for a claim where applicable:
1. reproducible deterministic test;
2. directly relevant primary/authoritative source;
3. verified repository artifact or tool output;
4. corroborated secondary evidence;
5. model assertion or unverified interpretation.

This ordering is contextual, not absolute. Policy authority may override empirical preference where policy is the governing question.

## 8. Orchestration routes

Arbitration outputs one advisory route:
- VERIFIED_SUPPORT -> PREPARE_OWNER_REVIEW
- PROVISIONAL_SUPPORT -> COLLECT_EVIDENCE
- FACT_CONFLICT -> COLLECT_AUTHORITATIVE_EVIDENCE_OR_RUN_TEST
- DESIGN_CONFLICT -> ROUTE_TO_WHY_NOT / RUN_COMPARATIVE_EVAL
- RISK_CONFLICT -> ROUTE_TO_DONT_DO_THAT / RUN_RED_TEAM
- POLICY_CONFLICT -> STOP_AND_ESCALATE
- INCIDENT_CONFLICT -> ROUTE_TO_FAILURE_FORENSICS
- STALE_EVIDENCE -> REFRESH_EVIDENCE
- CIRCULAR_EVIDENCE -> COLLECT_INDEPENDENT_EVIDENCE
- INSUFFICIENT_EVIDENCE -> COLLECT_EVIDENCE

## 9. GitHub role

GitHub is treated as an evidence and change-control participant, not a reasoning model.

GitHub may contribute:
- commit SHA;
- file/blob SHA;
- PR state;
- test workflow output;
- changed-file evidence;
- issue/PR review findings;
- repository version and branch provenance.

GitHub artifacts do not prove runtime deployment unless runtime/deployment evidence independently verifies it.

## 10. Performance advantages of the sandbox communications workflow

The workflow should improve system performance by:
- preventing early cross-model anchoring;
- reducing duplicated context;
- allowing each model to specialize;
- making disagreement machine-readable;
- attaching evidence to claims rather than prose threads;
- avoiding repeated full-context transfers;
- enabling selective rebuttal only on disputed claims;
- preserving GitHub/test artifacts as deterministic evidence;
- reducing circular validation;
- making routing deterministic.

Performance improvements must still be measured; architecture alone does not prove lower cost, latency, or higher quality.

## 11. Acceptance criteria

P11-PEE-009 v0.1 is review-ready when:
1. communication-envelope schema exists;
2. claim/evidence schema exists;
3. deterministic evidence arbitrator exists;
4. circular model-only agreement is not verified;
5. contradictory policy evidence stops/escalates;
6. factual conflicts route to evidence/test;
7. risk conflicts route conservatively;
8. stale evidence is rejected for current claims;
9. first-pass independence can be represented and checked;
10. no communication or arbitration path activates production.
