# Copilot instructions for this repo

This repo, `Prompt-11-`, is the canonical governance/rules engine for Charles Lipshay's `lippytm` org (lippytm.ai / "Business of Businesses"). It defines the risk-tier and approval-gate logic that other automation (Hermes engine, and separately, Zo Space) is built on top of.

## What "Prompt #11" means in this org
A continuous-improvement loop applied across repos, Zapier workflows, Dubb.AI scripts, Claude review prompts, and revenue paths:

```
Observe → Diagnose → Brainstorm → Package → Review → Build → Deploy → Measure → Improve
```

## Hard rules Copilot suggestions must respect
1. **This is a governance repo.** Any suggested change to approval-gate logic, safety-gate lists, or risk-tier definitions is a policy change, not a routine code change — flag it for explicit human review rather than auto-completing it confidently.
2. **Never suggest code that removes or weakens an approval gate.** The standing rule across this org: no destructive GitHub changes, public community posts, outbound Dubb messages, live Zap activation, or financial/funding claims without Charles's explicit approval.
3. **Never suggest guaranteed-outcome language** (funding approval, income, legal, tax, investment claims) in any content generated for `getbizfunds.com`-adjacent repos — this is a compliance requirement, not a style preference.
4. **Two systems currently implement this engine's rules independently:** the Hermes engine (`lippytm/Hermes-AI-Hermes`, code-enforced tier locking) and Zo Space (`lippytmai.zo.space/prompt-11-engine`, workflow-based). See issue #1 for the coordination question this raises — don't assume either one is the sole source of truth yet.

## Style
Write documentation and packet examples in plain, concrete language — this repo is read by both humans (Charles) and automation (Hermes, Zo, Claude review prompts), so ambiguity here propagates everywhere downstream.
