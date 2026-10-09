# Secret-leak invariant polarity errata

The original 7,500 modeled-pass records asserted `policy.secret_leak == true`; 2,500 intentionally failing records asserted `false`, despite the specification requiring secret redaction and fail-closed enforcement. The updated sources reverse that polarity. A detected leak can no longer be the passing invariant.

The change is applied to all 10,000 current records, 1,000 selected scripts, current catalogs/indexes, 64 conformance references, and current handbook source examples. Old/new hashes are recorded in SECRET_LEAK_AUDIT_CORRECTIONS.jsonl. Qualifications were recomputed from the updated source; no source-hash conflicts remain. Original archives and historical reference sources are preserved.

This is a source invariant repair and a metadata consistency check. It does not execute a policy engine, sandbox, audit sink, or signer. Existing modeled AST, semantic, R12, and MCRT identities need revalidation against the corrected source.
