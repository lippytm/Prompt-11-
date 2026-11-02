# P-011-PEE-017 — Continuous Production Monitoring, Incident Detection & Safe Rollback Orchestration

## Purpose
P11-PEE-017 extends Prompt #11 beyond rollout decisions into continuous operational observation.

It consumes structured production telemetry and incident signals, classifies operational state, preserves evidence, and recommends containment, rollback, or escalation. It does not execute rollback or production mutations.

## Monitoring inputs
- availability/health state;
- success and failure rates;
- critical error count;
- high-severity regression count;
- security/privacy violations;
- drift class;
- evidence completeness;
- rollback health;
- deployment/version identity;
- current rollout stage;
- incident status.

## Operational states
- HEALTHY
- DEGRADED
- INCIDENT
- CRITICAL_INCIDENT
- UNKNOWN

## Advisory actions
- OBSERVE
- INVESTIGATE
- CONTAIN
- HOLD_ROLLOUT
- ROLLBACK_RECOMMENDED
- ESCALATE

## Rules
- security/privacy violation => CRITICAL_INCIDENT + ESCALATE;
- rollback unavailable during material incident => CRITICAL_INCIDENT + ESCALATE;
- increased critical errors => INCIDENT + ROLLBACK_RECOMMENDED;
- high-severity regression => INCIDENT + ROLLBACK_RECOMMENDED;
- MATERIAL_DRIFT => INCIDENT + HOLD_ROLLOUT or ROLLBACK_RECOMMENDED;
- CRITICAL_DRIFT => CRITICAL_INCIDENT + ROLLBACK_RECOMMENDED;
- incomplete/unknown evidence => DEGRADED + INVESTIGATE;
- healthy metrics and complete evidence => HEALTHY + OBSERVE.

## Incident evidence packet
Every incident should preserve:
- incident ID;
- detected time;
- target/ref/version;
- triggering signals;
- affected scope;
- evidence references;
- current rollout stage;
- rollback target;
- recommended action;
- unresolved gaps;
- owner-review state.

## Safe rollback orchestration
The orchestration layer may prepare:
- rollback target;
- rollback preconditions;
- verification checklist;
- evidence-preservation checklist;
- owner approval request;
- post-rollback verification plan.

It must not execute rollback by itself.

## Integration
P11-PEE-017 consumes P11-PEE-015 drift and P11-PEE-016 rollout state.
Incident results route back to:
- P11-PEE-011 error barrier;
- P11-PEE-006 Control Tower;
- P11-PEE-007 priority engine;
- I_TOLD_YOU_NOT_TO_DO_THAT sandbox for failure forensics.

## Acceptance criteria
1. deterministic production-health evaluator exists;
2. security/privacy violations escalate;
3. critical regressions cannot remain HEALTHY;
4. rollback-unavailable incidents escalate;
5. incomplete evidence cannot be considered healthy;
6. rollback is recommendation/orchestration only;
7. owner review remains required;
8. no automatic production mutation occurs.
