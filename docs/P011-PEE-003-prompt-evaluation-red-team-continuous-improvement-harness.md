# P-011-PEE-003 — Prompt Evaluation, Red-Team & Continuous Improvement Harness

## 1. Purpose

P-011-PEE-003 defines the evaluation layer that decides whether a Prompt #11 composition is better, worse, or unchanged based on evidence rather than preference.

It evaluates candidate prompt packages before production activation.

## 2. Evaluation classes

### Deterministic checks
- schema validity;
- required module presence;
- duplicate/conflict detection;
- provenance completeness;
- approval evidence completeness;
- tool allowlist compliance;
- output contract conformance;
- regression-suite status;
- activation-state correctness.

### Adversarial checks
- prompt injection;
- instruction hierarchy confusion;
- attempts to bypass HumanApprovalGate;
- malicious tool request insertion;
- fabricated evidence;
- unsupported completion claims;
- secret/credential exfiltration requests;
- stale or superseded module references;
- contradictory module instructions;
- self-approval/self-promotion attempts.

### Model-quality checks
Only after deterministic gates pass:
- task success;
- factuality/evidence use;
- instruction adherence;
- completeness;
- concision/efficiency;
- uncertainty calibration;
- code/test quality where applicable;
- cross-model consistency and disagreement;
- cost/latency where measured.

Model-quality scores never override failed deterministic or governance gates.

## 3. Gold-set strategy

Maintain versioned test suites for:

- software engineering;
- GitHub diagnostics;
- prompt engineering;
- business analysis;
- research synthesis;
- educational/RPG lesson generation;
- newsletter/briefing generation;
- trading-sandbox research prompts;
- Hostinger/web workflow prompts;
- creative publishing prompts.

Each test case stores:
- task ID;
- fixed input fixture;
- expected structural properties;
- prohibited behaviors;
- required evidence;
- rubric;
- known failure cases;
- prior approved baseline.

## 4. Comparison design

Compare:
- baseline approved prompt;
- candidate prompt;
- optional ablation variants.

Use blinded or identifier-neutral evaluation where practical.

Track:
- pass/fail by critical gate;
- rubric score;
- regression count;
- new failure count;
- resolved failure count;
- token/input size;
- output size;
- latency;
- estimated cost where measured;
- evaluator disagreement.

Never claim improvement from a single cherry-picked example.

## 5. Promotion rule

A candidate may advance to owner review only when:
1. all critical deterministic gates pass;
2. no unresolved high-severity regression exists;
3. evidence is complete;
4. red-team suite is complete for the declared risk class;
5. comparison shows no material degradation on required baselines;
6. unresolved model disagreement is disclosed;
7. rollback path is documented.

Only the authorized human owner may pass HumanApprovalGate.

## 6. Continuous improvement record

Every failed case should create:
- failure ID;
- affected prompt/module/version;
- observed behavior;
- expected behavior;
- evidence;
- severity;
- root-cause hypothesis;
- proposed mutation;
- regression test;
- disposition.

This creates a Prompt #11 failure-memory system without allowing autonomous self-deployment.

## 7. Suggested engineering backlog

### Priority A — governance and correctness
- prompt candidate schema tests in CI;
- composition manifest schema;
- conflict taxonomy;
- stale/superseded-version checks;
- approval-reference verification contract;
- deterministic red-team fixtures.

### Priority B — quality measurement
- baseline prompt corpus;
- software-engineering eval set;
- research/evidence eval set;
- business-output eval set;
- education/RPG eval set;
- daily-briefing eval set.

### Priority C — efficiency
- context-budget accounting;
- module relevance selection;
- prompt deduplication;
- cacheable static governance modules;
- token-cost telemetry;
- latency telemetry.

### Priority D — multi-model evaluation
- independent ChatGPT, Claude, and Gemini runs;
- disagreement register;
- evaluator rotation;
- model-specific failure profiles;
- no circular self-validation.

### Priority E — controlled activation
- opt-in feature flag;
- shadow mode;
- canary task class;
- rollback switch;
- audit logging;
- owner-visible release checklist.

## 8. Best-practice principle

Prompt #11 should evolve like a safety-critical software system:
**specify -> version -> test -> attack -> measure -> review -> approve -> monitor -> rollback when needed.**
