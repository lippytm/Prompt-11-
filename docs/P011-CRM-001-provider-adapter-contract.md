# P-011-CRM-001 — Provider Adapter Contract

A provider adapter connects an approved external system to the canonical Prompt #11 CRM model. The adapter does not redefine identity, consent, quality, or release authority.

## Candidate adapter families

- HubSpot or another CRM platform;
- Airtable or another operational database;
- Gmail or approved email provider;
- Slack;
- forms and websites;
- ManyChat, BotBuilders, or another messaging platform;
- GitHub;
- lippytmai.zo.computer;
- payment or accounting reference systems;
- future approved providers.

## Required Adapter Passport

- adapter ID and version;
- human owner;
- exact business and user purpose;
- source and destination;
- direction: inbound, outbound, or bidirectional;
- field map and stable-ID map;
- minimum API or application scopes;
- permitted privacy classes;
- prohibited data classes;
- consent, suppression, and deletion behavior;
- identity conflict and duplicate policy;
- idempotency key and retry behavior;
- freshness and synchronization interval;
- rate, cost, and computational-credit limit;
- audit and correlation logging;
- validation and test evidence;
- failure and quarantine behavior;
- backup, rollback, shutdown, and revocation;
- incident and correction routes;
- retention and retirement;
- required gates and HumanApprovalGate.

## Data-routing rules

1. Route only the minimum fields needed for the declared purpose.
2. Do not broadcast confidential or restricted data to multiple AI systems.
3. Tokenize or redact contact details where full values are unnecessary.
4. Preserve provider record IDs as external references; Prompt #11 stable IDs remain canonical.
5. Record source, timestamp, model line, adapter version, and correlation ID.
6. Do not silently overwrite a newer approved value.
7. Quarantine unresolved identity or consent conflicts.
8. Propagate suppression and correction before further outreach.
9. Do not treat a successful API response as proof of a successful customer outcome.
10. Do not mark an adapter operational until permission, test, monitoring, rollback, shutdown, and revocation evidence exists.

## Conflict policy

Conflicts are classified as:

- identity;
- contact preference;
- consent or suppression;
- journey stage;
- learning or support status;
- opportunity or attribution;
- correction or retention;
- technical version.

Consent, suppression, legal rights, and security restrictions use the most protective valid state until a human resolves the conflict.

## Adapter certification

- **A0 Proposed** — idea only;
- **A1 Documented** — passport and field map complete;
- **A2 Sandbox** — synthetic tests and failure handling complete;
- **A3 Pilot** — bounded real-world test with monitoring and revocation;
- **A4 Certified** — all critical gates and HumanApprovalGate passed;
- **A5 Monitored** — ongoing drift, permission, cost, and incident review;
- **A6 Retired** — disabled, credentials revoked, records corrected or archived.

The current Q2 module defines the contract but does not certify a live provider adapter.