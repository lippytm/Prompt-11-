# P-011-OMNI-001 — Offline, Synchronization, Conflict and Recovery Procedure

## 1. Purpose

This procedure prevents loss, duplication, silent overwrites, false synchronization claims, and unsafe publication when Prompt #11 work moves among iPhone, iPad, ASUS laptop, Zo, ChatGPT, Gemini/NotebookLM, Claude/Fabric Hermes, GitHub, Slack, and other approved systems.

## 2. Core rules

1. An unsynchronized local copy is not the canonical copy.
2. A green checkmark or visible file name is not sufficient evidence of a tested backup.
3. Never delete the last known copy before verifying the authoritative copy opens and contains the expected version.
4. Never silently overwrite an approved artifact.
5. Never resolve a factual, rights, privacy, or identity conflict by selecting the newest timestamp alone.
6. When uncertain, quarantine rather than publish.
7. Record every material reconciliation in a Continuation Packet, issue, pull request, or correction record.

## 3. Offline work packet

Before intentional offline work, record:

- packet ID;
- parent Continuation Packet;
- device;
- human owner;
- artifact and version;
- privacy class;
- branch or local working-copy identifier;
- expected start and reconciliation time;
- acceptance criteria;
- files expected to change;
- prohibited actions;
- backup location;
- next authorized synchronization destination.

Use status `offline_queued` until reconciliation is complete.

## 4. Local filename convention

For temporary offline copies use:

`<ARTIFACT-ID>__<VERSION>__<DEVICE>__<YYYYMMDD-HHMM>__OFFLINE-WORKING.<ext>`

Example:

`P011-LESSON-001__v0.2__IPAD__20260822-1130__OFFLINE-WORKING.md`

Do not label a file `FINAL` unless it has passed the applicable gates and HumanApprovalGate.

## 5. Reconciliation sequence

1. **Stop editing.** Close or pause all other copies.
2. **Identify versions.** Record file name, size, modification time, content hash where available, branch, commit, device, and owner.
3. **Identify authority.** Determine the newest approved artifact and current issue or pull request.
4. **Create backups.** Preserve each conflicting version before merging.
5. **Classify the conflict.** Use the categories below.
6. **Compare.** Review differences line by line, field by field, or record by record.
7. **Merge deliberately.** Create a new version; do not overwrite either source copy.
8. **Test.** Run format, schema, code, accessibility, security, source, rights, and functional checks as applicable.
9. **Review.** Obtain the required human or specialist review.
10. **Record.** Commit, open or update the pull request, update the issue, and create a successor Continuation Packet.
11. **Supersede.** Mark old working copies as superseded or archived.
12. **Clean up safely.** Delete temporary duplicates only after verifying the authoritative version and backup.

## 6. Conflict categories

### Type 1 — Text or formatting conflict

Examples:

- two edits to the same chapter;
- different headings or layout;
- conflicting captions or descriptions.

Resolution:

- merge content intentionally;
- preserve meaning, truth labels, disclosures, accessibility, and rights;
- create a new version with reviewer record.

### Type 2 — Code or configuration conflict

Examples:

- different branches change the same function;
- environment or schema differences;
- incompatible dependency updates.

Resolution:

- use Git branch and pull-request workflow;
- run automated and manual tests;
- do not resolve by accepting all changes without review;
- preserve rollback capability.

### Type 3 — Data or ledger conflict

Examples:

- two devices update the same product status;
- duplicate source or learner records;
- conflicting quality scores or revenue figures.

Resolution:

- preserve both records;
- identify source system and timestamp;
- use transaction or audit IDs;
- reconcile based on evidence and authority;
- never average contradictory facts without justification.

### Type 4 — Source or factual conflict

Examples:

- two sources disagree;
- a current fact changed after an earlier packet;
- one AI model reports a conclusion unsupported by the source.

Resolution:

- create contradiction records;
- verify dates and primary sources;
- preserve uncertainty;
- do not force a single conclusion before evidence supports it.

### Type 5 — Privacy or identity conflict

Examples:

- a public version contains confidential details;
- a fictional character is confused with the creator;
- an AI clone uses unauthorized voice or likeness.

Resolution:

- stop distribution;
- quarantine affected copies;
- remove unauthorized access;
- preserve incident evidence privately;
- rotate credentials or revoke clone permissions where needed;
- issue corrections or takedowns.

### Type 6 — Rights or license conflict

Examples:

- third-party text, music, image, character, data, or code lacks permission;
- incompatible open-source licenses;
- unclear commercial rights.

Resolution:

- stop publication or distribution;
- replace, remove, license, or obtain qualified review;
- record RightsGate status.

### Type 7 — Approval conflict

Examples:

- Slack discussion suggests approval but the canonical record does not;
- an AI agent marks HumanApprovalGate passed;
- one version was approved for internal use but another is publicly released.

Resolution:

- the canonical human approval record controls only the stated artifact, version, scope, and conditions;
- anything beyond that scope remains unapproved.

## 7. Synchronization states

Use only these terms:

- **local-only:** exists on one device and is not backed up;
- **queued:** prepared for synchronization but not confirmed;
- **uploaded:** transmitted to a destination but not verified;
- **verified:** destination copy opens and matches expected version or hash;
- **canonical:** designated authoritative through the approved workflow;
- **replicated:** verified in an additional approved backup or system;
- **conflicted:** two or more versions require reconciliation;
- **quarantined:** removed from active use because of safety, privacy, rights, truth, or integrity concerns;
- **superseded:** replaced by a newer version but retained;
- **retired:** intentionally removed from active use and archived.

Do not say “synchronized” unless the relevant copies were verified.

## 8. Lost device procedure

1. Use available account controls to lock, locate, or erase the device where appropriate.
2. Revoke active sessions and tokens.
3. Rotate credentials that may have been exposed.
4. Suspend affected connectors, agents, clones, wallets, and deployment keys.
5. Record the incident privately.
6. Identify exposed data classes and affected accounts.
7. Notify required people or institutions through authorized channels.
8. Restore from a verified backup to a secured replacement device.
9. Review the current Continuation Packet and identify unsynchronized work.
10. Reconstruct only from authoritative artifacts; do not invent missing changes.

## 9. Lost chat or platform access procedure

If a chat, notebook, Slack workspace, Zo runtime, or AI account becomes unavailable:

1. Do not assume the content was deleted or compromised without evidence.
2. Check `continuation/CURRENT.md`.
3. Check GitHub issues, pull requests, files, releases, and archived packets.
4. Check approved exports or backups.
5. Identify the last known authoritative artifact.
6. Record missing context and uncertainty.
7. Create a recovery work packet.
8. Resume only from verified state.

## 10. Corrupted or unreadable file procedure

1. Preserve the corrupted original.
2. Record file path, size, timestamp, application, error, and device.
3. Attempt recovery from a copy, version history, repository, backup, or export.
4. Do not repeatedly overwrite the original during recovery attempts.
5. Verify recovered content against sources, tests, hashes, or prior versions.
6. Record what may be missing or altered.
7. Create a correction or incident record.

## 11. Backup requirements

Critical Prompt #11 artifacts should have:

- one authoritative working copy;
- one version-controlled history when the format permits;
- one separate approved backup;
- documented restore instructions;
- at least one tested restore;
- privacy controls matching the most sensitive included data.

A public GitHub repository is not a backup for confidential or restricted information.

## 12. Release hold conditions

Stop release when:

- the authoritative version cannot be identified;
- unresolved conflicts affect meaning, code, sources, privacy, identity, rights, safety, accessibility, environment, price, or approval;
- a backup or restore failure threatens irreversible loss;
- a platform account or device may be compromised;
- HumanApprovalGate is absent or out of scope;
- a Red RiskGate or failed critical gate exists.

## 13. Minimum reconciliation record

Record:

- conflict ID;
- affected artifacts and versions;
- devices or platforms;
- privacy class;
- conflict category;
- preserved copies;
- comparison method;
- resolution decision and rationale;
- tests performed;
- reviewer and approver;
- new canonical version;
- correction or notification required;
- superseded and archived versions;
- updated Continuation Packet.
