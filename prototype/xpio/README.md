# XPIO Q2 Control Plane Prototype

This standard-library Python prototype registers Prompt #11 download artifacts, platforms, clone identities, work packets, documents, transparency events, diagnostics, decisions, and defects in SQLite.

## Bootstrap

```bash
python xpio_control_plane.py bootstrap \
  --db ../reports/P011_XPIO_Control_Plane_Q2.sqlite \
  --manifest ../manifests/P011_ARTIFACT_VAULT_001.manifest.json \
  --identity ../manifests/P011-XPIO-001.sample-identity-passport.json \
  --work-packet ../manifests/P011-XPIO-001.sample-work-packet.json \
  --document canonical_architecture=../docs/P011-XPIO-001-canonical-architecture.md \
  --document diagnostics_manual=../docs/P011-XPIO-001-diagnostics-debugging-observability.md \
  --document database_transparency=../docs/P011-XPIO-001-documentation-database-transparency.md \
  --document identity_strategy=../docs/P011-XPIO-001-clone-identity-strategy.md \
  --document artifact_vault=../docs/P011-XPIO-001-artifact-vault-integration.md \
  --json-report ../reports/P011_XPIO_Q2_REPORT.json \
  --markdown-report ../reports/P011_XPIO_Q2_REPORT.md
```

## Backup and restore test

```bash
python xpio_control_plane.py backup-test \
  --db ../reports/P011_XPIO_Control_Plane_Q2.sqlite \
  --backup ../reports/P011_XPIO_Control_Plane_Q2.backup.sqlite \
  --report ../reports/P011_XPIO_BACKUP_RESTORE_REPORT.json
```

## Tests

```bash
python -m unittest -v test_xpio_control_plane.py
```

## Boundaries

The prototype is offline and does not connect to external AI platforms, hold secrets, execute payments, impersonate a person, deploy mutations, or approve Q3/Q4.
