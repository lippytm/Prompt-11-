# P-011-PEE-002 — Jarvis Prompt Composition, Evaluation & Regression Framework

## 1. Purpose

P-011-PEE-002 extends P-011-PEE-001 from prompt governance into deterministic prompt composition for AI Jarvis Assistants, GitHub Copilot workflows, and downstream agent systems.

The design objective is **more capable AI with less prompt drift**.

P11-PEE-002 does not authorize production activation. It creates a testable composition contract and evaluation workflow.

## 2. Composition model

A composed Jarvis instruction package is built from ordered modules:

1. governance core;
2. role/persona constraints;
3. domain module;
4. task module;
5. tool-use module;
6. evidence and QA module;
7. red-team safeguards;
8. output contract;
9. continuation/resume contract.

Only modules with valid identifiers, versions, provenance, and required approval state may be selected.

## 3. Composition invariants

A composer must:

- preserve module order explicitly;
- preserve module identifiers and versions;
- reject duplicate module identifiers unless an override policy explicitly allows replacement;
- reject conflicting authority declarations;
- keep user/task input separate from system/governance content;
- label each module boundary;
- emit a composition manifest;
- never silently mutate source modules;
- never infer approval from branch, filename, model output, or repository ownership;
- never activate a composed prompt merely because composition succeeds.

## 4. Prompt package

Each composed package should contain:

- composition ID;
- timestamp;
- task class;
- target agent role;
- module list and versions;
- source repository/path/ref for each module;
- approval audit references;
- deterministic composition order;
- composed system text;
- expected inputs;
- output contract;
- acceptance criteria;
- evaluation rubric ID;
- regression-suite ID;
- unresolved conflicts;
- activation state.

Default activation state is `inactive`.

## 5. Evaluation dimensions

Every candidate composition is scored across:

- instruction consistency;
- authority consistency;
- context sufficiency;
- context minimization;
- tool eligibility;
- provenance completeness;
- safety boundary preservation;
- output-schema compliance;
- deterministic test pass rate;
- regression pass rate;
- latency/cost budget where measured;
- portability across approved model lines;
- recoverability and rollback clarity.

No single aggregate score overrides a failed critical gate.

## 6. Red-team suite

At minimum test:

- prompt injection in user/task input;
- attempts to override HumanApprovalGate;
- malformed or missing module metadata;
- duplicate modules;
- conflicting instructions;
- stale/superseded module versions;
- tool requests outside allowlist;
- hidden deployment assumptions;
- fabricated evidence;
- secret or restricted-data leakage requests;
- self-promotion of a candidate prompt;
- model claims of approval without audit evidence.

## 7. AI-building-AI improvement loop

`compose -> execute in sandbox -> measure -> critique -> compare -> diagnose gap -> propose mutation -> rerun -> regression -> owner review`

Mutations are proposals, not self-deploying changes.

## 8. Best-practice rules

1. Prefer smaller composable modules over monolithic prompts.
2. Put stable governance before volatile task instructions.
3. Use explicit data schemas for machine-consumed outputs.
4. Separate generation from evaluation.
5. Keep evaluation rubrics versioned.
6. Record negative tests, not only happy-path tests.
7. Treat prompt changes like code changes: branch, diff, test, review, rollback.
8. Minimize context to what is necessary for the task.
9. Make uncertainty and unresolved gaps first-class output fields.
10. Prefer deterministic preprocessing/postprocessing over asking a model to remember format rules.
11. Require evidence for claims of better quality, lower cost, faster execution, or higher reliability.
12. Maintain cross-model comparison without assuming one model validates another.
13. Log failures as regression cases.
14. Keep production activation as a distinct, explicit step.
15. End every meaningful evolution cycle with a Continuation Packet.

## 9. Initial implementation target

Implement a reference-only composer inside `jarvis-nexus-core` that:

- accepts already-validated Prompt #11 module descriptors;
- deterministically orders them;
- rejects duplicates;
- emits a frozen composition manifest;
- does not fetch prompt text;
- does not call a model;
- does not alter Jarvis-Hub or Jarvis-Flow runtime paths;
- remains inactive by default.

## 10. Acceptance criteria

P11-PEE-002 v0.1 is review-ready when:

1. composition rules are documented;
2. deterministic composer code exists;
3. duplicate/conflict rejection is tested;
4. composition output is immutable;
5. no network/model call occurs;
6. no runtime integration occurs;
7. provenance is retained for every module;
8. test evidence and hashes are recorded;
9. unresolved limitations are explicit;
10. HumanApprovalGate remains external to AI.
