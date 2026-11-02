# P-011-PEE-006 — AI Control Tower & Best-Practice Scoreboard

## 1. Purpose

P-011-PEE-006 consolidates Prompt #11 engineering state into one owner-facing decision packet. It does not make autonomous release decisions. It summarizes evidence, risk, regressions, Quantum Sandbox outputs, best-practice compliance, model disagreements, cost/performance signals, and next actions for human review.

## 2. Control Tower inputs

The Control Tower may consume only structured, provenance-carrying records from:
- Prompt candidate records;
- Prompt composition manifests;
- IF / MAYBE / WHY_NOT / DONT_DO_THAT / I_TOLD_YOU_NOT_TO_DO_THAT sandbox packets;
- Best Practice Attestations;
- deterministic test results;
- red-team findings;
- incident and regression records;
- model-comparison results;
- cost/latency telemetry;
- approved project continuation packets.

## 3. Owner-facing decision packet

Every Control Tower packet should contain:
- packet ID and version;
- project/work-packet identifier;
- Prompt #11 module IDs and versions;
- current lifecycle state;
- five-sandbox status;
- critical-gate status;
- best-practice scorecard;
- evidence completeness;
- regression count and severity;
- unresolved high-severity risks;
- model disagreements;
- cost/performance observations;
- rollback readiness;
- recommended next action;
- blocked actions;
- human approval state.

## 4. Scoreboard dimensions

Default scoreboard:
- governance and authority: 15
- evidence/provenance: 15
- testing/regression: 15
- security/privacy: 10
- red-team/risk: 10
- reliability/recovery: 10
- context/prompt quality: 10
- observability/continuity: 5
- cost/performance: 5
- maintainability/reusability: 5

Total: 100.

A score is advisory. A failed critical gate overrides the score.

## 5. Traffic-light state

- GREEN: all critical gates pass; no unresolved high-severity regression; owner review may proceed.
- YELLOW: no critical violation, but unresolved medium-risk gaps, incomplete evidence, disagreement, or missing noncritical tests remain.
- ORANGE: high-risk unresolved issue, material regression, or rollback/recovery gap; promotion blocked.
- RED: failed authority/privacy/security/critical evidence gate, prohibited action, or severe incident; stop work and escalate.

## 6. Five-sandbox aggregation

The Control Tower does not collapse the sandboxes into one opaque answer. It preserves each contribution:

- IF: hypothesis, experiment, pass/fail condition.
- MAYBE: uncertainty, alternatives, missing data.
- WHY NOT: alternative designs and opportunity set.
- DONT_DO_THAT: risk, threat model, prohibited actions, rollback.
- I_TOLD_YOU_NOT_TO_DO_THAT: incident evidence, root-cause hypothesis, recovery, regression requirement.

Disagreements are recorded, not silently averaged away.

## 7. Best-practice scoreboard

For each applicable practice domain:
- status: pass / partial / fail / not-applicable;
- evidence reference;
- tests;
- deviations;
- owner-visible rationale.

Critical practices cannot be marked not-applicable without a rationale.

## 8. Multi-model comparison

When multiple model lines are used:
- record model/provider/version when available;
- keep independent first-pass outputs separate;
- track agreement/disagreement;
- record which claims were independently verified;
- do not let majority vote replace evidence;
- do not let one model approve another model's release.

## 9. Cost and performance

Where measured, record:
- input/context size;
- output size;
- latency;
- retry count;
- tool calls;
- estimated cost;
- test pass rate;
- failure rate;
- regression delta versus approved baseline.

Optimization must not trade away required correctness, governance, or safety gates.

## 10. Recommended next action engine

Recommendations may include:
- continue experiment;
- collect missing evidence;
- rerun a specific test;
- route to a Quantum Sandbox;
- repair a regression;
- perform red-team review;
- reduce context;
- compare an alternate model;
- prepare owner review;
- stop work / quarantine.

Recommendations are advisory and non-executing.

## 11. Deterministic release-state rules

Promotion is blocked when any of these are true:
- a critical gate fails;
- best-practice attestation reports promotion_blocked;
- unresolved high/critical risk exists;
- a required regression test fails;
- rollback/recovery is missing for a material change;
- HumanApprovalGate is pending for an action requiring it.

## 12. Acceptance criteria

P11-PEE-006 v0.1 is review-ready when:
1. Control Tower packet schema exists;
2. deterministic scoreboard implementation exists;
3. critical-gate failures override high numeric scores;
4. unresolved high-severity risks block promotion;
5. owner approval remains external;
6. Quantum Sandbox provenance is preserved;
7. no model or network call is required for core scoring;
8. tests cover GREEN/YELLOW/ORANGE/RED outcomes;
9. evidence and limitations are recorded.
