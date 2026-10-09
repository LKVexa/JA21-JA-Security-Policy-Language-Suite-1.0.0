# JA21 JA Security Policy Language Suite 1 0 0 main Updated Corpus Audit

This updated copy supplies explicit rights, default deny, redaction and revocation. Its import boundary is: Use corrected no-leak invariant; execute policy engine denial tests before admission.

## Source and coverage

Original input: `JA21-JA-Security-Policy-Language-Suite-1.0.0-main.zip`. Source SHA 256: `8ccaccd58ee29681e860805c9ddbd476521be616b5863a5178019054dd242f30`. The source archive is preserved in the parent folder. All 1,070 original leaf files were read and hashed; 31,072 stored JSONL rows were structurally parsed, including historical/reconstructed copies. Nested ZIPs are materialized in `.expanded` directories. Dataset row counts include duplicate representations and metadata headers; they are not unique executable programs.

Original checks and locations are in [the source manifest](audit/source_manifest.json). Current payload bytes are in [the updated manifest](audit/updated_manifest.json), and changes are in [the ledger](audit/change_ledger.json). Embedded source layers have [separate coverage](audit/embedded_layer_coverage.json). Historical hashes and modeled labels retain their historical meaning. The updated manifest and qualification sidecars govern this release.

## Upgrades and open implementation work

### JA-09 High priority

Passing examples asserted secret_leak=true while intended failure examples asserted false. All 10,000 current assertions now use the corrected polarity, with hashes and qualifications refreshed.

Status: **applied_source_or_tool_repair_and_qualified**. Security leak assertion polarity repair

Evidence: `JA21_JASEC_Suite_1.0.0/corpus/technical/JA21_JASEC_TECHNICAL_CORPUS_10000.jsonl.gz | JA21_JASEC_Suite_1.0.0/specification/LANGUAGE_SPECIFICATION.md`.

Remaining gate: A complete versioned profile parser, semantic inference and target/runtime conformance are needed before native admission.

### BASE-16 Medium priority

Nested packaging, raw modeled labels and historical copies need explicit current provenance and reuse boundaries.

Status: **APPLIED**. Expanded materialized payload; source and updated manifests; change ledger; dataset-bound qualification; individual audit and fabric role.

Evidence: `audit/source_manifest.json | audit/updated_manifest.json | audit/dataset_qualification.json`.

Remaining gate: Use corrected no-leak invariant; execute policy engine denial tests before admission.

## Contribution to the new fabric language

Profile owner: `ja.security`. Explicit rights, default deny, redaction and revocation. Use corrected no-leak invariant; execute policy engine denial tests before admission.

The [adapter contract](audit/fabric_adapter_contract.json) is a proposed interface with executable_adapter_implemented=false. It preserves source authority rather than using a feature label as inferred semantics. See [the collection architecture](../../fabric_language/ARCHITECTURE.md) and the [8S foundation](../../fabric_language/profiles/coupling8s/PROFILE.md).

## Qualification and verification

Use [dataset qualifications](audit/dataset_qualification.json) before training, importing or treating a record as evidence. A modeled pass or a structural validator pass is not native execution, authenticated federation, race proof, or physical device evidence. Current JA and DeepML technical records carry additional qualifications; deliberate negative examples remain negative examples.

The release provides an offline integrity checker: run `python tools/verify_release.py --deep` from the collection root. Per-profile test reports and validators qualify the exact behavior they checked. Complete grammars, native adapters, authenticated transports and a bootable unikernel remain separately tracked implementation gates.
