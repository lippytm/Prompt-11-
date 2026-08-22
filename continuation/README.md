# Prompt #11 Continuation Directory

This directory contains the portable project checkpoints used to resume Prompt #11 across devices, platforms, people, and AI model lines.

## Authoritative pointer

Open [`CURRENT.md`](CURRENT.md) first.

`CURRENT.md` identifies:

- the newest review-ready or human-approved Continuation Packet;
- its status and privacy class;
- the current module and workstream;
- the highest-priority unblocked action;
- authoritative repositories, branches, pull requests, issues, and artifacts;
- critical blockers and quality state;
- the exact resume command.

## Packet naming

Use:

`P011-CP-<PROGRAM>-<YYYY-MM-DD>-v<MAJOR>.<MINOR>.json`

Example:

`P011-CP-OMNI-2026-08-22-v0.4.json`

## Status meanings

- **draft:** incomplete and not safe to rely on;
- **under_review:** structurally usable but awaiting human review or approval;
- **approved:** accepted by an identified human approver for the stated scope;
- **superseded:** replaced by a newer packet but retained for provenance;
- **quarantined:** unsafe, conflicting, incomplete, or under incident review;
- **retired:** intentionally removed from active use while preserved in the archive.

## Operating rules

1. Begin every meaningful session by reading `CURRENT.md` and the referenced packet.
2. Confirm that referenced branches, files, issues, and approvals still exist.
3. Never invent missing work, synchronization, deployments, or approvals.
4. Create a successor packet before changing devices, platforms, workstreams, model lines, or responsible humans.
5. Never silently overwrite an approved packet.
6. Store only public or appropriately redacted internal information here. Restricted personal, medical, identity, witness, financial, credential, or security evidence belongs in an approved private vault.
7. Record model-line identity. ChatGPT, Gemini/NotebookLM, and Claude/Hermes first-pass work remains independent.
8. Slack, chat history, and local notes may support collaboration but do not replace the canonical packet, issue, pull request, decision record, or approval.
9. If two packets conflict, quarantine both affected claims or artifacts until ConflictResolutionGate is completed.
10. HumanApprovalGate can be passed only by an identified human with authority for the stated scope.

## Resume hierarchy

When the newest packet cannot be accessed, reconstruct in this order:

1. `continuation/CURRENT.md`;
2. newest approved packet;
3. newest review-ready packet;
4. open GitHub issues and pull requests;
5. merged module documents and manifests;
6. archived packets and correction records;
7. chats or Slack only as secondary context.

Any uncertainty must be recorded rather than filled with invented progress.
