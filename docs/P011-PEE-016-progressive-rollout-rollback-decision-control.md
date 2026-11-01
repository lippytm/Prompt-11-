# P-011-PEE-016 — Progressive Rollout & Rollback Decision Control

## Purpose
P11-PEE-016 governs what happens after a canary has been reviewed. It converts verified canary evidence into an advisory rollout-stage recommendation while preserving HumanApprovalGate and rollback readiness.

It never expands rollout or executes rollback automatically.

## Rollout stages
- CANARY
- LIMITED
- PARTIAL
- BROAD
- FULL

## Inputs
- current rollout stage;
- P11-PEE-014 recommendation;
- P11-PEE-015 drift class;
- Control Tower state;
- HumanApprovalGate state;
- rollback readiness;
- evidence completeness;
- unresolved high/critical risks;
- owner-approved maximum next stage.

## Rules
- ESCALATE => no rollout expansion.
- ROLLBACK => recommend rollback to approved baseline.
- HOLD => remain at current stage.
- CONTINUE + NO_DRIFT/IMPROVEMENT + GREEN + owner approval + rollback ready => advance by at most one stage.
- ACCEPTABLE_DRIFT may advance only with explicit owner approval and no unresolved high/critical risk.
- MATERIAL/CRITICAL_DRIFT never advances.
- no stage skipping.
- rollback target must always be the approved baseline or explicitly approved prior stage.

## Acceptance criteria
1. deterministic stage-decision engine exists;
2. rollout can advance by at most one stage;
3. critical/material drift cannot advance;
4. no owner approval => no stage advance;
5. no rollback readiness => no stage advance;
6. HOLD preserves current stage;
7. ROLLBACK recommends baseline restoration only;
8. engine itself performs no deployment.
