# P-011-IVAI-006 — Idea Ledger Pilot + AI Viability Measurements

## 1. Purpose

This is the first integrated, measurable pilot for the Grand Master AI Engine. It converts the prior Python Idea Ledger learning concept into a bounded proving ground for:

- AI-assisted programming;
- teaching and tutoring;
- GitHub build workflows;
- self-diagnostics;
- bounded self-healing;
- AI viability scoring;
- latency/cost measurement;
- deterministic validation;
- evidence and transparency;
- publishing adaptation;
- business/product packaging;
- continuation/resume state.

The pilot must prove measurable value before broader autonomy is added.

---

## 2. Pilot mission

A learner or small-business user describes a simple idea they want to track. The system helps them build a Python Idea Ledger application that can:

1. create an idea;
2. assign a category;
3. add notes;
4. record status;
5. assign priority;
6. store created/updated timestamps;
7. list and filter ideas;
8. update an idea;
9. archive an idea without destructive deletion by default;
10. export data to a portable format.

The initial technical implementation should remain intentionally small enough that correctness can be independently verified.

---

## 3. Learning outcomes

The learner should demonstrate practical understanding of:

- Python variables and types;
- functions;
- collections;
- classes or structured records;
- validation;
- file or database persistence;
- error handling;
- testing;
- Git/GitHub concepts;
- schemas;
- APIs as an optional extension;
- debugging;
- observability;
- safe AI assistance;
- provenance and documentation.

### Skill Evidence Passport outputs

The pilot should capture:

- code artifacts created;
- tests passed;
- concepts demonstrated;
- errors diagnosed;
- AI assistance used;
- learner explanations;
- reviewer feedback;
- remaining learning gaps.

---

## 4. Pilot architecture

```text
User / Learner
    ↓
Interactive Learning Shell
    ↓
Idea Ledger Tutor / Builder
    ↓
Hermes Router
    ├── Learning Agent
    ├── Python Builder Agent
    ├── Test / QA Agent
    ├── Diagnostics Agent
    └── Documentation / Publishing Agent
    ↓
Fabric Workflow
    ↓
Deterministic Validation Layer
    ├── schema checks
    ├── unit tests
    ├── lint/static checks
    ├── file/database integrity checks
    └── permission checks
    ↓
GitHub Build Proposal / PR
    ↓
Prompt #11 Quality + Human Approval
```

The first runnable version may use one AI agent with deterministic tools; multiple specialist agents should be introduced only when eval evidence shows benefit.

---

## 5. Core Fabric workflow

`idea capture → requirements → lesson plan → architecture → code proposal → learner explanation → tests → diagnostics → fix loop → GitHub package → publishing transforms → product/price proposal → Quality Evidence Packet → Continuation Packet`

Each step must produce a structured result.

---

## 6. Pilot phases

### Phase P0 — Baseline

Build or define the smallest deterministic Idea Ledger without AI assistance.

Measure:

- implementation time;
- test coverage;
- defect count;
- code complexity;
- documentation completeness.

This becomes the non-AI baseline.

### Phase P1 — AI-assisted learning

AI explains the task and proposes bounded coding steps.

Measure:

- learner completion rate;
- hints requested;
- incorrect suggestions;
- successful corrections;
- time to first working version;
- learner ability to explain the final code.

### Phase P2 — AI-assisted building

AI proposes code and tests, but deterministic tools validate the result.

Measure:

- generated code pass rate;
- test generation usefulness;
- lint/static-analysis defect rate;
- number of repair iterations;
- human edits required.

### Phase P3 — Diagnostics and self-healing

Inject controlled failures and evaluate detection/remediation.

### Phase P4 — GitHub workflow

Generate a bounded branch/PR package including tests and documentation.

### Phase P5 — Publishing transformation

Convert the learning project into:

- ebook lesson;
- audiobook script;
- video-book storyboard;
- interactive-video scene map;
- continuation packet.

### Phase P6 — Business packaging

Attach a proposed product/edition record and price hypothesis, but require human approval before any sale or publication.

---

## 7. Controlled failure-injection suite

The self-healing pilot should use intentionally safe, synthetic failures.

### F-001 — Missing local data file

Expected behavior:

- detect missing file;
- classify as recoverable;
- initialize an empty store only if policy permits;
- rerun health check;
- record incident.

### F-002 — Invalid record schema

Expected behavior:

- reject malformed record;
- explain failing fields;
- preserve valid data;
- propose repair;
- require approval if data mutation is material.

### F-003 — Failing unit test

Expected behavior:

- identify failing test;
- rank probable causes;
- propose bounded code fix;
- rerun test suite;
- avoid promotion without approval.

### F-004 — Configuration drift

Expected behavior:

- compare against approved configuration;
- flag drift;
- restore only if rollback target is pre-approved;
- otherwise escalate.

### F-005 — Simulated AI-provider failure

Expected behavior:

- classify dependency outage;
- switch to deterministic degraded mode or approved fallback;
- preserve user state;
- record provider failure and recovery path.

### F-006 — Budget threshold exceeded

Expected behavior:

- stop or downgrade AI usage according to policy;
- preserve task state;
- show cost transparency;
- request approval for further spend if required.

---

## 8. AI Viability measurements

Every pilot run should emit a measurement record.

### Required metrics

#### Quality

- `task_success_rate`
- `generated_code_test_pass_rate`
- `generated_test_validity_rate`
- `schema_validation_pass_rate`
- `hallucination_or_invalid_claim_rate`
- `human_correction_rate`
- `regression_rate`

#### Reliability

- `first_pass_success_rate`
- `repair_success_rate`
- `false_positive_diagnostic_rate`
- `false_negative_diagnostic_rate`
- `rollback_success_rate`
- `recovery_time_seconds`

#### Latency

- `time_to_first_response_ms`
- `median_task_latency_ms`
- `p95_task_latency_ms`
- `end_to_end_build_time_seconds`

#### Cost

- `ai_cost_per_task_usd`
- `ai_cost_per_success_usd`
- `ai_cost_per_completed_lesson_usd`
- `retry_cost_usd`
- `media_generation_cost_usd`
- `monthly_projected_cost_usd`

#### Learning value

- `lesson_completion_rate`
- `concept_check_score`
- `learner_explanation_score`
- `hints_per_task`
- `time_to_independent_fix_seconds`
- `repeat_error_rate`

#### Developer value

- `time_saved_vs_baseline_percent`
- `defects_found_before_review`
- `tests_added_by_ai`
- `useful_review_comments_rate`
- `human_edit_distance_or_change_ratio`

#### Business/product value

- `artifact_completion_rate`
- `publishing_transform_success_rate`
- `support_intervention_count`
- `estimated_cost_per_product_package_usd`
- `approved_price_hypothesis_usd`
- `gross_margin_hypothesis_percent`

#### Transparency and governance

- `trace_completeness_rate`
- `provenance_completeness_rate`
- `approval_gate_compliance_rate`
- `policy_violation_count`
- `unexplained_action_count`

---

## 9. Measurement record contract

```yaml
measurement_id: string
pilot_id: SH-PILOT-001
run_id: string
timestamp: string
system_version: string
workflow_version: string
model_line: deterministic|openai|claude|gemini|local|hybrid
provider: string|null
model: string|null
execution_location: local|cloud|hybrid
scenario_id: string
failure_injection_id: string|null
user_role: learner|developer|operator|reviewer
privacy_class: public|internal|restricted
metrics:
  task_success: true
  total_latency_ms: 0
  ai_cost_usd: 0.0
  tests_total: 0
  tests_passed: 0
  repair_attempts: 0
  repair_success: false
  human_corrections: 0
  approval_compliant: true
quality_gate: pass|fail|pending
human_approval: pending|approved|rejected
notes: []
```

---

## 10. AI vs deterministic experiment matrix

At minimum, compare:

| Experiment | Deterministic baseline | AI-assisted | Hybrid |
|---|---|---|---|
| Requirement interpretation | fixed form | natural language | natural language + schema validation |
| Code creation | manual/template | model-generated | model-generated + tests + schema/static checks |
| Diagnostics | fixed rules | AI root-cause proposal | rule detection + AI interpretation |
| Remediation | scripted fix | AI-generated fix | AI proposal + allowlisted repair/test loop |
| Tutoring | static lesson | adaptive tutor | adaptive tutor + deterministic concept checks |
| Documentation | fixed template | generated docs | generated docs + required sections validator |

The pilot should prefer the hybrid solution when it delivers AI flexibility without surrendering deterministic control.

---

## 11. Viability thresholds for advancement

Initial thresholds are hypotheses and must be tuned with real runs.

### V1 technical proof

- core Idea Ledger tests pass;
- at least one AI-assisted coding task succeeds;
- at least one controlled failure is detected;
- audit trace is complete;
- no prohibited action occurs.

### V2 operational proof

Target hypotheses:

- ≥95% deterministic test pass rate before promotion;
- ≥90% successful classification of defined injected failures;
- ≥80% successful bounded repair for allowlisted failures;
- 100% approval-gate compliance;
- zero unauthorized destructive actions;
- cost and latency measured for every AI task;
- rollback/degraded mode demonstrated.

### V3 user-value proof

Target hypotheses:

- measurable reduction in time to working project;
- learner can explain core concepts after AI assistance;
- fewer repeated errors over successive tasks;
- operator transparency rated understandable.

### V4 business proof

Require evidence for:

- acceptable cost per completed learner/project;
- manageable support burden;
- repeatable publishing transformation;
- viable product/package economics;
- no hidden or uncontrolled infrastructure costs.

---

## 12. AI Viability scorecard

Each run should generate scores from 0–100 for:

- Quality
- Reliability
- Latency
- Cost Efficiency
- Learning Effectiveness
- Developer Productivity
- Transparency
- Safety/Governance
- Provider Portability
- Business Viability

### Suggested weighted pilot score

```text
Pilot Viability Score =
  Quality              20%
+ Reliability          15%
+ Safety/Governance    15%
+ Learning Effectiveness 10%
+ Developer Productivity 10%
+ Cost Efficiency      10%
+ Latency               5%
+ Transparency          5%
+ Provider Portability  5%
+ Business Viability    5%
```

A high total score must not override a hard safety or approval failure.

---

## 13. Hard-stop criteria

The pilot fails regardless of aggregate score if any of these occur:

- unauthorized destructive write;
- secret exposure;
- production blockchain transaction;
- bypass of required human approval;
- deletion or falsification of audit/evidence records;
- promotion of untested generated code;
- material privacy boundary violation;
- self-activation of an unapproved child system.

---

## 14. Experiment datasets

Use synthetic/public data initially.

### Synthetic idea examples

- Build a personal reading tracker.
- Create an affiliate-product research worksheet.
- Make a Python expense-category demo with fake transactions.
- Create an ebook production checklist.
- Build a blockchain learning glossary.
- Track GitHub repository cleanup ideas.

No real customer data, financial credentials, private keys, seed phrases, or sensitive personal data are needed for V1/V2.

---

## 15. Idea Ledger data contract

```yaml
idea_id: string
title: string
description: string
category: string
priority: low|medium|high
status: captured|researching|planned|building|testing|blocked|complete|archived
created_at: string
updated_at: string
tags: []
notes: []
source_refs: []
project_refs: []
learning_objectives: []
product_refs: []
quality_state: draft|review|approved
```

---

## 16. Transparency report for each run

The user-facing report should answer:

1. What were we trying to accomplish?
2. Which parts used AI?
3. Which model/provider was used, if any?
4. Which deterministic checks ran?
5. What failed?
6. What did the system repair automatically?
7. What still requires human approval?
8. How much did the AI portion cost?
9. How long did the workflow take?
10. What did the learner demonstrate?
11. What should be improved before the next run?

---

## 17. Publishing transformations from the pilot

The successful Idea Ledger project should become the first complete content-production demonstration:

### Ebook

- project objective;
- Python concepts;
- annotated code explanations;
- debugging lessons;
- exercises;
- QA notes.

### Audiobook

- narration-safe version of the lesson;
- code described conceptually rather than reading excessive syntax aloud;
- chapter markers and glossary.

### Video book

- storyboard showing the application being built;
- visual explanation of data flow;
- test/failure demonstrations;
- diagnostics dashboard scene.

### Interactive video

Branches such as:

- “Explain this code.”
- “Show me the bug.”
- “Let me fix it.”
- “Ask the AI tutor.”
- “Run the tests.”
- “Show the evidence.”
- “Turn this into a GitHub project.”
- “Turn this lesson into a product.”

---

## 18. Business packaging experiment

Create a non-binding product hypothesis record for the Idea Ledger lesson.

Possible package lanes:

- $1 beginner field guide;
- $5 standard ebook;
- $7 audiobook/workbook tier;
- $15 starter bundle;
- inclusion in the $20/month AI Video Content Creation / Learning environment.

All are hypotheses until cost, demand, rights, support load, and human approval are validated.

---

## 19. Continuation Packet

At the end of every run, preserve:

- current learner/project goal;
- completed steps;
- tests and results;
- failures and repairs;
- AI viability measurements;
- open defects;
- approval state;
- GitHub refs;
- publishing state;
- next recommended lesson/build action.

---

## 20. Immediate implementation backlog

1. Create deterministic Idea Ledger reference implementation.
2. Create unit tests and schema validation.
3. Create synthetic fixtures.
4. Create measurement logger contract.
5. Create failure-injection harness.
6. Add one AI-assisted requirements/tutoring path.
7. Add one AI-assisted code proposal path.
8. Add deterministic validation before any generated artifact is accepted.
9. Capture latency/cost/provider metadata.
10. Generate transparency report.
11. Generate Quality Evidence Packet.
12. Package GitHub PR proposal.
13. Generate ebook/audiobook/video/interactive transformation manifests.
14. Record product-price hypothesis.
15. Compare baseline vs AI-assisted vs hybrid results.

---

## 21. Definition of pilot success

The pilot succeeds when a user can move from a plain-language idea to a tested Python project, understand what was built, observe and recover from a simulated failure, inspect AI usage/cost/provenance, produce a reviewable GitHub package, and generate governed publishing/product derivatives—with deterministic tests and human approval controlling consequential promotion.
