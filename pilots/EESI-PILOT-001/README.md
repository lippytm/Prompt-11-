# EESI-PILOT-001 — Evidence-Driven Clone Evolution Engine

This standard-library Python prototype turns evaluation records into **reviewable mutation proposals** for the authorized Charles Earl Lipshay AI interface.

It does not:

- rewrite its own source code;
- deploy a model or agent;
- access the internet;
- send messages;
- move money;
- sign contracts;
- impersonate Charles Earl Lipshay;
- fabricate personal memories;
- pass HumanApprovalGate.

## Run

```bash
python evolution_engine.py \
  --passport clone_passport.json \
  --evaluations evaluations.json \
  --output proposed_mutations.json
```

## Test

```bash
python -m unittest -v test_evolution_engine.py
```

## Learning objectives

Learners practice:

- Python dataclasses, validation, lists, dictionaries, JSON, hashing and command-line arguments;
- test-driven development;
- model evaluation and capability-gap analysis;
- safe AI-agent boundaries;
- why an improvement proposal is not the same as a deployed improvement;
- why financial and identity authority remain human controlled.

## Quantum Questions

- **IF:** What evidence would prove that a mutation improved performance rather than merely changing behavior?
- **MAYBE:** Could a lower score reflect a poor evaluation instead of a weak capability?
- **WHY NOT:** Why not let several model lines propose different training plans and compare them after independent evaluation?
- **DON'T DO THAT:** Do not let the engine auto-deploy code, grant itself permissions, access restricted data, or approve financial actions.

## Q-stage

Q2 structured implementation. It may become Q3 only after CI passes, independent model-line review is recorded, accessibility and security reviews are complete, and the Quality Evidence Packet is approved for a bounded pilot.
