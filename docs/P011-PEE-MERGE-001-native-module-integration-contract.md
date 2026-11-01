# P-011-PEE-MERGE-001 — Prompt #11 Native Module Integration Contract

## Purpose
This contract makes P11-PEE-001 through P11-PEE-016 native modules of Prompt #11 rather than parallel add-ons.

## Canonical relationship
- P-011-XPIO-001 remains the master operating prompt.
- The P11-PEE module registry defines the governed extension set.
- Every substantial Prompt #11 task selects applicable P11-PEE modules by ID/version.
- Selected modules inherit XPIO authority, privacy, provenance, rollback, and HumanApprovalGate rules.
- No P11-PEE module may weaken XPIO controls.

## Native lifecycle
`task -> module selection -> composition -> Quantum Sandboxes -> Best Practices -> Council/Evidence Arbitration -> Error Barrier -> Control Tower -> Priority -> HumanApprovalGate -> Deployment Readiness -> Canary -> Telemetry/Drift -> Post-Canary Verification -> Progressive Rollout Decision -> Continuation Packet`

## Merge rules
1. Registry is canonical for P11-PEE module identity/version/status.
2. Prompt composition must reference registry entries.
3. Unknown or unregistered P11-PEE modules fail closed.
4. Review-ready modules may be tested but not treated as production-approved.
5. Canonical activation requires evidence, regression tests, approval record, and version update.
6. Continuation Packets must record active module IDs/versions.
7. GitHub remains the change-control/evidence system; runtime deployment requires separate verification.

## Acceptance criteria
- registry exists;
- XPIO references the registry;
- rollout engine exists and is tested;
- module status remains non-production until approval;
- no stage bypasses HumanApprovalGate.
