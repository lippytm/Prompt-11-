# P-011-PEE-014 — Post-Deployment Verification & Rollback Recommendation Engine

## Purpose
P11-PEE-014 evaluates canary results against an approved baseline and recommends one of four advisory outcomes:
- CONTINUE
- HOLD
- ROLLBACK
- ESCALATE

It never executes rollback or production changes.

## Inputs
- canary manifest ID;
- candidate ref;
- baseline ref;
- success/failure criteria results;
- critical error count;
- high-severity regression count;
- security/privacy violations;
- rollback verification state;
- evidence completeness;
- post-canary verification status.

## Rules
- any security/privacy violation => ESCALATE;
- any critical error => ROLLBACK;
- rollback verification failure => ESCALATE;
- failed high-severity regression => ROLLBACK;
- incomplete evidence or incomplete post-canary verification => HOLD;
- all required checks pass => CONTINUE.

## Output
- recommendation;
- rationale;
- owner_review_required=true;
- executes_rollback=false;
- production_activation=false.

## Acceptance criteria
1. deterministic recommendation engine exists;
2. critical/security failures cannot recommend continue;
3. incomplete verification cannot recommend continue;
4. rollback remains advisory;
5. owner review remains required.
