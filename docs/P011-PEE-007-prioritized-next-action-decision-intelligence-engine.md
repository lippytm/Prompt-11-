# P-011-PEE-007 — Prioritized Next-Action & Decision Intelligence Engine

## Purpose

P11-PEE-007 extends the Control Tower from status reporting to deterministic prioritization of the next safest, highest-value action.

It does not execute actions. It ranks recommendations for owner review.

## Inputs

- Control Tower traffic-light state;
- failed critical gates;
- unresolved risks;
- failed regressions;
- evidence completeness;
- Quantum Sandbox status;
- model disagreements;
- rollback readiness;
- cost/performance signals;
- business/learning/project priority;
- dependencies and blockers.

## Priority order

1. RED: stop, contain, preserve evidence, escalate.
2. ORANGE: repair high-risk/regression/rollback gaps before new capability work.
3. YELLOW: close evidence gaps, resolve disagreements, run missing noncritical tests.
4. GREEN + approval pending: prepare concise owner decision packet.
5. GREEN + approved: recommend the next bounded implementation or controlled canary.

## Recommendation classes

- STOP_AND_ESCALATE
- QUARANTINE
- REPAIR_REGRESSION
- COMPLETE_ROLLBACK
- COLLECT_EVIDENCE
- RUN_RED_TEAM
- ROUTE_TO_IF
- ROUTE_TO_MAYBE
- ROUTE_TO_WHY_NOT
- ROUTE_TO_DONT_DO_THAT
- ROUTE_TO_FAILURE_FORENSICS
- RESOLVE_MODEL_DISAGREEMENT
- REDUCE_CONTEXT
- RUN_COMPARATIVE_EVAL
- PREPARE_OWNER_REVIEW
- PREPARE_CANARY
- CONTINUE_BOUNDED_BUILD

## Best-practice constraints

Recommendations must:
- cite the blocking evidence/gate;
- preserve human authority;
- remain non-executing;
- prefer the smallest reversible next step;
- avoid optimizing cost before correctness/safety;
- identify dependencies;
- identify what would change the recommendation.

## Acceptance criteria

P11-PEE-007 v0.1 is review-ready when deterministic tests prove:
- RED always outranks feature work;
- failed high-severity regression outranks new capability work;
- missing rollback outranks optimization;
- missing evidence routes to evidence collection;
- unresolved model disagreement routes to comparison/review;
- GREEN + pending human approval routes to owner review;
- no recommendation can directly activate production.
