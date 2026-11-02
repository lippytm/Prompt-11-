# P-011-PEE-019 — Autonomous Root-Cause Analysis, Failure Signature Memory & Repair Candidate Ranking Engine

## Purpose
P11-PEE-019 strengthens AI Building Better AI by converting incidents and failed repairs into reusable failure signatures, then ranking multiple repair candidates using deterministic evidence.

It may analyze, compare, rank, and recommend. It may not self-approve or patch production.

## Failure signature
A failure signature records:
- signature_id;
- incident/error class;
- affected component;
- triggering condition;
- observed behavior;
- expected behavior;
- evidence references;
- recurrence count;
- known root-cause hypotheses;
- prior repair attempts;
- regression tests;
- last verified disposition.

Failure signatures are reusable only after evidence review.

## Root-cause analysis
Root-cause hypotheses should be ranked by:
- evidence coverage;
- deterministic reproduction;
- causal proximity;
- consistency with known failure signature;
- contradiction count;
- unresolved assumptions.

The engine must preserve multiple hypotheses when evidence is inconclusive.

## Repair candidate ranking
Each candidate is scored on:
- deterministic tests: 20
- regression coverage: 20
- reversibility/rollback: 15
- evidence completeness: 15
- scope discipline: 10
- risk reduction: 10
- simplicity/maintainability: 5
- cost/performance impact: 5

Critical gates override score.

## Critical gates
A repair cannot rank as READY_FOR_OWNER_REVIEW when:
- rollback is unverified;
- required deterministic tests fail;
- required regression tests fail;
- high/critical unresolved risk remains;
- permitted scope is exceeded;
- security/privacy/authority gate fails.

## Ranking output
- candidate_id;
- score;
- critical_gates_passed;
- rank;
- recommendation;
- reasons;
- unresolved gaps;
- production_mutation_allowed=false;
- human_approval_required=true.

## Recommendations
- READY_FOR_OWNER_REVIEW
- REPAIR_AND_RETEST
- COLLECT_EVIDENCE
- REDUCE_SCOPE
- VERIFY_ROLLBACK
- RUN_RED_TEAM
- QUARANTINE

## Regression learning
A failed candidate creates or updates:
- failure signature;
- regression test;
- rejected repair pattern;
- reason for rejection;
- Prompt #11 lesson candidate.

## Acceptance criteria
1. failure-signature schema exists;
2. deterministic repair-candidate ranker exists;
3. failed critical gate overrides high numeric score;
4. recurring failure signatures can increase evidence relevance but not replace fresh verification;
5. multiple root-cause hypotheses can remain unresolved;
6. rejected repairs are retained as regression-learning records;
7. owner approval remains external;
8. no production mutation occurs.
