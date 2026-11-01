# P-011-PEE-001 — Prompt Engineering & Evolution Engine

## 1. Mission

P-011-PEE-001 turns Prompt #11 into a versioned prompt-engineering control system for AI Building Better AI, AI Jarvis Assistants Swarms Systems Communications Networks, GitHub Copilot, and downstream repositories.

It supplements P-011-XPIO-001. It does not replace owner authority, existing privacy controls, release gates, or the rule: **No human approval, no release.**

## 2. Core operating loop

`objective -> context selection -> prompt candidate -> agent execution -> deterministic checks -> evidence review -> red-team critique -> rubric evaluation -> capability-gap analysis -> revised candidate -> regression test -> owner review -> promotion or rejection`

A prompt is not improved merely because a model says it is improved. Promotion requires recorded evidence and the required gates.

## 3. Prompt engineering layers

1. Mission — exact outcome and acceptance criteria.
2. Authority — permitted actions, prohibited actions, and owner approval boundaries.
3. Context — minimum necessary project/repository context.
4. Role — named Jarvis/Copilot/agent responsibility.
5. Planning — bounded tasks and dependencies.
6. Execution — tools, code, research, documentation, and actions.
7. Evidence — sources, artifacts, commits, tests, hashes, and defects.
8. Evaluation — rubric-based scoring against acceptance criteria.
9. Red Team — independent failure search and counterexamples.
10. Evolution — proposed prompt/tool/workflow changes based on evidence.
11. Promotion & Continuity — regression checks, owner approval, versioning, and Continuation Packet update.

## 4. Jarvis prompt-engineering roles

- Prompt Architect — drafts or refactors candidate prompts.
- Context Engineer — selects only necessary context.
- Copilot Engineer — translates requirements into repository coding instructions.
- Test Engineer — defines deterministic acceptance and regression checks.
- Evidence Officer — records proof and unresolved gaps.
- Red Team — seeks contradictions, unsafe behavior, prompt injection, regressions, and unsupported assumptions.
- Evaluator — scores against the declared rubric; does not promote its own work.
- Evolution Engineer — proposes bounded mutations after failed or weak evaluations.
- Hermes Dispatcher — routes work packets among authorized agents/tools.
- MemPalace Librarian — stores approved reusable prompt modules and provenance.
- Release Manager — prepares promotion evidence; HumanApprovalGate remains external to AI.

The producer and final evaluator should be separated where practical.

## 5. Quantum Questions integration

Every material prompt evolution must record:

- **IF** — what hypothesis or outcome is being tested?
- **Maybe** — what uncertainties or alternative explanations remain?
- **Why Not** — what alternative design could outperform the current candidate?
- **Don't Do That** — what known failure, unsafe action, or prohibited behavior must be blocked?
- **I Told You Not To Do That!** — after failure, what warning was ignored, what evidence proves the failure, what recovery is required, and what new regression guardrail prevents recurrence?

A repeated failure should create or strengthen a regression test before another promotion attempt.

## 6. Prompt candidate lifecycle

States:

`draft -> testable -> evaluated -> review_ready -> approved -> superseded|rejected|quarantined`

AI agents may create candidates and evidence, but may not set `approved`.

Semantic versions are required for approved reusable prompts:

- PATCH — wording/clarity change with unchanged behavior target.
- MINOR — backward-compatible capability or module addition.
- MAJOR — changed authority, contract, inputs/outputs, or behavior assumptions.

## 7. Prompt viability score

Default 100-point rubric:

- instruction clarity: 15
- context quality: 15
- task decomposition: 10
- tool selection: 10
- evidence/provenance: 15
- testing/regression coverage: 15
- safety/governance: 10
- efficiency: 5
- reusability: 5

Interpretation:

- 90-100: production candidate, still requires required gates and human approval
- 80-89: experimental/review-ready
- 70-79: revise
- below 70: reject or redesign

A score never overrides a failed critical gate.

## 8. GitHub/Copilot workflow

`issue/work packet -> candidate branch -> prompt/module change -> tests/evals -> evidence packet -> red-team review -> PR -> owner review -> merge -> approved version record -> downstream consumption`

Downstream repositories should consume approved prompt modules by identifier/version and should not silently fork Prompt #11 policy.

Initial consumers:

1. `lippytm/jarvis-nexus-core`
2. `lippytm/AI-Jarvis-Assistant-AI-Copilot-for-Self-Healing-and-Self-Improvements-for-all-Repositories-`
3. other authorized Jarvis/Copilot repositories after the first integration is validated.

## 9. Minimal acceptance criteria for P11-PEE-001 v0.1

P11-PEE-001 is review-ready when:

1. a canonical architecture document exists;
2. a machine-readable prompt-candidate schema exists;
3. a current Continuation Packet records the exact next action;
4. no existing Prompt #11 authority or privacy boundary is weakened;
5. prompt promotion requires evidence, regression checks, and HumanApprovalGate;
6. the first downstream integration target is `jarvis-nexus-core`;
7. no claim of deployment or cross-repository synchronization is made without verification.

## 10. Current bounded next task

Inspect `jarvis-nexus-core` for its existing agent/prompt/instruction entrypoints, then propose the smallest adapter that reads or references an approved Prompt #11 module without changing production behavior. Implementation remains on a branch until tests and owner review are complete.
