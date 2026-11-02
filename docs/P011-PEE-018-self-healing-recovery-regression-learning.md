# P-011-PEE-018 — Self-Healing Proposal, Recovery Planning & Regression-Learning Engine

## Purpose
P11-PEE-018 converts verified incidents into bounded recovery proposals. It may diagnose, propose, simulate, compare, and prepare repair candidates, but it does not patch production or approve its own repair.

## Inputs
- incident ID and operational state;
- affected target/version;
- triggering evidence;
- approved baseline/rollback target;
- failed tests/regressions;
- error class;
- drift class;
- constraints and prohibited actions.

## Recovery proposal lifecycle
`incident -> evidence freeze -> root-cause hypotheses -> repair candidates -> sandbox tests -> baseline comparison -> red-team -> regression tests -> recovery scorecard -> owner review`

## Proposal states
- DRAFT
- TESTABLE
- TESTED
- REVIEW_READY
- APPROVED
- REJECTED
- QUARANTINED

AI may not set APPROVED.

## Required proposal contents
- proposal ID;
- incident ID;
- target/ref;
- root-cause hypothesis;
- candidate change summary;
- exact permitted scope;
- rollback target;
- deterministic tests;
- regression tests;
- expected benefit;
- known risks;
- unresolved gaps;
- evidence references;
- HumanApprovalGate state.

## Self-healing constraints
- no direct production mutation;
- no secret/credential changes;
- no scope expansion beyond incident repair without a separate work packet;
- preserve incident evidence before repair;
- prefer smallest reversible patch;
- compare repair against approved baseline;
- failed repair becomes a regression-learning record;
- successful sandbox repair remains a proposal until owner approval.

## Regression-learning output
Every material failure should create:
- failure signature;
- triggering condition;
- expected behavior;
- observed behavior;
- root-cause hypothesis;
- repair candidate;
- regression test;
- Prompt #11 lesson/update candidate;
- disposition.

## Acceptance criteria
1. deterministic recovery-planning engine exists;
2. critical incidents cannot produce an auto-apply state;
3. repair proposals require rollback target and test plan;
4. unresolved evidence gaps remain visible;
5. failed repairs create regression requirements;
6. approved state cannot be asserted without external human approval evidence;
7. no production mutation occurs.
