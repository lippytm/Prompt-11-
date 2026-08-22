# P-011-OMNI-001 — Mobile, Device and Platform Session Checklists

**Purpose:** Preserve continuity, security, privacy, provenance, and Quality and Quality Assurance while Prompt #11 moves among devices and platforms.

## 1. Universal start-of-session checklist

- [ ] Open `continuation/CURRENT.md`.
- [ ] Open the packet referenced by `CURRENT.md`.
- [ ] Confirm repository, branch, issue, pull request, artifact, privacy class, model line, RiskGate, and next action.
- [ ] Check whether the packet is approved, review-ready, superseded, quarantined, or retired.
- [ ] Confirm that no newer approved packet exists.
- [ ] Confirm that the current device and platform are authorized for the packet’s privacy class.
- [ ] Confirm that the account and workspace are the intended personal, business, model-line, or public identity.
- [ ] Check for unresolved edit conflicts, incidents, corrections, or failed critical gates.
- [ ] State the session objective and definition of done.
- [ ] Work only on the highest-priority unblocked action unless a P0 safety or continuity issue requires interruption.

## 2. Universal end-of-session checklist

- [ ] Record what was completed, partially completed, blocked, or not started.
- [ ] Record decisions and rationale.
- [ ] Record all artifacts, versions, paths, commits, pull requests, issues, notebooks, jobs, or authoritative references.
- [ ] Record privacy class and model-line identity.
- [ ] Record sources, truth labels, contradictions, and date-verification needs.
- [ ] Record tests, defects, RiskGate, release gates, and required reviewers.
- [ ] Record the exact next actions in priority order.
- [ ] Write a self-contained resume prompt.
- [ ] Create a successor Continuation Packet when project state materially changed.
- [ ] Update `CURRENT.md` only when the successor becomes review-ready or approved.
- [ ] Confirm synchronization or safe queueing before deleting any local capture.
- [ ] Remove temporary sensitive copies from unauthorized locations.
- [ ] Sign out or lock the device when appropriate.

## 3. iPhone checklist

### Best uses

- voice dictation and idea capture;
- quick issue review;
- photographs of non-sensitive project materials;
- short approvals or corrections;
- checking `CURRENT.md` and next actions;
- emergency incident reporting.

### Start

- [ ] Confirm the correct ChatGPT, GitHub, Slack, email, cloud, or browser identity.
- [ ] Confirm screen lock and current operating-system updates.
- [ ] Avoid public networks for confidential work unless an approved secure connection is used.
- [ ] Use the smallest necessary data excerpt.
- [ ] Open the current packet before adding new work.

### Capture format

Record:

1. **Observation or idea** — what was directly seen, heard, received, or imagined.
2. **Interpretation** — what it may mean.
3. **Truth label** — fact, official assessment, testimony, allegation, hypothesis, fiction, or contradicted.
4. **Privacy class** — public, internal, confidential, or restricted.
5. **Requested outcome** — research, story, lesson, code, business experiment, issue, or correction.
6. **Next routing destination** — Prompt #11 issue, private vault, model-line packet, or archive.

### Do not place in general notes, chat, or Slack

- passwords, private keys, recovery codes, full government identifiers;
- unredacted medical, banking, tax, legal, identity-theft, or witness records;
- confidential allegations naming identifiable people without authorized handling;
- API credentials or repository secrets;
- raw evidence that belongs in a private vault.

### End

- [ ] Convert important capture into a structured issue, artifact, or Continuation Packet.
- [ ] Confirm upload or safe queueing.
- [ ] Record whether the capture remains only on the phone.
- [ ] Delete duplicate temporary copies only after verifying the authoritative copy.

## 4. iPad checklist

### Best uses

- reading and annotation;
- storyboards, visual structure, presentation and video review;
- accessibility and touch-interface review;
- comparison of model-line outputs;
- human approval review when the approver has authority.

### Start

- [ ] Open the authoritative artifact rather than an old download.
- [ ] Confirm version, branch, and approval status.
- [ ] Check for an existing edit lock or active branch.
- [ ] Use comment or review mode when direct editing could create conflicts.

### Review checklist

- [ ] Is the purpose clear on the first screen?
- [ ] Are headings, text size, spacing, contrast, touch targets, and navigation usable?
- [ ] Can a learner understand where to begin and what success looks like?
- [ ] Are fiction, evidence, uncertainty, limitations, and business assumptions visibly labeled?
- [ ] Are captions, transcripts, alt text, keyboard alternatives, and plain-language explanations required?
- [ ] Does the product remain usable without unnecessary animation, audio, or high bandwidth?
- [ ] Are corrections and version identifiers visible?

### End

- [ ] Save review findings to the canonical issue or review record.
- [ ] Do not leave the only copy of annotations in a local app.
- [ ] Record approved, conditional, rejected, or returned-for-correction status.

## 5. ASUS laptop checklist

### Best uses

- coding and tests;
- repository branches and pull requests;
- spreadsheet or database construction;
- media production;
- local builds and deployment preparation;
- backups and restore testing.

### Start

- [ ] Pull or fetch the newest approved repository state.
- [ ] Confirm branch and issue.
- [ ] Check uncommitted changes and edit conflicts.
- [ ] Confirm dependencies and runtime versions.
- [ ] Confirm secrets are loaded through approved environment mechanisms and not committed.
- [ ] Read acceptance criteria before coding.

### Build and test

- [ ] Use a feature branch.
- [ ] Make small, traceable commits.
- [ ] Add tests or documented review evidence.
- [ ] Run lint, schema, unit, integration, accessibility, security, and documentation checks as applicable.
- [ ] Record defects instead of hiding or deleting them.
- [ ] Do not represent mock routes, placeholder connectors, or architecture documents as deployed services.
- [ ] Confirm local and cloud backups.

### End

- [ ] Push the branch.
- [ ] Create or update the pull request.
- [ ] Link the issue and acceptance criteria.
- [ ] Record test results and limitations.
- [ ] Update the Continuation Packet.
- [ ] Lock, shut down, or secure the laptop appropriately.

## 6. Zo workspace checklist

### Best uses

- authorized cloud runtime;
- scheduled jobs;
- prototype deployment;
- data processing;
- hosted tools and dashboards.

### Before any deployment

- [ ] Confirm account ownership and authorization.
- [ ] Confirm pricing, credits, limits, data location, retention, and backup needs.
- [ ] Confirm secrets storage and least-privilege permissions.
- [ ] Confirm the repository commit to deploy.
- [ ] Confirm rollback and shutdown procedures.
- [ ] Confirm monitoring and cost alerts.

### Deployment status terms

Use only:

- **planned** — architecture or backlog only;
- **configured** — settings exist but function is not verified;
- **tested** — bounded test passed with evidence;
- **deployed** — approved version is running;
- **monitored** — health, cost, security, and error data are being reviewed;
- **retired** — service is intentionally stopped and archived.

Never call a service deployed merely because a README, manifest, environment variable, or mock endpoint exists.

## 7. ChatGPT Business checklist

- [ ] Read the current packet.
- [ ] Identify whether the work is orchestration, research, drafting, QA, coding, or continuation.
- [ ] Preserve the ChatGPT model-line identifier.
- [ ] Do not claim access to another platform unless a connector call succeeds.
- [ ] Use authoritative sources for current or high-stakes facts.
- [ ] Do not treat generated text as verified evidence.
- [ ] Create structured artifacts, issues, or packets rather than leaving material only in chat.
- [ ] Human approval remains external to model confidence.

## 8. Gemini and NotebookLM checklist

- [ ] Create or identify the independent Gemini/NotebookLM work packet.
- [ ] Record notebook or source-collection identifier.
- [ ] Maintain a source manifest.
- [ ] Distinguish source-grounded statements from Gemini-generated analysis.
- [ ] Do not copy ChatGPT or Claude conclusions into the independent first pass.
- [ ] Record source gaps, contradictions, and unanswered questions.
- [ ] Treat audio overviews as derivative learning media requiring fact, rights, and accessibility review.
- [ ] Export or reference approved results in the Continuation Packet.

## 9. Claude and Fabric Hermes checklist

- [ ] Create or identify the independent Claude/Hermes work packet.
- [ ] Define bounded scope, tools, permitted data classes, and output schema.
- [ ] Use Hermes for routing, provenance, audit, contradiction analysis, and QA—not autonomous truth, diagnosis, liability, contract, financial, or publication decisions.
- [ ] Preserve source and model-line independence.
- [ ] Record work-packet dispatches and returns.
- [ ] Require human approval for external action.

## 10. GitHub checklist

- [ ] Use issues for work definitions and acceptance criteria.
- [ ] Use branches for implementation.
- [ ] Use commits for traceable changes.
- [ ] Use pull requests for review and merge evidence.
- [ ] Use releases or tags for approved versions.
- [ ] Use schemas and manifests for machine-readable contracts.
- [ ] Use correction and retirement records rather than deleting history.
- [ ] Never commit secrets or restricted evidence.
- [ ] Distinguish public and private repositories.
- [ ] Confirm mergeability and review status before merging.

## 11. Slack checklist

### Appropriate uses

- handoff notifications;
- review requests;
- alerts;
- discussion;
- links to authoritative issues, pull requests, packets, decisions, incidents, or corrections.

### Rules

- [ ] Link to the canonical artifact.
- [ ] Include packet ID, issue, owner, privacy class, requested action, and due condition.
- [ ] Do not paste restricted evidence into a broad channel.
- [ ] Record decisions back in the canonical issue or decision record.
- [ ] Do not treat an emoji, informal reaction, or model-generated Slack message as HumanApprovalGate.
- [ ] Propagate corrections to affected Slack messages or threads when necessary.

## 12. Human approval checklist

Before approving publication, minting, financial action, identity cloning, voice or likeness use, medical or legal conclusions, named allegations, product certification, or franchise certification:

- [ ] Confirm identity and authority of the approver.
- [ ] Confirm exact artifact, version, scope, and privacy class.
- [ ] Review critical gates and Red RiskGate.
- [ ] Review unresolved defects, contradictions, rights, accessibility, environmental effects, support obligations, and correction plan.
- [ ] Record conditions and expiration where appropriate.
- [ ] Record the approval in an auditable canonical system.

An AI recommendation may inform the decision but cannot be the human approval.
