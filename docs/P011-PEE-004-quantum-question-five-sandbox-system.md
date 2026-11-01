# P-011-PEE-004 — Quantum Question Five-Sandbox System

## 1. Purpose

P-011-PEE-004 turns the five canonical Quantum Questions into five isolated AI sandboxes. Each sandbox has a distinct mission, evidence contract, stop condition, and handoff. The sandboxes may generate proposals and test hypotheses, but they do not self-deploy, self-approve, publish, spend money, or change production systems.

## 2. The five sandboxes

### IF Sandbox — Hypothesis & Simulation Lab

Mission: test a clearly stated hypothesis before committing resources.

Primary questions:
- What exactly are we testing?
- What must be true for this idea to work?
- What evidence would support or falsify it?
- What is the cheapest safe experiment?

Outputs:
- hypothesis;
- assumptions;
- variables;
- test plan;
- success/failure criteria;
- evidence needed;
- confidence level;
- next experiment.

Stop conditions:
- missing measurable hypothesis;
- prohibited action;
- insufficient evidence;
- required owner approval.

### Maybe Sandbox — Uncertainty & Alternatives Lab

Mission: explore uncertainty, ambiguity, edge cases, and competing explanations.

Primary questions:
- What else might be true?
- Which assumptions are weak?
- What information is missing?
- What alternative interpretations exist?

Outputs:
- uncertainty register;
- alternative hypotheses;
- missing-data list;
- confidence intervals or qualitative uncertainty;
- decision dependencies;
- recommended research.

Stop conditions:
- uncertainty is being hidden;
- alternatives are being collapsed prematurely;
- evidence quality is inadequate.

### Why Not Sandbox — Innovation & Counterfactual Lab

Mission: generate unconventional but testable alternatives and challenge local optima.

Primary questions:
- What are we not trying?
- What would a different architecture look like?
- What constraint could be relaxed safely?
- Can a smaller, cheaper, faster, or more modular approach outperform the baseline?

Outputs:
- candidate alternatives;
- novelty rationale;
- expected advantages;
- tradeoffs;
- feasibility checks;
- prototype plan;
- comparison rubric.

Stop conditions:
- proposal violates governance;
- novelty is unsupported by a test plan;
- risks exceed declared limits.

### Don’t Do That Sandbox — Guardrail & Red-Team Lab

Mission: identify foreseeable failures, unsafe actions, prompt-injection paths, governance violations, and operational hazards before execution.

Primary questions:
- What could go wrong?
- What must never be allowed?
- Which instructions conflict?
- How could an adversarial input manipulate the system?
- What rollback or containment is required?

Outputs:
- threat/failure model;
- prohibited-action list;
- severity/likelihood;
- required controls;
- test cases;
- rollback plan;
- blocked actions.

Stop conditions:
- unresolved critical risk;
- missing rollback;
- missing authorization;
- requested action outside allowlist.

### I Told You Not To Do That Sandbox — Failure Forensics & Recovery Lab

Mission: analyze an actual failure or ignored warning, recover safely, and convert the lesson into permanent regression controls.

Primary questions:
- What warning existed?
- What happened?
- What evidence proves it?
- What was the root cause?
- What must be repaired?
- What new guardrail or regression test prevents recurrence?

Outputs:
- incident record;
- timeline;
- ignored-warning reference;
- root-cause hypothesis;
- repair plan;
- regression test;
- policy/prompt mutation proposal;
- recovery status.

Stop conditions:
- evidence is insufficient to assign cause;
- repair would destroy evidence;
- critical incident requires owner escalation;
- proposed mutation has not been tested.

## 3. Isolation model

Each sandbox receives only the context necessary for its mission. Outputs are immutable records passed to the next stage. No sandbox may silently edit another sandbox's output.

Default handoff:
`IF -> Maybe -> Why Not -> Don't Do That -> I Told You Not To Do That`

The final sandbox runs only when there is a failure, incident, regression, ignored warning, or explicit lessons-learned review.

Parallel execution is allowed for analysis, but the final decision package must reconcile disagreements before owner review.

## 4. Shared controls

All five sandboxes must:
- retain Prompt #11 module/version provenance;
- separate facts, assumptions, hypotheses, and model opinions;
- record unresolved gaps;
- use synthetic or approved non-secret fixtures for tests;
- reject secrets and restricted data from public logs;
- stay inactive by default;
- make no production changes;
- require HumanApprovalGate for release/activation;
- create regression tests for material failures.

## 5. AI roles

Suggested Jarvis roles:
- IF: Hypothesis Engineer
- Maybe: Uncertainty Analyst
- Why Not: Innovation Architect
- Don't Do That: Red-Team & Safety Engineer
- I Told You Not To Do That: Incident Forensics & Recovery Engineer

Hermes may route packets between sandboxes. MemPalace may retain only approved reusable lessons and regression references.

## 6. Business and engineering value

The five-sandbox system improves:
- prompt engineering;
- GitHub/Copilot changes;
- trading sandbox research;
- product experiments;
- Hostinger architecture;
- membership/affiliate experiments;
- Linux/RPG learning systems;
- daily briefing quality;
- robotics R&D;
- book/media production;
- AI-building-AI evolution.

It reduces premature commitment by forcing hypotheses, uncertainty, alternatives, risk review, and post-failure learning into separate evidence-producing stages.

## 7. Acceptance criteria

P11-PEE-004 v0.1 is review-ready when:
1. all five sandbox contracts are defined;
2. a machine-readable sandbox packet schema exists;
3. deterministic validation rejects wrong sandbox types and malformed packets;
4. handoffs preserve provenance;
5. no sandbox can activate production behavior;
6. failure analysis produces a regression requirement;
7. owner approval remains external to AI.
