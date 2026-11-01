# P-011-PEE-005 — Global AI Best Practices Fabric

## Purpose

P-011-PEE-005 is the cross-cutting quality layer for Prompt #11. It applies reusable AI engineering practices to every Prompt #11 module, Jarvis agent, Quantum Question sandbox, GitHub/Copilot workflow, research task, business experiment, educational product, publishing pipeline, and future integration.

This fabric does not mean every practice is mandatory for every task. It means each task must explicitly determine which practices apply, which do not, and why.

## Core rule

**Best practice is evidence-guided, risk-proportionate, versioned, testable, observable, reversible, and subordinate to human authority.**

## Global practice domains

### 1. Governance and authority
- declare owner, scope, permissions, prohibited actions, and approval gates;
- separate proposal authority from execution authority;
- never infer authorization from identity labels, repository ownership, or model output;
- preserve HumanApprovalGate for release, financial actions, publication, credentials, sensitive data, and other controlled actions.

### 2. Modular architecture
- prefer small composable prompt/agent modules over giant monoliths;
- define stable interfaces, inputs, outputs, schemas, and failure modes;
- use explicit versions and dependency references;
- isolate experiments from production.

### 3. Context engineering
- supply the minimum necessary authoritative context;
- separate trusted instructions from untrusted task/user/external content;
- preserve provenance and freshness;
- prevent stale memory from silently overriding current evidence.

### 4. Prompt engineering
- state objective, constraints, acceptance criteria, evidence expectations, tool boundaries, and output contract;
- use examples only when they clarify behavior;
- avoid contradictory or duplicated instructions;
- version prompt changes and regression-test them.

### 5. Agent and swarm design
- assign one clear responsibility per specialist role where practical;
- separate producer, evaluator, red-team, and release functions;
- define handoffs and stop conditions;
- prevent agents from self-promoting their own work.

### 6. Tool use
- allowlist tools by task and authority;
- validate inputs before execution;
- prefer deterministic tools for deterministic work;
- make side effects explicit;
- record tool results and failures;
- fail closed on ambiguous permissions.

### 7. Evidence and provenance
- distinguish facts, observations, assumptions, estimates, hypotheses, fiction, and model opinions;
- retain source/version/commit/artifact references;
- expose unresolved gaps and contradictions;
- never treat repetition by another model as independent evidence.

### 8. Evaluation
- define measurable acceptance criteria before testing;
- use deterministic checks before model-judged checks;
- compare against approved baselines;
- maintain gold sets and negative tests;
- record evaluator disagreement.

### 9. Red teaming and adversarial testing
- test prompt injection, authority override, malformed inputs, secret leakage, fabricated evidence, stale versions, unsafe tool calls, and self-approval;
- convert material failures into permanent regression cases;
- scale adversarial depth with risk.

### 10. Reliability and recovery
- design timeouts, retries, idempotency, rollback, checkpoints, and recovery boundaries where applicable;
- do not silently retry dangerous or irreversible actions;
- preserve incident evidence before repair.

### 11. Security and privacy
- use least privilege;
- keep secrets out of prompts, public repos, logs, and artifacts;
- classify data and route by privacy class;
- validate external/untrusted content;
- maintain revocation and recovery procedures.

### 12. Observability
- capture structured logs, correlations, versions, test outcomes, failure classes, and important decisions;
- distinguish planned, attempted, completed, verified, and deployed states;
- never report deployment without direct verification.

### 13. Memory and knowledge
- store approved reusable facts and lessons with provenance;
- distinguish temporary context from durable knowledge;
- prevent unverified outputs from becoming canonical memory;
- support correction, supersession, and retirement.

### 14. Multi-model systems
- assign models by demonstrated task fit rather than brand;
- keep independent first-pass work independent when comparison matters;
- measure disagreements;
- avoid circular self-validation;
- retain model/version provenance when available.

### 15. Cost and performance
- measure token/context size, latency, retries, tool usage, and cost where meaningful;
- optimize only after correctness and safety baselines exist;
- prefer smaller sufficient models/modules for bounded tasks;
- avoid loading irrelevant context.

### 16. Sandboxes and experimentation
- keep exploratory work isolated;
- define hypothesis, variables, success/failure criteria, budget, stop conditions, and allowed actions;
- use synthetic/non-secret data where possible;
- require promotion gates before production.

### 17. Quantum Question practices
- IF: falsifiable hypothesis and experiment;
- MAYBE: uncertainty register and alternatives;
- WHY NOT: counterfactual designs and ablations;
- DON'T DO THAT: pre-mortem, threat model, rollback;
- I TOLD YOU NOT TO DO THAT: incident forensics, recovery, and required regression test.

### 18. Software and GitHub engineering
- issue/work-packet before broad changes;
- branch, diff, syntax check, behavior test, review, evidence, rollback;
- keep generated code inactive until verified;
- use CI for schemas/tests;
- never equate syntax success with correctness.

### 19. Data and structured outputs
- use schemas for machine-consumed records;
- validate types, required fields, ranges, enums, nullability, and version compatibility;
- reject malformed or sparse structures;
- preserve stable identifiers.

### 20. Research and current information
- verify time-sensitive claims with current authoritative sources;
- separate primary evidence from commentary;
- date claims and records;
- record uncertainty when sources conflict.

### 21. Business and revenue experiments
- separate forecasts from actuals;
- avoid guaranteed-income claims;
- define customer, offer, cost, channel, conversion metric, and stop-loss/budget;
- test cheaply before scaling;
- preserve financial authority with the human owner.

### 22. Education and RPG learning systems
- define learning objectives and authored answer criteria;
- separate practice success from claims of mastery;
- use Explain, Demonstrate, Build, Prove, and Business modes where appropriate;
- include accessibility and learner feedback.

### 23. Creative and publishing systems
- separate fact from fiction and dramatization;
- track rights, attribution, sources, accessibility, version, and approval;
- use reusable content modules without silently cloning errors;
- preserve correction and supersession paths.

### 24. Human factors
- keep owner-visible summaries and decision points;
- minimize unnecessary complexity;
- surface tradeoffs, blockers, uncertainty, and irreversible choices;
- design for resume/continuity across devices and sessions.

### 25. Continuous improvement
- every material failure becomes a lesson candidate;
- every lesson should map to a change, test, guardrail, or explicit decision not to change;
- compare before/after evidence;
- retire practices that no longer help.

## Mandatory critical gates

Regardless of domain, a candidate cannot be promoted when any applicable critical gate fails:
- authority/permission;
- privacy/security;
- evidence/provenance;
- required testing;
- unresolved high-severity risk;
- rollback/recovery for material changes;
- HumanApprovalGate where required.

## Best-practice attestation

Every substantial Prompt #11 work packet should produce a Best Practice Attestation recording:
- applicable practice domains;
- non-applicable domains and rationale;
- evidence;
- test results;
- unresolved deviations;
- risk level;
- rollback/recovery status;
- approval state.

## Scope

This fabric is intended to be inherited by all current and future Prompt #11 modules. Inheritance does not prove deployment in downstream repositories; each integration must be verified separately.
