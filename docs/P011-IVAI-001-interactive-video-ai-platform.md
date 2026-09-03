# P-011-IVAI-001 — Interactive Video AI Platform

## Mission

Create a Prompt #11 governed interactive video intelligence platform that combines conversational AI, branching video, game-like learning, AI Clone identities, Hermes routing, Fabric workflows, Swarms, evidence controls, product manufacturing, and human-approved commerce.

The platform is intended to feel like a conversational AI interface expressed through interactive video rather than a text-only chat window. Users can ask questions, choose paths, enter learning missions, inspect evidence, build projects, and move among ebook, audiobook, video-book, interactive-video, coding, business, and creative modes.

## Relationship to Prompt #11

P-011-IVAI-001 does not replace existing Prompt #11 modules. It acts as an experience and delivery layer over them.

Primary dependencies:

- `P-011-MEPL-001` — product, evidence, quality, pricing, cost, revenue, correction, and lifecycle records.
- `P-011-EESI-001` — AI Clone Fabric, Fabric Hermes, Fable 5, Publishing Swarm, Ethical Revenue Swarm, and Control/Safety Swarm.
- `P-011-EEBDS-001` — educational-entertainment delivery and Character–Ecosystem Innovation Units.
- `P-011-OMNI-001` — continuity across mobile, computer, GitHub, ChatGPT, Gemini/NotebookLM, Claude/Hermes, Slack, and other approved platforms.
- `P-011-CRM-001` — relationship, membership, affiliate, support, campaign, and customer-quality workflows.
- `P-011-XPIO-001` — cross-platform I/O, adapters, diagnostics, identity boundaries, and transparency.

## Core experience modes

### 1. Chat Video Mode

A user asks a question by text or voice. A selected guide/avatar responds through synchronized video, audio, captions, transcript, and optional source cards. The response may offer next actions instead of ending as static output.

### 2. Interactive Video Book Mode

An approved ebook is converted into:

`manuscript → scene graph → narration → visual plan → video scenes → choices → evidence links → accessibility variants → QA package → release candidate`

Each scene retains a stable link back to its source chapter, claims, rights status, model-line provenance, and correction state.

### 3. Learning Quest Mode

Programming, blockchain, AI, cybersecurity, robotics, evidence literacy, publishing, and entrepreneurship are taught as missions. Each mission has:

- learning objective;
- prerequisite state;
- interactive explanation;
- challenge or build task;
- evidence/resources;
- automated tests where applicable;
- hints and remediation;
- completion evidence;
- optional product or affiliate pathway after approval.

### 4. Build Mode

The user may ask the system to help create a GitHub project, ebook, audiobook, video book, lesson, product, campaign, workflow, or other approved artifact. Hermes routes bounded tasks to eligible specialist agents. GitHub changes remain reviewable through branches and pull requests.

### 5. Evidence Mode

The interface separately presents:

- verified fact;
- official assessment;
- source quotation/paraphrase;
- allegation;
- hypothesis;
- uncertainty;
- contradiction;
- fictional dramatization;
- correction or supersession.

### 6. Business Mode

Approved products may move through:

`customer problem → offer hypothesis → format selection → price hypothesis → cost model → rights/risk review → Q3 experiment → human approval → limited sale → measurement → correction/scale/retirement`

### 7. Swarm Mode

Specialists can appear as visible panelists or operate behind the scenes. Initial roles:

- Product Owner Clone
- Prompt #11 QA/RiskGate Reviewer
- Source and Rights Reviewer
- Story Architect
- Ebook Editor
- Audiobook Adapter
- Video Storyboard Agent
- Interactive Branch Designer
- Accessibility Reviewer
- GitHub DevOps Clone
- Pricing Experiment Planner
- CRM/Affiliate Governance Agent
- Revenue Integrity Auditor
- Correction and Archive Steward

## Multi-AI integration model

ChatGPT/OpenAI may serve as the primary conversational experience where available, but the architecture must remain provider-agnostic.

Independent model lines:

- ChatGPT/OpenAI line
- Claude line
- Gemini/NotebookLM line
- future approved AI/provider lines

Each line maintains its own provenance, outputs, evaluation results, and QA status until a comparison or merged-premium edition is explicitly approved.

The core platform must communicate through provider adapters rather than embedding provider-specific assumptions into product, scene, task, or evidence schemas.

## Scene graph contract

Each interactive scene should minimally track:

```yaml
scene_id: IVAI-SCENE-0001
product_id: PRODUCT-ID
source_unit_id: CHAPTER-OR-LESSON-ID
mode: chat_video|video_book|learning_quest|build|evidence|business|swarm
status: draft
privacy_class: public
risk_gate: green
model_line: chatgpt
speaker_profile_id: AGENT-OR-CHARACTER-ID
prompt_context_refs: []
source_refs: []
claim_refs: []
media_assets: []
caption_asset: null
transcript_asset: null
choices: []
next_scene_ids: []
required_gates: []
human_approval: pending
```

## Interaction contract

An interaction records:

- interaction ID;
- user intent category;
- current scene;
- user input type;
- task generated;
- routed agent/workflow;
- response scene;
- evidence references;
- safety/quality decisions;
- latency/cost metrics where available;
- whether human approval is required;
- whether a product/revenue action was proposed or executed.

## Publishing manufacturing pipeline

One approved source product should be reusable across formats without losing traceability:

1. Canonical source manuscript
2. Ebook edition
3. Audiobook adaptation
4. Video-book adaptation
5. Interactive-video edition
6. Accessibility edition
7. Affiliate/resale companion edition where rights allow
8. Bundle or membership inclusion where approved
9. Correction/supersession propagation across all editions

## Price catalog — starting hypotheses

The platform should maintain pricing as versioned catalog data, not hard-coded application logic.

Initial hypotheses based on the existing product roadmap:

| Offer | Starting price hypothesis |
|---|---:|
| Entry field-guide ebook | $1 |
| Affiliate/resale companion edition | $2 |
| Standard ebook | $5 |
| Audiobook or selected master-product tier | $7 |
| Affiliate ebook / builder tier | $10 |
| Starter bundle or affiliate audiobook | $15 |
| AI Video Content Creation Machine | $20/month |
| Standard/special ebook list-price experiment | $27 |
| Launch Map / starter implementation package | $30 |

Prices are hypotheses until approved for a specific product, channel, rights package, tax/payment setup, support level, and experiment. The platform must never imply guaranteed earnings.

## Pricing record

```yaml
price_id: PRICE-0001
product_id: PRODUCT-ID
edition_id: EDITION-ID
currency: USD
amount: 5.00
billing_mode: one_time
channel: direct
status: hypothesis
rights_clearance: pending
cost_model_ref: null
margin_target: null
effective_from: null
effective_to: null
human_approval: pending
```

## Release gates

No public release or sale unless required gates pass, including as applicable:

- EvidenceGate
- RightsGate
- PrivacyGate
- Identity/ConsentGate
- Fiction/RealityBoundaryGate
- AccessibilityGate
- SecurityGate
- QualityGate
- ModelLineIndependenceGate
- Price/CostGate
- AffiliateDisclosureGate
- RevenueIntegrityGate
- HumanApprovalGate

## MVP v0.1

The first proof should use one approved Prompt #11 product and demonstrate:

1. manuscript/lesson import;
2. scene graph generation;
3. at least three connected interactive scenes;
4. one conversational question path;
5. one learning/build choice;
6. evidence/source drawer specification;
7. ebook, audiobook, and video-book production task generation;
8. price-catalog association;
9. Prompt #11 QA/RiskGate status;
10. human approval before publication or sale.

## First candidate pilots

- `$1 Prompt #11 Evidence Processing Field Guide`
- `$2 Prompt #11 Affiliate Edition`
- `$7 Prompt #11 Master Evidence & Product Ledger`
- Lippy Killjoy / Encyclopedia of Everything Applied CEIU pilot
- beginner programming/blockchain lesson

## Non-goals for v0.1

- autonomous financial transactions;
- autonomous publishing to public channels;
- unrestricted agent access to repositories or accounts;
- automatic NFT minting;
- pretending Claude, Gemini, GitHub, or any external platform integration is live before an adapter is actually configured and tested;
- generating a large game engine before the core scene/interaction contracts are proven.

## Success criteria

P-011-IVAI-001 succeeds when one approved Prompt #11 knowledge product can be transformed into a traceable interactive experience that supports conversation, branching learning, multimedia editions, product packaging, pricing hypotheses, GitHub development tasks, model-line provenance, QA evidence, corrections, and human-approved release decisions.