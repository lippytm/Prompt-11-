# P-011-XPIO-001 Diagnostics, Debugging and Observability Manual

## Diagnostic categories

| Category | Examples | Release effect |
|---|---|---|
| Integrity | file hash, database integrity, schema validity | mismatch may block |
| Identity | passport, owner, disclosure, memory provenance | critical failure blocks |
| Privacy | data class and destination compatibility | critical failure blocks |
| Security | permissions, secrets, dependency and configuration state | critical failure blocks |
| Model independence | copied output, shared source dependence | warning or block for comparison claims |
| Quality | tests, defects, risk, gate status | critical failure blocks |
| Documentation | missing runbook, ADR, data dictionary, QEP | may block Q3/Q4 |
| Operations | stale checkpoint, queue age, backup evidence | warning or block |
| Revenue | price, cost, refund, affiliate and approval records | block financial action |
| Correction | affected editions and channels updated | block continued sale when material |

## Error taxonomy

- `XPIO-INPUT-001` malformed work packet
- `XPIO-ID-001` duplicate or invalid stable ID
- `XPIO-HASH-001` artifact hash mismatch
- `XPIO-PRIV-001` privacy route violation
- `XPIO-PERM-001` connector permission unknown or excessive
- `XPIO-MODEL-001` model-line independence failure
- `XPIO-DB-001` database integrity or migration failure
- `XPIO-DOC-001` required documentation missing
- `XPIO-GATE-001` critical gate failure
- `XPIO-AUTH-001` invalid human approval
- `XPIO-FIN-001` unauthorized financial action
- `XPIO-CORR-001` correction propagation incomplete

## Reproduction packet

Every debugging packet includes:

- defect or incident ID;
- correlation ID;
- smallest safe input fixture;
- exact command or operation;
- expected output;
- actual output;
- environment and versions;
- redacted logs;
- evidence and screenshots when useful;
- suspected and alternative causes;
- rollback or containment;
- regression test path.

## Observability signals

- event count by severity and platform;
- failed diagnostics by category;
- artifact verification percentage;
- stale work packets;
- open critical defects;
- failed gates;
- unapproved release attempts;
- connector permission age;
- model-line independence findings;
- backup and restore age;
- correction propagation percentage;
- cost and budget variance.

## Debugging sequence

1. Contain unsafe effects.
2. Preserve original evidence and logs.
3. Assign IDs and correlation.
4. Reproduce with the smallest safe fixture.
5. Compare expected and actual behavior.
6. Test alternative hypotheses.
7. Implement the smallest fix.
8. Add regression tests.
9. Review privacy, security, rights, and downstream effects.
10. Obtain required approval.
11. Deploy through a reversible release.
12. Monitor and close only with evidence.
