# P-011-PEE-015 — Canary Telemetry, Drift Detection & Baseline Comparison Engine

## Purpose
P11-PEE-015 compares canary behavior against the approved baseline and classifies measurable drift before wider rollout.

It is deterministic, advisory, and non-deploying.

## Telemetry dimensions
- success rate;
- failure rate;
- critical error count;
- high-severity regression count;
- evidence completeness;
- latency;
- retry count;
- tool-call count;
- output-schema pass rate;
- cost estimate when available;
- owner-visible disagreement count.

## Drift classes
- NO_DRIFT
- IMPROVEMENT
- ACCEPTABLE_DRIFT
- MATERIAL_DRIFT
- CRITICAL_DRIFT
- INSUFFICIENT_DATA

## Core rules
- critical error increase => CRITICAL_DRIFT;
- high-severity regression increase => CRITICAL_DRIFT;
- output-schema pass-rate degradation >= 10 percentage points => MATERIAL_DRIFT;
- success-rate degradation >= 10 percentage points => MATERIAL_DRIFT;
- evidence-completeness degradation >= 10 percentage points => MATERIAL_DRIFT;
- latency/cost regressions alone are not critical unless explicitly declared as a hard requirement;
- missing baseline/candidate samples => INSUFFICIENT_DATA;
- measurable improvement may be recorded but never bypasses governance or HumanApprovalGate.

## Integration with P11-PEE-014
- CRITICAL_DRIFT => ROLLBACK or ESCALATE according to cause;
- MATERIAL_DRIFT => HOLD or ROLLBACK recommendation;
- ACCEPTABLE_DRIFT => HOLD or CONTINUE depending on owner-approved thresholds;
- NO_DRIFT / IMPROVEMENT => may continue to owner review.

## Acceptance criteria
1. telemetry packet schema exists;
2. deterministic baseline comparator exists;
3. critical errors/regressions dominate performance improvements;
4. material quality degradation blocks continue;
5. insufficient data never recommends continue;
6. post-canary verifier can consume drift state;
7. no live deployment or automatic rollback occurs.
