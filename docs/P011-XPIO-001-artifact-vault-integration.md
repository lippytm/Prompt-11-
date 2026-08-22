# P-011-XPIO-001 Artifact Vault Integration

`P011-ARTIFACT-VAULT-001` converts the generated downloads into governed build inputs.

## Current inventory

- 54 registered download aliases
- 51 unique SHA-256 content objects
- 3 exact duplicate aliases
- 3 vault parts

## Vault parts

1. Architecture and continuity
2. MEPL data and quality
3. Clone evolution and ethical revenue

## Operational use

An artifact may be used only after:

1. hash verification;
2. privacy and rights review;
3. linkage to a work packet;
4. status and version review;
5. applicable tests;
6. correction and supersession check;
7. release-gate evaluation.

## Deduplication

Exact duplicates receive the same artifact ID and different alias records. This preserves the user's download names while preventing duplicate inventory and false progress counts.

## Product status

`registered_build_input` means the file is available to the building process. It does not mean Q4, approved inventory, commercial release, deployment, or factual certification.

## Storage boundary

The canonical repository stores the complete alias-and-hash manifest, human-readable register, source code, tests, and Quality Evidence Packet. The binary vault parts are distributed in the signed Q2 delivery package because the connected GitHub text-file interface cannot upload binary release assets. Their filenames, sizes, and SHA-256 hashes remain recorded in the manifest.
