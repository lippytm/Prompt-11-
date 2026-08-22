# OMNI-PILOT-001 — Lippy Killjoy and the Evidence Passport

**Purpose:** Turn an iPhone-captured idea into a beginner Python lesson that can be reviewed on iPad, built and tested on an ASUS laptop, versioned in GitHub, coordinated in Slack, and handed independently to Gemini/NotebookLM and Claude/Fabric Hermes.

**Current status:** ChatGPT-line code lab complete; eight unit tests pass. Independent model-line work, physical device review, and HumanApprovalGate remain pending.

## The Educational Entertainment story

In the Marketplace of Unfinished Futures, dazzling inventions arrive with enormous promises but incomplete evidence. Lippy Killjoy, Nexus Nine, does not destroy the marketplace. He gives every idea an **Evidence Passport**.

The passport asks:

- What is this idea?
- Is the statement verified, assessed, testified, alleged, hypothetical, fictional, or contradicted?
- What evidence or disclosure is required?
- Is the information public or restricted?
- What is the current RiskGate?
- Has the product reached Q4?
- Have the critical gates passed?
- Has an authorized human approved release?

The program never releases or publishes anything. It only explains whether a record is blocked, review-only, not requested, or structurally eligible for an authorized human release.

## What the learner practices

- Python dictionaries
- constants and sets
- functions
- conditionals
- loops and list comprehensions
- type checking
- JSON files
- command-line arguments
- error handling
- deterministic serialization
- SHA-256 integrity hashes
- unit testing with `unittest`
- privacy, risk, quality, and human-approval logic

## Files

- `evidence_passport.py` — validator and command-line program
- `test_evidence_passport.py` — eight unit tests
- `sample_passport.json` — safe Q3 fictional sample
- `model-line-handoffs/chatgpt-treatment.md` — completed ChatGPT treatment
- `model-line-handoffs/gemini-notebooklm-handoff.md` — independent research assignment
- `model-line-handoffs/claude-hermes-handoff.md` — independent red-team assignment
- `continuation-packet.json` — portable checkpoint

## Run on the ASUS laptop

No external package is required. Use Python 3.10 or newer.

```bash
cd pilots/OMNI-PILOT-001
python evidence_passport.py sample_passport.json
python -m unittest -v
```

Expected sample decision:

```text
REVIEW_ONLY — Q4 or higher is required for approved inventory
```

Expected test result:

```text
Ran 8 tests
OK
```

## Device roles

**iPhone:** capture the idea, read the story and learning goals, record the exact next action, and update the Continuation Packet.

**iPad:** annotate the lesson, inspect readability and touch navigation, and review cognitive load and accessibility.

**ASUS laptop:** run the code and tests, make controlled edits, commit through GitHub, compare model-line outputs, and prepare Q3 evidence.

Never place passwords, API keys, wallet seeds, private keys, recovery codes, full identity or medical records, confidential witnesses, or unpublished restricted evidence in the lesson.

## Programming exercises

1. Change `risk_gate` from `Yellow` to `Red` and explain why release becomes blocked.
2. Change `truth_label` to `VF`, test with and without a public `source_url`, and compare results.
3. Change `privacy_class` to `Restricted` while `publish_requested` is `true` and confirm the block.
4. Change the stage to `Q4`, set RiskGate to Green and critical gates to passed, but leave human approval pending. Explain why release remains review-only.
5. Add a unit test showing that an unknown truth label is rejected.

## Optional blockchain connection

The program calculates a SHA-256 hash from canonical JSON. A learner can record that hash in a ledger to show that a specific version existed and has not changed.

The hash does **not** prove that the underlying claim is true, safe, legal, useful, or valuable. It supports integrity and version comparison only.

## Optional entrepreneurship connection

Treat the Evidence Passport as a product-readiness checklist. Ask:

- What customer problem is being solved?
- Which claims require evidence?
- What would a safe pilot cost?
- What must be tested before charging money?
- What refund, correction, support, and retirement procedures are needed?
- Which metrics show customer value rather than mere attention?

No exercise guarantees revenue, funding, employment, token value, or business success.

## Quantum Questions

**IF:** If the passport says a product is review-ready, what evidence would still be needed before release?

**MAYBE:** Maybe a missing source is an honest documentation error rather than deception. How should the system distinguish error, uncertainty, and intentional misconduct?

**WHY NOT:** Why not create reusable Evidence Passports for code repositories, ebooks, lessons, smart contracts, AI agents, campaigns, and franchise nodes?

**DON’T DO THAT:** Do not convert the exercise into a system that automatically publishes content, transfers money, makes medical or legal judgments, exposes restricted data, or treats a hash as proof of truth.

## Completion evidence

The ChatGPT-line implementation currently has:

- one runnable Python program;
- one sample JSON passport;
- eight passing unit tests;
- a stable content-hash test;
- explicit fiction, privacy, risk, Q4, and HumanApprovalGate controls;
- no external dependencies;
- no secret or restricted personal data.

## Remaining before Q3 completion

- physical iPhone and iPad review;
- issue #9 device and account evidence;
- independent Gemini/NotebookLM treatment;
- independent Claude/Fabric Hermes treatment;
- model-line comparison and contradiction report;
- learner-outcome rubric and beginner test session;
- accessibility review;
- final Q3 Quality Evidence Packet;
- explicit human decision.
