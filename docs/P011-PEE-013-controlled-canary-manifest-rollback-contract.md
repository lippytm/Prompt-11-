# P-011-PEE-013 — Controlled Canary Manifest & Rollback Contract

## Purpose

P11-PEE-013 defines the exact metadata required before a candidate that is READY_FOR_CANARY may enter a bounded canary.

It does not execute deployment.

## Required canary manifest

Every proposed canary must define:
- canary_id;
- target system/repository/service;
- exact candidate version/commit/ref;
- approved baseline version;
- bounded task class;
- canary scope;
- maximum duration or run count;
- success criteria;
- failure criteria;
- automatic stop conditions;
- rollback target;
- rollback procedure reference;
- post-canary verification plan;
- evidence collection plan;
- HumanApprovalGate audit reference.

## Canary rules

- no broad rollout;
- no silent expansion of scope;
- no irreversible change without separate confirmation;
- compare candidate against approved baseline;
- stop on critical error, security/privacy violation, high-severity regression, or rollback failure;
- preserve logs/evidence before repair;
- owner review required before any wider rollout.

## Acceptance criteria

1. canary manifest schema exists;
2. exact target/ref/baseline required;
3. success and failure criteria required;
4. stop conditions required;
5. rollback target and procedure required;
6. post-canary verification required;
7. HumanApprovalGate evidence required;
8. manifest itself never deploys.
