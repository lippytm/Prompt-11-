# P-011-PEE-011 — Human + AI Error Prevention, Detection & Recovery Layer

## Purpose
P11-PEE-011 adds layered controls designed to reduce both human and AI mistakes before they become material actions.

## Error classes
INPUT_ERROR, ASSUMPTION_ERROR, FACTUAL_ERROR, LOGIC_ERROR, TOOL_ERROR, PERMISSION_ERROR, CONFIGURATION_ERROR, VERSION_ERROR, EVIDENCE_ERROR, COMMUNICATION_ERROR, APPROVAL_ERROR, DEPLOYMENT_ERROR, RECOVERY_ERROR, UNKNOWN.

## Prevention stack
1. explicit task contract;
2. schema/type validation;
3. independent first pass;
4. evidence/provenance check;
5. simulation/sandbox;
6. red-team/pre-mortem;
7. deterministic tests;
8. second review for material actions;
9. explicit confirmation for irreversible actions;
10. rollback/recovery readiness;
11. post-action verification;
12. incident-to-regression conversion.

## Human-error controls
- use checklists for irreversible actions;
- read back critical parameters;
- detect conflicting instructions and stale context;
- distinguish intended action from inferred action;
- preserve rollback where possible;
- show owner-visible consequences before execution.

## AI-error controls
- do not treat confidence as correctness;
- require evidence for material claims;
- separate generator from evaluator;
- reject unsupported completion claims;
- require exact object/version/branch identifiers for changes;
- compare expected versus actual outputs;
- fail closed on malformed or ambiguous data;
- preserve dissent and contradictory evidence;
- prevent self-approval and self-deployment.

## Error barrier states
PASS, WARN, BLOCK, ESCALATE.

Critical permission, privacy, security, evidence, or rollback failures => BLOCK or ESCALATE.

## Recovery loop
detect -> contain -> preserve evidence -> diagnose -> repair -> verify -> add regression test -> update Prompt #11 lesson -> owner review

## Acceptance criteria
1. deterministic error-prevention checker exists;
2. critical errors block progression;
3. warnings remain owner-visible;
4. irreversible actions require explicit confirmation metadata;
5. post-action verification is required for claimed completion;
6. failures create regression requirements;
7. no automatic production activation.
