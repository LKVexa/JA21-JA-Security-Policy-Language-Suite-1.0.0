# JA21 JA Security Policy Technical Corpus Guide

## Scope

This corpus contains **10,000 normalized JA Security Policy Language records**. Each record preserves source, semantic interpretation, typed AST, compiler representation, R12 lowering, modeled policy-runtime evidence, MCRT identity, validation expectation, optimization notes, and Smithson 8S annotations.

## Evidence boundary

The corpus specifies expected behavior. It does not prove that a native parser, compiler, proof checker, policy engine, sandbox, audit sink, or certificate signer executed a program. Native evidence must be recorded separately with tool identity, command, input hashes, output hashes, sandbox settings, and replay results.

## Navigation

Begin with `record_id`, `feature`, `level`, and `validation_class`. Verify `source_sha256`, then follow the semantic judgment into the typed AST, R12 record, policy decision, runtime expectation, and MCRT receipt. The 1,000-script catalog points to curated source examples.

## Publication principles

1. Deny and require rules are first-class—not comments around allow rules.
2. Capabilities are explicit, attenuated, revocable, and scope-bound.
3. Secret values never appear in source, diagnostics, traces, or receipts.
4. Network and process execution fail closed without declared authority.
5. Static proofs and runtime enforcement complement rather than replace each other.
6. Optimization preserves decision precedence, auditability, revocation, and explanation.
7. Modeled evidence, structural validation, native execution, and certification remain distinct.
