# P-011-MEPL-001 — $7 Prompt #11 Master Evidence and Product Ledger Data Model

**Parent:** P-011-OMNI-001  
**Related:** P-011-EEBDS-001, P-011-E6C-001, P-011-E6C-CHAR-001, P-011-DSF-001  
**Work packet:** WP-OMNI-0005  
**Status:** Data-model architecture v0.1  
**Target implementation:** Q3 accessible spreadsheet prototype, followed by an optional database implementation  
**Governing law:** Quality and Quality Assurance is Job #1.

## 1. Purpose

The Master Evidence and Product Ledger—MEPL—is the authoritative operational record for the Prompt #11 Business of Businesses. It connects project continuity, sources, claims, products, educational systems, fictional characters and ecosystems, independent AI model lines, quality assurance, media production, business experiments, devices, connectors, incidents, corrections, franchises, and archives.

The ledger must answer five questions at any time:

1. **Where are we now?**
2. **What has been completed and what evidence proves it?**
3. **What is blocked, risky, contradicted, unapproved, or unsafe?**
4. **What is the highest-priority unblocked next action?**
5. **What may be released, sold, taught, replicated, corrected, or retired?**

The first implementation should be understandable and usable as an `.xlsx` workbook. Stable identifiers, enumerations, relationships, and audit rules must allow later migration to PostgreSQL, SQLite, Airtable, or another approved database without changing canonical meanings.

## 2. Non-negotiable principles

- One stable ID per object for its entire lifecycle.
- New versions do not overwrite approved history.
- Public, internal, confidential, and restricted information have separate routing and export rules.
- ChatGPT, Gemini/NotebookLM, and Claude/Fabric Hermes editions remain separate until independent QA is complete.
- A model’s agreement with another model is not source verification.
- A blockchain hash proves file integrity or existence, not factual truth.
- Q4 is the minimum certification for approved product inventory.
- A Red RiskGate or failed critical gate blocks release.
- HumanApprovalGate can be passed only by an identified authorized human.
- Documentation, mockups, schemas, manifests, and planned routes are not deployed services.
- Corrections must propagate to every affected product, edition, campaign, repository, channel, and public provenance record.
- Restricted personal evidence is not stored in the public MEPL prototype.

## 3. Data architecture

MEPL uses five layers.

### Layer A — Identity and hierarchy

Defines the object, owner, module, program, workstream, work packet, version, model line, device, platform, and privacy class.

### Layer B — Evidence and quality

Defines sources, claims, contradictions, requirements, tests, defects, risks, gates, decisions, approvals, incidents, corrections, and audit events.

### Layer C — Product and learning delivery

Defines products, editions, characters, ecosystems, CEIUs, lessons, skills, assessments, Build Mode projects, media assets, NFT provenance, offers, campaigns, affiliates, support, and outcomes.

### Layer D — Business and operations

Defines costs, revenue events, forecasts, customer or learner outcomes, device and connector state, franchise nodes, audits, succession, and retirement.

### Layer E — Views and exports

Provides dashboards, mobile summaries, review queues, reports, CSV exports, JSON bundles, GitHub work packets, Slack notifications, NotebookLM source manifests, and future Tower Control API payloads.

## 4. Entity relationship overview

```text
Module
  └── Program
       └── Workstream
            └── WorkPacket
                 ├── ContinuationPacket
                 ├── Decision
                 ├── Artifact
                 ├── Requirement ── Test ── Defect
                 ├── Risk ── Gate ── Approval
                 └── AuditEvent

Source ── Claim ── Contradiction
                └── ProductVersion

Product
  └── ProductVersion
       ├── ModelLineEdition
       ├── MediaAsset
       ├── NFTProvenance
       ├── Offer ── Campaign ── Affiliate
       ├── RevenueEvent / CostEvent / SupportEvent
       ├── Incident ── Correction ── Retirement
       └── QualityEvidencePacket

Character ── CEIU ── Ecosystem
                  ├── LearningObject ── Skill ── Assessment
                  └── BuildProject

Device ── Platform ── Connector
                        └── WorkPacket / AuditEvent / Incident

FranchiseNode ── Audit ── Approval / Correction / Retirement
```

Many-to-many relationships use explicit junction tables or link records rather than comma-separated IDs.

## 5. Stable identifier registry

| Entity | Prefix | Example |
|---|---|---|
| Module | `MOD-` | `MOD-P011-OMNI-001` |
| Program | `PRG-` | `PRG-LEARNING-001` |
| Workstream | `WS-` | `WS-MEPL-001` |
| Work packet | `WP-` | `WP-OMNI-0005` |
| Continuation packet | `CP-` | `CP-OMNI-20260822-005` |
| Decision | `DEC-` | `DEC-MEPL-0001` |
| Artifact | `ART-` | `ART-MEPL-DM-001` |
| Source | `SRC-` | `SRC-FTC-IDTHEFT-2025` |
| Claim | `CLM-` | `CLM-MEPL-0001` |
| Contradiction | `CON-` | `CON-MEPL-0001` |
| Requirement | `REQ-` | `REQ-MEPL-0001` |
| Test | `TST-` | `TST-MEPL-0001` |
| Defect | `DEF-` | `DEF-MEPL-0001` |
| Risk | `RSK-` | `RSK-MEPL-0001` |
| Gate result | `GATE-` | `GATE-MEPL-0001` |
| Approval | `APR-` | `APR-MEPL-0001` |
| Product | `PROD-` | `PROD-P011-MEPL-001` |
| Product version | `VER-` | `VER-P011-MEPL-001-V010` |
| Model-line edition | `ED-` | `ED-MEPL-CHATGPT-V010` |
| Character | `CHAR-` | `CHAR-E6C-009-019` |
| Ecosystem | `ECO-` | `ECO-DIGITAL-CYBER-001` |
| CEIU | `CEIU-` | `CEIU-LK9-QUANTUM-INNOVATION-001` |
| Learning object | `LO-` | `LO-PYTHON-001` |
| Skill | `SKILL-` | `SKILL-DEBUG-001` |
| Assessment | `ASM-` | `ASM-PYTHON-001` |
| Build project | `BUILD-` | `BUILD-INNOVATION-PASSPORT-001` |
| Media asset | `MEDIA-` | `MEDIA-MEPL-EBOOK-001` |
| NFT provenance | `NFT-` | `NFT-MEPL-EDITION-001` |
| Offer | `OFFER-` | `OFFER-P011-7-LEDGER-001` |
| Campaign | `CAM-` | `CAM-MEPL-PILOT-001` |
| Affiliate | `AFF-` | `AFF-MEPL-0001` |
| Revenue event | `REV-` | `REV-MEPL-202608-001` |
| Cost event | `COST-` | `COST-MEPL-202608-001` |
| Support event | `SUP-` | `SUP-MEPL-0001` |
| Device | `DEV-` | `DEV-IPHONEX-001` |
| Platform | `PLAT-` | `PLAT-GITHUB-001` |
| Connector | `CONN-` | `CONN-GITHUB-ISSUES-001` |
| Incident | `INC-` | `INC-MEPL-0001` |
| Correction | `COR-` | `COR-MEPL-0001` |
| Retirement | `RET-` | `RET-MEPL-0001` |
| Franchise node | `NODE-` | `NODE-LIPPYTM-001` |
| Audit | `AUD-` | `AUD-NODE-001-2026` |
| Archive record | `ARC-` | `ARC-MEPL-0001` |
| Audit event | `EVT-` | `EVT-MEPL-000001` |
| Quality Evidence Packet | `QEP-` | `QEP-MEPL-Q3-001` |

IDs are never reused, even after retirement.

## 6. Core tables and required fields

The field dictionary below gives the minimum fields. Implementations may add fields but may not silently change definitions.

### 6.1 `Modules`

- `module_id` — primary key
- `module_name`
- `module_version`
- `status`
- `parent_module_id`
- `canonical_repository`
- `canonical_path`
- `human_owner`
- `privacy_class`
- `created_at`
- `updated_at`
- `supersedes_module_id`
- `retirement_id`

### 6.2 `Programs`

- `program_id` — primary key
- `module_id` — foreign key
- `program_name`
- `purpose`
- `human_owner`
- `status`
- `priority`
- `privacy_class`
- `start_date`
- `target_date`
- `actual_completion_date`

### 6.3 `Workstreams`

- `workstream_id` — primary key
- `program_id` — foreign key
- `workstream_name`
- `objective`
- `owner`
- `reviewer`
- `status`
- `priority`
- `percent_complete`
- `blocked_reason`
- `current_work_packet_id`

### 6.4 `WorkPackets`

- `work_packet_id` — primary key
- `workstream_id` — foreign key
- `title`
- `objective`
- `scope_in`
- `scope_out`
- `acceptance_criteria`
- `owner`
- `model_line`
- `device_id`
- `platform_id`
- `privacy_class`
- `status`
- `priority`
- `dependency_ids`
- `issue_reference`
- `branch_reference`
- `pull_request_reference`
- `started_at`
- `due_at`
- `completed_at`
- `next_action`

### 6.5 `ContinuationPackets`

- `continuation_packet_id` — primary key
- `packet_version`
- `supersedes_packet_id`
- `work_packet_id`
- `status`
- `created_at`
- `human_owner`
- `reviewer`
- `device_id`
- `platform_id`
- `model_line`
- `privacy_class`
- `objective_summary`
- `work_completed_summary`
- `blocker_summary`
- `highest_priority_next_action`
- `resume_prompt`
- `risk_gate`
- `certification_level`
- `human_approval_status`
- `artifact_reference`

### 6.6 `Decisions`

- `decision_id` — primary key
- `work_packet_id`
- `decision_text`
- `rationale`
- `evidence_reference`
- `decided_by`
- `decision_date`
- `reversible`
- `review_date`
- `status`
- `superseded_by_decision_id`

### 6.7 `Artifacts`

- `artifact_id` — primary key
- `work_packet_id`
- `product_version_id`
- `artifact_type`
- `title`
- `version`
- `location`
- `repository`
- `branch`
- `commit_sha`
- `content_hash`
- `media_type`
- `privacy_class`
- `rights_status`
- `status`
- `created_by`
- `created_at`
- `approved_by`
- `approved_at`
- `supersedes_artifact_id`

### 6.8 `Sources`

- `source_id` — primary key
- `title`
- `author_or_organization`
- `source_type`
- `publication_date`
- `retrieved_at`
- `canonical_reference`
- `primary_or_secondary`
- `authority_score`
- `relevance_score`
- `currency_score`
- `independence_group`
- `rights_status`
- `privacy_class`
- `content_hash`
- `archived_reference`
- `notes`

`independence_group` identifies sources that ultimately derive from the same original evidence.

### 6.9 `Claims`

- `claim_id` — primary key
- `claim_text`
- `truth_label`
- `claim_domain`
- `subject`
- `date_context`
- `geographic_context`
- `status`
- `confidence`
- `publication_status`
- `owner`
- `last_verified_at`
- `freshness_due_at`
- `correction_id`

### 6.10 `ClaimSourceLinks`

- `claim_source_link_id` — primary key
- `claim_id`
- `source_id`
- `support_type` — supports, contradicts, contextualizes, quotes, metadata_only
- `source_location`
- `evidence_summary`
- `reviewer`
- `reviewed_at`

### 6.11 `Contradictions`

- `contradiction_id` — primary key
- `claim_id_a`
- `claim_id_b`
- `source_id_a`
- `source_id_b`
- `contradiction_type`
- `materiality`
- `status`
- `resolution_method`
- `resolution_summary`
- `resolved_by`
- `resolved_at`

### 6.12 `Requirements`

- `requirement_id` — primary key
- `work_packet_id`
- `product_version_id`
- `requirement_type`
- `requirement_text`
- `priority`
- `critical`
- `source_reference`
- `acceptance_method`
- `status`
- `owner`
- `due_at`

### 6.13 `Tests`

- `test_id` — primary key
- `requirement_id`
- `test_type`
- `test_name`
- `procedure`
- `expected_result`
- `actual_result`
- `status`
- `performed_by`
- `performed_at`
- `evidence_reference`
- `environment`
- `repeatable`

### 6.14 `Defects`

- `defect_id` — primary key
- `test_id`
- `artifact_id`
- `product_version_id`
- `severity`
- `title`
- `description`
- `privacy_or_security_impact`
- `status`
- `owner`
- `detected_at`
- `target_fix_date`
- `fixed_at`
- `verification_test_id`
- `release_blocking`

### 6.15 `Risks`

- `risk_id` — primary key
- `object_type`
- `object_id`
- `category`
- `description`
- `likelihood`
- `impact`
- `risk_score`
- `risk_gate`
- `mitigation`
- `owner`
- `status`
- `review_due_at`
- `residual_risk`
- `accepted_by`

### 6.16 `GateResults`

- `gate_result_id` — primary key
- `object_type`
- `object_id`
- `gate_name`
- `critical`
- `status`
- `evidence_reference`
- `reviewer`
- `reviewed_at`
- `conditions`
- `expires_at`
- `supersedes_gate_result_id`

### 6.17 `Approvals`

- `approval_id` — primary key
- `object_type`
- `object_id`
- `approval_type`
- `status`
- `requested_by`
- `requested_at`
- `approver`
- `decided_at`
- `scope`
- `conditions`
- `expires_at`
- `revoked_at`
- `audit_reference`

An AI identity cannot be entered as the `approver` for HumanApprovalGate.

### 6.18 `Products`

- `product_id` — primary key
- `product_family`
- `product_name`
- `description`
- `product_type`
- `ceiu_id`
- `human_owner`
- `privacy_class`
- `status`
- `current_version_id`
- `inventory_status`
- `franchise_eligible`
- `created_at`
- `retirement_id`

### 6.19 `ProductVersions`

- `product_version_id` — primary key
- `product_id`
- `version`
- `title`
- `certification_level`
- `risk_gate`
- `status`
- `model_independence_required`
- `source_manifest_reference`
- `quality_packet_id`
- `release_eligibility`
- `release_block_reason`
- `approved_at`
- `published_at`
- `supersedes_version_id`

### 6.20 `ModelLineEditions`

- `edition_id` — primary key
- `product_version_id`
- `model_line`
- `edition_type`
- `status`
- `independent_first_pass`
- `source_manifest_reference`
- `working_location`
- `quality_packet_id`
- `approved_by`
- `approved_at`
- `comparison_eligible`
- `merged_premium_eligible`

Allowed `model_line` values:

- `chatgpt_business`
- `gemini_notebooklm`
- `claude_fabric_hermes`
- `human_editorial`
- `comparison`
- `merged_premium`

### 6.21 `Characters`

- `character_id` — primary key
- `public_name`
- `creator_or_rights_owner`
- `fiction_status`
- `passport_reference`
- `permissions`
- `limitations`
- `voice_likeness_status`
- `rights_status`
- `privacy_class`
- `status`

### 6.22 `Ecosystems`

- `ecosystem_id` — primary key
- `ecosystem_name`
- `environment_type`
- `description`
- `affected_groups`
- `dependencies`
- `risks`
- `measures`
- `status`

### 6.23 `CEIUs`

- `ceiu_id` — primary key
- `title`
- `character_id`
- `primary_ecosystem_id`
- `truth_boundary`
- `quantum_questions_reference`
- `learning_summary`
- `story_summary`
- `innovation_summary`
- `business_summary`
- `certification_level`
- `risk_gate`
- `status`
- `entry_passport_reference`

Use junction table `CEIUEcosystemLinks` for additional ecosystems.

### 6.24 `LearningObjects`

- `learning_object_id` — primary key
- `ceiu_id`
- `title`
- `object_type`
- `learning_level`
- `audience`
- `prerequisites`
- `objectives`
- `assessment_summary`
- `accessibility_requirements`
- `estimated_duration`
- `status`
- `version`

### 6.25 `Skills`

- `skill_id` — primary key
- `skill_name`
- `domain`
- `level`
- `description`
- `evidence_required`
- `prerequisite_skill_id`
- `status`

Use junction table `LearningObjectSkillLinks`.

### 6.26 `Assessments`

- `assessment_id` — primary key
- `learning_object_id`
- `assessment_type`
- `instructions`
- `rubric_reference`
- `passing_rule`
- `attempt_limit`
- `human_review_required`
- `privacy_class`
- `status`

### 6.27 `BuildProjects`

- `build_project_id` — primary key
- `ceiu_id`
- `learning_object_id`
- `title`
- `problem`
- `requirements`
- `repository`
- `test_plan`
- `security_review`
- `accessibility_review`
- `environmental_review`
- `status`
- `certification_level`

### 6.28 `MediaAssets`

- `media_asset_id` — primary key
- `product_version_id`
- `edition_id`
- `media_type`
- `title`
- `file_or_location`
- `duration_or_length`
- `language`
- `accessibility_assets`
- `rights_status`
- `privacy_class`
- `content_hash`
- `status`

### 6.29 `NFTProvenance`

- `nft_provenance_id` — primary key
- `product_version_id`
- `media_asset_id`
- `network`
- `contract_reference`
- `token_or_edition_reference`
- `public_metadata_reference`
- `content_hash`
- `license_reference`
- `correction_reference`
- `mint_status`
- `privacy_review_status`
- `rights_review_status`
- `investment_disclaimer_present`

No private or restricted information belongs in this table’s public export.

### 6.30 `Offers`

- `offer_id` — primary key
- `product_id`
- `offer_name`
- `customer_problem`
- `value_proposition`
- `scope`
- `exclusions`
- `price_assumption`
- `currency`
- `recurring`
- `support_commitment`
- `refund_policy_reference`
- `claims_review_status`
- `status`

### 6.31 `Campaigns`

- `campaign_id` — primary key
- `offer_id`
- `campaign_name`
- `audience`
- `channel`
- `budget`
- `start_date`
- `end_date`
- `status`
- `campaign_passport_reference`
- `truth_and_disclosure_status`
- `accessibility_status`
- `correction_plan`
- `stop_conditions`

### 6.32 `Affiliates`

- `affiliate_id` — primary key
- `human_or_business_name`
- `agreement_reference`
- `approved_offers`
- `commission_rule`
- `disclosure_requirement`
- `payment_status`
- `privacy_class`
- `status`

Use `CampaignAffiliateLinks` for many-to-many assignment.

### 6.33 `RevenueEvents`

- `revenue_event_id` — primary key
- `product_id`
- `offer_id`
- `campaign_id`
- `affiliate_id`
- `event_date`
- `event_type`
- `quantity`
- `gross_amount`
- `discount_amount`
- `refund_amount`
- `fee_amount`
- `net_amount`
- `currency`
- `payment_status`
- `source_reference`
- `privacy_class`

### 6.34 `CostEvents`

- `cost_event_id` — primary key
- `program_id`
- `product_id`
- `campaign_id`
- `event_date`
- `cost_category`
- `vendor_or_platform`
- `amount`
- `currency`
- `recurring`
- `source_reference`
- `privacy_class`

### 6.35 `SupportEvents`

- `support_event_id` — primary key
- `product_id`
- `customer_or_learner_reference`
- `event_date`
- `event_type`
- `severity`
- `summary`
- `privacy_class`
- `status`
- `owner`
- `resolution_summary`
- `correction_id`

The public prototype should use anonymized or synthetic customer and learner references.

### 6.36 `Devices`

- `device_id` — primary key
- `device_type`
- `owner`
- `business_or_personal`
- `operating_system`
- `encryption_status`
- `update_status`
- `backup_status`
- `restore_tested`
- `mfa_capable`
- `approved_privacy_classes`
- `last_security_review`
- `status`

No serial number, password, recovery code, or device unlock credential is required in the public ledger.

### 6.37 `Platforms`

- `platform_id` — primary key
- `platform_name`
- `account_or_workspace_label`
- `human_owner`
- `business_or_personal`
- `primary_role`
- `approved_privacy_classes`
- `recovery_verified`
- `mfa_status`
- `last_permission_review`
- `status`

### 6.38 `Connectors`

- `connector_id` — primary key
- `source_platform_id`
- `destination_platform_id`
- `purpose`
- `permission_scope`
- `allowed_data_classes`
- `allowed_actions`
- `prohibited_actions`
- `rate_limit`
- `spend_limit`
- `expiration`
- `revocation_procedure`
- `permission_test_status`
- `functional_test_status`
- `security_test_status`
- `audit_reference`
- `status`

### 6.39 `Incidents`

- `incident_id` — primary key
- `detected_at`
- `incident_type`
- `severity`
- `affected_object_type`
- `affected_object_id`
- `privacy_class`
- `summary`
- `status`
- `containment_action`
- `owner`
- `notification_required`
- `recovery_status`
- `root_cause`
- `closed_at`

### 6.40 `Corrections`

- `correction_id` — primary key
- `proposed_at`
- `affected_object_type`
- `affected_object_id`
- `materiality`
- `reason`
- `corrected_text_or_action`
- `status`
- `approved_by`
- `approved_at`
- `propagation_scope`
- `propagation_complete_percent`
- `verification_reference`
- `completed_at`

Use `CorrectionTargets` to list every affected edition, campaign, repository, channel, and NFT record.

### 6.41 `Retirements`

- `retirement_id` — primary key
- `object_type`
- `object_id`
- `reason`
- `requested_at`
- `approved_by`
- `approved_at`
- `effective_at`
- `replacement_object_id`
- `customer_or_learner_impact`
- `archive_id`
- `status`

### 6.42 `FranchiseNodes`

- `franchise_node_id` — primary key
- `node_name`
- `human_owner`
- `node_level`
- `jurisdiction`
- `approved_products`
- `data_permissions`
- `brand_permissions`
- `audit_due_at`
- `incident_status`
- `succession_plan_reference`
- `status`

### 6.43 `Audits`

- `audit_id` — primary key
- `object_type`
- `object_id`
- `audit_type`
- `auditor`
- `started_at`
- `completed_at`
- `scope`
- `findings_summary`
- `critical_findings`
- `corrective_actions`
- `status`
- `next_audit_due_at`

### 6.44 `Archives`

- `archive_id` — primary key
- `object_type`
- `object_id`
- `archive_location`
- `content_hash`
- `privacy_class`
- `retention_class`
- `restore_procedure`
- `restore_tested_at`
- `status`

### 6.45 `AuditEvents`

- `audit_event_id` — primary key
- `event_timestamp`
- `actor_type`
- `actor_id`
- `action`
- `object_type`
- `object_id`
- `previous_state`
- `new_state`
- `reason`
- `source_platform_id`
- `privacy_class`
- `correlation_id`

Audit events are append-only. Corrections create new events rather than rewriting prior events.

### 6.46 `QualityEvidencePackets`

- `quality_packet_id` — primary key
- `object_type`
- `object_id`
- `certification_target`
- `requirements_complete_percent`
- `test_pass_percent`
- `critical_defects_open`
- `noncritical_defects_open`
- `risk_gate`
- `critical_gates_pass`
- `quality_score`
- `reviewer_summary`
- `human_approval_status`
- `decision`
- `created_at`
- `supersedes_quality_packet_id`

## 7. Junction and link tables

Required relationship tables include:

- `ModuleProgramLinks` when a program belongs to multiple modules;
- `WorkPacketDependencyLinks`;
- `ArtifactSourceLinks`;
- `ClaimSourceLinks`;
- `ClaimProductVersionLinks`;
- `ProductCharacterLinks`;
- `CEIUEcosystemLinks`;
- `LearningObjectSkillLinks`;
- `LearningObjectAssessmentLinks`;
- `CampaignAffiliateLinks`;
- `CorrectionTargets`;
- `FranchiseNodeProductLinks`;
- `ConnectorWorkPacketLinks`.

Every link table uses a unique link ID, both foreign keys, relationship type, effective date, expiration date, status, and audit reference.

## 8. Canonical enumerations

### 8.1 Privacy class

- `public`
- `internal`
- `confidential`
- `restricted`

### 8.2 Model line

- `chatgpt_business`
- `gemini_notebooklm`
- `claude_fabric_hermes`
- `human_editorial`
- `comparison`
- `merged_premium`
- `not_applicable`

### 8.3 Truth label

- `VF_verified_fact`
- `OA_official_assessment`
- `CT_corroborated_testimony`
- `AL_allegation`
- `WH_working_hypothesis`
- `FD_fictional_dramatization`
- `CX_contradicted`

### 8.4 Certification

- `Q0_idea`
- `Q1_structured_draft`
- `Q2_evidence_mapped`
- `Q3_testable_pilot`
- `Q4_certified_product`
- `Q5_production_proven`
- `Q6_franchise_replicable`
- `Q7_continuum_stewarded`

### 8.5 RiskGate

- `green`
- `yellow`
- `orange`
- `red`

### 8.6 Gate status

- `not_started`
- `in_review`
- `pass`
- `conditional`
- `fail`
- `not_applicable`
- `expired`
- `revoked`

### 8.7 General lifecycle status

- `idea`
- `draft`
- `ready`
- `active`
- `blocked`
- `under_review`
- `approved`
- `published`
- `paused`
- `quarantined`
- `rejected`
- `withdrawn`
- `superseded`
- `retired`
- `archived`

Each table may restrict this list to a defined state machine.

## 9. State machines

### 9.1 Work packet

`backlog → ready → active → blocked | under_review → completed → archived`

Alternate terminal states:

`cancelled`, `superseded`, `quarantined`.

### 9.2 Product and CEIU

`idea → structured_draft → evidence_mapped → testable_pilot → certified_product → production_proven → franchise_replicable → continuum_stewarded`

Side states:

`quarantined`, `suspended`, `superseded`, `retired`.

### 9.3 Product version

`draft → under_review → approved → published → paused | withdrawn → superseded → retired`

### 9.4 Model-line edition

`not_started → researching → drafting → qa → approved | rejected → superseded`

Comparison may begin only when required independent editions are `approved` and have valid source manifests and quality packets.

### 9.5 Claim

`captured → sourced → corroborated | contradicted | unresolved → approved_for_publication | blocked → corrected | retired`

### 9.6 Requirement

`proposed → approved → implementing → test_ready → verified | failed → superseded | retired`

### 9.7 Defect

`new → triaged → assigned → fixing → verification → closed`

Side states:

`deferred`, `duplicate`, `not_reproducible`, `accepted_risk`, `reopened`.

### 9.8 Risk

`identified → analyzed → mitigating → monitored → closed`

Alternate treatment states:

`accepted`, `avoided`, `transferred`, `escalated`.

### 9.9 Gate

`not_started → in_review → pass | conditional | fail | not_applicable`

A pass may later become `expired` or `revoked`.

### 9.10 Approval

`not_requested → pending → approved | rejected → expired | revoked`

### 9.11 Campaign

`draft → review → approved → scheduled → active → paused | corrected → withdrawn → archived`

### 9.12 Connector

`planned → configured → permission_tested → function_tested → security_reviewed → approved → active → suspended | revoked → retired`

### 9.13 Incident

`detected → triaged → contained → remediating → recovered → closed`

### 9.14 Correction

`proposed → reviewed → approved → propagating → completed → verified`

Alternate states:

`rejected`, `withdrawn`, `superseded`.

### 9.15 Franchise node

`N0_proposed → N1_registered → N2_sandbox → N3_pilot → N4_certified → N5_replication_ready → N6_mentor_node → N7_continuum_steward`

Side states:

`suspended`, `quarantined`, `revoked`, `retired`.

## 10. Access and privacy model

Every table and record receives:

- `privacy_class`;
- `workspace_scope`;
- `role_required`;
- `export_allowed`;
- `public_ai_allowed`;
- `slack_allowed`;
- `nft_metadata_allowed`;
- `blockchain_allowed`;
- `retention_class`;
- `redaction_required`;
- `audit_required`.

### Public

May be exported to approved public repositories, products, websites, or NFT metadata after rights and quality review.

### Internal

May be used inside authorized business and project workspaces; public export is blocked until review and redaction.

### Confidential

Limited to named roles and approved private systems; broad AI prompts, broad Slack channels, and public repositories are prohibited.

### Restricted

Private case-vault only. Public AI prompts, general collaboration channels, public repositories, blockchains, and NFT metadata are prohibited.

The spreadsheet prototype should contain only public data and synthetic or redacted internal examples.

## 11. Workbook implementation map

The Q3 `.xlsx` prototype should use these sheets or views:

1. `00_README`
2. `01_CURRENT_CHECKPOINT`
3. `02_DASHBOARD`
4. `03_MODULES_PROGRAMS`
5. `04_WORKSTREAMS_PACKETS`
6. `05_CONTINUATION_DECISIONS`
7. `06_PRODUCTS_VERSIONS`
8. `07_MODEL_LINE_EDITIONS`
9. `08_SOURCES_CLAIMS`
10. `09_CONTRADICTIONS`
11. `10_REQUIREMENTS_TESTS`
12. `11_DEFECTS_RISKS`
13. `12_GATES_APPROVALS`
14. `13_CHARACTERS_ECOSYSTEMS`
15. `14_CEIUS`
16. `15_LEARNING_SKILLS`
17. `16_BUILD_MEDIA_NFT`
18. `17_OFFERS_CAMPAIGNS`
19. `18_REVENUE_COSTS`
20. `19_DEVICES_PLATFORMS`
21. `20_CONNECTORS`
22. `21_INCIDENTS_CORRECTIONS`
23. `22_FRANCHISE_AUDITS`
24. `23_ARCHIVE_AUDIT_EVENTS`
25. `24_DATA_DICTIONARY`
26. `25_ENUMS_VALIDATION`
27. `26_IMPORT_EXPORT`
28. `27_VERSION_HISTORY`

For readability, related normalized tables may share a sheet as distinct Excel Tables. Every table retains its own primary key.

## 12. Formula and derived-field specification

### 12.1 Status score

Map work status to a numeric score:

- backlog or not started = 0.00
- ready = 0.10
- active = 0.50
- blocked = previous earned score but flagged
- under review = 0.85
- completed or approved = 1.00
- cancelled, rejected, superseded, retired = excluded from active completion calculations unless explicitly included

### 12.2 Weighted completion

```text
Weighted Completion % =
SUM(Task Weight × Status Score) / SUM(Active Task Weight)
```

### 12.3 Requirement coverage

```text
Requirement Coverage % =
Verified Requirements / Approved Active Requirements
```

### 12.4 Test pass rate

```text
Test Pass % =
Passed Tests / Executed Tests
```

### 12.5 Evidence coverage

```text
Evidence Coverage % =
Publication-Relevant Claims with at Least One Reviewed Supporting or Contextual Source
/ Total Publication-Relevant Claims
```

Claims marked `FD_fictional_dramatization` use fiction and rights review rather than factual-source coverage.

### 12.6 Independent model-line completion

```text
Model Independence % =
Approved Required Independent Editions / Required Independent Editions
```

Comparison and merged-premium rows are excluded from the denominator.

### 12.7 Critical gate pass

```text
Critical Gates Pass = TRUE only when every applicable critical gate is Pass or Not Applicable
```

`Conditional`, `Fail`, `Expired`, or `Revoked` returns FALSE.

### 12.8 Release eligibility

```text
Release Eligible =
Certification >= Q4
AND Critical Gates Pass
AND RiskGate <> Red
AND Open Critical Defects = 0
AND Human Approval = Approved and In Scope
AND Rights, Privacy, Security and Accessibility Requirements Satisfied
```

No score or forecast overrides this logic.

### 12.9 Overdue days

```text
Overdue Days = MAX(0, Today - Due Date)
```

Exclude completed, cancelled, superseded, retired, or archived work.

### 12.10 Stale checkpoint

```text
Checkpoint Age = Today - Current Packet Created Date
```

Flag after a configurable threshold or whenever current project state changed without a successor packet.

### 12.11 Risk score

```text
Risk Score = Likelihood × Impact
```

RiskGate is assigned by policy, not only the numeric product. Certain events automatically produce Red regardless of score.

### 12.12 Correction propagation

```text
Correction Propagation % =
Verified Corrected Targets / Total Required Correction Targets
```

A material correction remains open until 100% or an approved exception exists.

### 12.13 Net revenue

```text
Net Revenue = Gross Amount - Discounts - Refunds - Fees
```

### 12.14 Contribution margin

```text
Contribution Margin = Net Revenue - Direct Variable Costs
```

### 12.15 Forecast value

```text
Probability-Weighted Forecast = Expected Amount × Stated Probability
```

Forecasts must display assumptions and must not be represented as guaranteed revenue.

### 12.16 Budget variance

```text
Variance = Actual - Budget
Variance % = IF(Budget = 0, blank, Variance / Budget)
```

### 12.17 Quality score

A configurable 100-point score may summarize:

- purpose and value — 8
- evidence and truth — 12
- functional correctness — 10
- safety and abuse resistance — 10
- privacy and identity — 8
- cybersecurity — 8
- rights, legal, and medical controls — 8
- accessibility and usability — 8
- environmental responsibility — 6
- interoperability and maintainability — 6
- resilience and incident readiness — 6
- business and revenue integrity — 5
- provenance, correction, and retirement — 5

The score is informative only. Critical gates and Red RiskGate control release.

## 13. Dashboard requirements

### 13.1 Current Checkpoint dashboard

Show:

- current packet and status;
- current module, program, workstream, and work packet;
- highest-priority unblocked action;
- parallel human action;
- open blockers;
- RiskGate, certification, and critical gates;
- last update and packet age;
- authoritative issue, branch, pull request, and artifact links.

### 13.2 Product Factory dashboard

Show:

- products by certification level;
- inventory status;
- products blocked by critical gates, defects, rights, or approval;
- planned and completed media editions;
- corrections and retirements;
- Q3-to-Q4 conversion queue.

### 13.3 Model-Line dashboard

Show independent ChatGPT, Gemini/NotebookLM, and Claude/Hermes state separately, including source manifests, QA, approvals, comparison eligibility, and source-dependence warnings.

### 13.4 Evidence dashboard

Show claims by truth label, evidence coverage, stale claims, unresolved contradictions, sources by independence group, and publication blocks.

### 13.5 Quality and Risk dashboard

Show critical gate failures, Red and Orange risks, open critical defects, overdue tests, expiring approvals, incidents, and correction propagation.

### 13.6 Learning dashboard

Show learning objects by level and domain, skill coverage, assessment state, accessibility status, learner evidence using anonymized references, mentor reviews, and credential status.

### 13.7 Business dashboard

Show offers, campaigns, assumptions, costs, revenue, refunds, support burden, contribution margin, forecast versus actual, and integrity disclosures.

### 13.8 Device and Connector dashboard

Show security-review state, backup and restore evidence, permission tests, connector state, expirations, revocations, incidents, and approved data classes.

### 13.9 Franchise dashboard

Show node level, approved products, audit status, incidents, corrections, succession plans, and certification blocks.

## 14. Mobile views

The workbook should provide simplified mobile-readable views:

- `MOBILE_CURRENT`
- `MOBILE_NEXT_ACTIONS`
- `MOBILE_RELEASE_BLOCKS`
- `MOBILE_PRODUCT_STATUS`
- `MOBILE_INCIDENTS`
- `MOBILE_REVENUE_SUMMARY`

Mobile views are read-focused. Complex data editing remains desktop-oriented unless a validated mobile form is provided.

## 15. Data validation

Use controlled lists for:

- status;
- certification level;
- RiskGate;
- privacy class;
- model line;
- truth label;
- severity;
- priority;
- gate name and status;
- approval type and status;
- product type;
- media type;
- environment type;
- learning level;
- currency;
- connector state;
- incident state;
- correction state;
- franchise node level.

Reject or flag unknown enumeration values rather than silently accepting them.

## 16. Conditional formatting

Use accessible cues, not color alone.

- Red RiskGate or failed critical gate: red fill plus `STOP` text.
- Orange risk: orange fill plus `PILOT/QUARANTINE` text.
- Yellow risk: yellow fill plus `CONDITIONAL` text.
- Green risk: green fill plus `ELIGIBLE FOR REVIEW` text.
- Overdue: date and `OVERDUE` label.
- Missing evidence: warning icon or text.
- Human approval pending: `HUMAN APPROVAL REQUIRED`.
- Restricted data: `RESTRICTED — DO NOT EXPORT`.
- Model-line copying concern: `INDEPENDENCE REVIEW`.

## 17. Import and export contract

### Imports

- one CSV per table;
- JSON bundles using stable IDs;
- existing Prompt #11 example JSON files;
- GitHub issue and pull-request metadata;
- source manifests;
- approved redacted campaign and business records;
- device and connector inventory without secret values.

### Exports

- filtered CSV per table;
- public JSON product manifest;
- Continuation Packet JSON;
- GitHub work-packet Markdown;
- Slack notification summary linking to canonical records;
- NotebookLM source manifest;
- QEP summary;
- correction-propagation report;
- public NFT metadata subset;
- future Tower Control API payload.

Every export applies privacy, rights, approval, and destination checks.

## 18. GitHub mapping

| Ledger object | GitHub object |
|---|---|
| Work packet | Issue |
| Implementation | Feature branch |
| Review | Pull request |
| Versioned artifact | File and commit |
| Approved release | Tag or release |
| Defect | Issue with defect ID |
| Decision | Issue or decision record linked from packet |
| Correction | Correction issue and commit |
| Retirement | Retirement issue and archive record |
| Audit event | Commit, issue event, workflow record, or append-only log |

GitHub is a version and collaboration layer. It does not replace confidential case-vault storage or financial accounting systems.

## 19. Slack mapping

Slack receives only:

- packet ID;
- issue or pull-request link;
- requested action;
- owner;
- privacy class;
- due condition;
- status;
- correction or incident notice when authorized.

Decisions, approvals, and evidence must be written back to the canonical ledger or linked GitHub record.

## 20. NotebookLM and model-line mapping

Each independent model-line edition records:

- edition ID;
- work-packet ID;
- model line;
- source manifest;
- source independence groups;
- output artifact;
- omissions and uncertainties;
- contradiction report;
- QA packet;
- approval status;
- comparison eligibility.

No model line imports another line’s first-pass conclusions before its own first pass is complete.

## 21. Audit and version policy

- `created_at`, `created_by`, `updated_at`, and `updated_by` exist on every implementation table even when omitted from the minimum field list above.
- Approved rows are not deleted; they are superseded, corrected, quarantined, retired, or archived.
- State changes create `AuditEvents`.
- Sensitive changes require a reason and reviewer.
- Formula, validation, and dashboard changes are versioned.
- Spreadsheet structure changes update the data dictionary and migration map.

## 22. Migration plan

### Phase 1 — Inventory

List existing Prompt #11 modules, schemas, examples, issues, pull requests, products, pilots, and model-line repositories.

### Phase 2 — Crosswalk

Map existing fields to MEPL entities and enumerations. Record unmapped fields rather than discarding them.

### Phase 3 — Privacy and rights review

Remove secrets and restricted personal evidence. Assign privacy and rights status.

### Phase 4 — Identifier assignment

Assign stable IDs and preserve existing canonical IDs where compatible.

### Phase 5 — Deduplication

Identify duplicates by canonical reference, content hash, title, source, date, and independence group. Merge only with documented review.

### Phase 6 — Core import

Import modules, programs, workstreams, work packets, continuation packets, products, versions, sources, claims, quality records, and issues.

### Phase 7 — Extended import

Import CEIUs, learning objects, media, business experiments, devices, connectors, incidents, corrections, franchises, and archives.

### Phase 8 — Reconciliation

Run missing-key, orphan-record, enumeration, privacy, source, gate, and model-line-independence checks.

### Phase 9 — Dashboard and Q3 review

Generate dashboards, sample reports, Quality Evidence Packet, limitations, and Q3 decision.

### Phase 10 — Database option

Migrate to a normalized database using stable IDs and audit rules only after the spreadsheet prototype has proven the workflow.

## 23. Q3 prototype acceptance criteria

The workbook must:

- open without repair warnings;
- contain the required sheets and Excel Tables;
- have frozen headers, filters, usable widths, clear instructions, and accessible labels;
- use stable IDs and controlled validation lists;
- maintain separate model-line records;
- block or visibly flag release when critical controls fail;
- show the Current Checkpoint and next action on the first operational view;
- include sample records from current Prompt #11 work;
- contain no secrets or restricted personal records;
- produce traceable dashboard metrics;
- include a data dictionary, version history, correction log, and known-limitations section;
- export selected public tables to CSV or JSON;
- pass manual formula, reference, accessibility, privacy, and visual QA;
- include a Quality Evidence Packet.

## 24. Completion boundary

This document defines the data model. It does not claim that the `.xlsx` workbook, production database, APIs, connectors, dashboards, imports, exports, accounting integration, payment integration, or live automations are implemented.

The next work packet is **WP-OMNI-0006 / issue #11 — Build the Q3 $7 Master Evidence and Product Ledger prototype** after this model reaches review-ready status.
