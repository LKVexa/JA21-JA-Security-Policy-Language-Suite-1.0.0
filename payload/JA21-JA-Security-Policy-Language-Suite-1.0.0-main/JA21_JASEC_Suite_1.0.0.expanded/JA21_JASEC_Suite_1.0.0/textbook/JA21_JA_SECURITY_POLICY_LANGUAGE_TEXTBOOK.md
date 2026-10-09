# JA21 JA Security Policy Language Textbook
## Identity, Authority, Enforcement, Audit, and Evidence

**Edition:** 1.0.0  
**Suite:** JA21 JA Security Policy Language Suite  
**Extension:** `.jasec`  
**Evidence status:** corpus-modeled unless a separate native report is supplied.

## Preface

This textbook turns the uploaded JA Security Policy Language corpus into a coherent course of study. It treats identity, authorization, delegation, revocation, classification, secrets, sandboxes, proof, runtime enforcement, audit, and certification as typed language concerns. The 10,000-record corpus is the technical reference; the 1,000-program pack is the laboratory library; this book supplies the conceptual sequence and review discipline.

The five analytical roles are used throughout. **SOPHIA** examines semantic and systemic coherence. **CHARLOTTE** examines policy information architecture and explanation quality. **LANDON** examines compiler, proof checker, runtime, sandbox, and replay feasibility. **Professor** examines pedagogy, counterexamples, and proof obligations. **Podium** examines publication, release integrity, limitations, and certification readiness.

## Contents

1. Security Policy as a Language Suite
2. Program Anatomy, Modules, and No-Network Policy
3. Principals, Identities, Groups, and Roles
4. Resources, Classification, and Scope
5. Capabilities and Least Authority
6. Allow, Deny, and Require Rules
7. Conflict Resolution and Policy Composition
8. Explanation and Human Approval
9. Delegation and Attenuation
10. Revocation and Time-Bound Permission
11. Agent, Tool, and Model Access Policies
12. Secrets, Redaction, and Evidence Hygiene
13. Network and Process Sandboxes
14. Retention and Deletion Rules
15. Audit Rules and Immutable Decision History
16. Fail-Closed Policy and Recovery
17. Compiler Frontend and Typed Policy AST
18. Static Proofs and Policy Verification
19. Runtime Enforcement and Deterministic Replay
20. Optimization Without Security Drift
21. R12, MCRT, Certification, and Smithson 8S
22. Standalone JA Security Policy Toolchain Capstone

# Chapter 1: Security Policy as a Language Suite

## Learning objectives

- Explain policy programs as evidence-bearing authorization systems across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that source, judgment, enforcement, and receipt remain connected.
- Construct a positive case and a minimal counterexample involving treating policy as scattered configuration.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **policy programs as evidence-bearing authorization systems** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **source, judgment, enforcement, and receipt remain connected**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **treating policy as scattered configuration**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00008`  
**Feature:** `policy_composition`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `5a7d87c55b83181fe92a73d1d2c6399e38c3ad498d91623e97717f08dd8de3eb`

```jasec
ja source 0.3
module corpus.ja_security.example_00008
use Security
policy no_network

principal WorkerJASEC_00008
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport10 classification restricted
policy PolicyJASEC_00008 {
    deny network.* by default
    allow ModelExport10 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00008.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-0e5f29c7bfe177a5b2b9`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-4aa1d31f6978b1b64174 : PolicyDecision ! {state.read} ⇒ validated`
- AST node: `node-4aa1d31f6978b1b64174` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.read`
- Capabilities: `ledger.append`
- Semantic operator: `allow`
- Policy decision: `allow`
- R12 record: `r12-73b34f60a69ad485eb3c`
- MCRT record: `mcrt-987355ba8aac8fe205b1`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Assemble a minimal policy suite and evidence map.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 2: Program Anatomy, Modules, and No-Network Policy

## Learning objectives

- Explain source identity, module boundaries, and default-deny execution across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every decision executes in a named module and declared policy context.
- Construct a positive case and a minimal counterexample involving implicit authority inherited from the host.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **source identity, module boundaries, and default-deny execution** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **every decision executes in a named module and declared policy context**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **implicit authority inherited from the host**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00032`  
**Feature:** `principal`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `e9be4e50f703ec81965d4b83651980e7849fcc49c1e70aa645081392775badbb`

```jasec
ja source 0.3
module corpus.ja_security.example_00032
use Security
policy no_network

principal WorkerJASEC_00032
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport34 classification restricted
policy PolicyJASEC_00032 {
    deny network.* by default
    allow ModelExport34 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00032.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-09b8b2f2452f91a7e1f5`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-e1f23a18cd9d9f02c9bf : PolicyDecision ! {ledger.append} ⇒ validated`
- AST node: `node-e1f23a18cd9d9f02c9bf` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `ledger.append`
- Capabilities: `ledger.append`
- Semantic operator: `principal_declare`
- Policy decision: `allow`
- R12 record: `r12-d2aec23851f8ad10d892`
- MCRT record: `mcrt-d9ff1b971bfab12cb2ca`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Compare a valid module with an undeclared-authority variant.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 3: Principals, Identities, Groups, and Roles

## Learning objectives

- Explain stable subject identity and role assignment across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that identity resolution is deterministic and auditable.
- Construct a positive case and a minimal counterexample involving ambiguous or mutable identity aliases.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **stable subject identity and role assignment** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **identity resolution is deterministic and auditable**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **ambiguous or mutable identity aliases**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00311`  
**Feature:** `identity`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `0919e7b08ffd4b3806253dca155ed214d00ac7151967995f024b53ee6357ab56`

```jasec
ja source 0.3
module corpus.ja_security.example_00311
use Security
policy no_network

principal WorkerJASEC_00311
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport22 classification restricted
policy PolicyJASEC_00311 {
    deny network.* by default
    allow ModelExport22 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00311.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-bc5ad11c6b3278c6b1cb`
- Judgment: `Environment; Policy; {secret.reference} ⊢ node-eb2cc60d3ee9be80bb58 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-eb2cc60d3ee9be80bb58` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `secret.reference`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-32eb0ac058cfad4e5afe`
- MCRT record: `mcrt-ff67cf698a423520b670`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Build an identity graph and detect conflicting membership.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 4: Resources, Classification, and Scope

## Learning objectives

- Explain typed resources, classification labels, and bounded scope across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that authority is evaluated against exact resource identity and classification.
- Construct a positive case and a minimal counterexample involving wildcard scope that bypasses classification.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **typed resources, classification labels, and bounded scope** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **authority is evaluated against exact resource identity and classification**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **wildcard scope that bypasses classification**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00171`  
**Feature:** `data_classification`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `543d255b1e5e026a9fb9f0130759a3c6a0ca610fe4365288769b8aff5949eb58`

```jasec
ja source 0.3
module corpus.ja_security.example_00171
use Security
policy no_network

principal WorkerJASEC_00171
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport76 classification restricted
policy PolicyJASEC_00171 {
    deny network.* by default
    allow ModelExport76 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00171.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-ad032ff0177659003640`
- Judgment: `Environment; Policy; {delegation.issue:bounded} ⊢ node-c1469416ede113393a23 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-c1469416ede113393a23` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `delegation.issue:bounded`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-a775a18fd9d3358effc1`
- MCRT record: `mcrt-39bba05fa250381ba1df`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Design a resource lattice and scope tests.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 5: Capabilities and Least Authority

## Learning objectives

- Explain capability requirements and least-privilege admission across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every privileged effect has an explicit capability.
- Construct a positive case and a minimal counterexample involving ambient authority and capability inference from names.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **capability requirements and least-privilege admission** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **every privileged effect has an explicit capability**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **ambient authority and capability inference from names**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00028`  
**Feature:** `capability`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `ff365d88e42bb3fae6f4d01ad39ea69abc68d95d11671203a94e9ca11789df42`

```jasec
ja source 0.3
module corpus.ja_security.example_00028
use Security
policy no_network

principal WorkerJASEC_00028
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport30 classification restricted
policy PolicyJASEC_00028 {
    deny network.* by default
    allow ModelExport30 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00028.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-d610bd35909225138184`
- Judgment: `Environment; Policy; {approval.verify} ⊢ node-acc15c7cf23e532fb7d7 : PolicyDecision ! {state.read} ⇒ validated`
- AST node: `node-acc15c7cf23e532fb7d7` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.read`
- Capabilities: `approval.verify`
- Semantic operator: `allow`
- Policy decision: `allow`
- R12 record: `r12-775f20ac24a4aec0e551`
- MCRT record: `mcrt-9f6d3c4412e26b8210db`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Construct capability admission and rejection cases.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 6: Allow, Deny, and Require Rules

## Learning objectives

- Explain decision rules and ordered evaluation across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that explicit deny and mandatory requirements cannot be erased by permissive rules.
- Construct a positive case and a minimal counterexample involving first-match logic that hides conflicts.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **decision rules and ordered evaluation** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **explicit deny and mandatory requirements cannot be erased by permissive rules**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **first-match logic that hides conflicts**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00024`  
**Feature:** `deny_rule`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `68540d4650d6ce8800a02bf1ad4f6038f0b8f8271cc1af2175bb3b361faa4ac7`

```jasec
ja source 0.3
module corpus.ja_security.example_00024
use Security
policy no_network

principal WorkerJASEC_00024
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport26 classification restricted
policy PolicyJASEC_00024 {
    deny network.* by default
    deny ModelExport26 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00024.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-77deae13226f6f67c33f`
- Judgment: `Environment; Policy; {policy.enforce} ⊢ node-bd14f48946cf95504e97 : PolicyDecision ! {secret.read} ⇒ validated`
- AST node: `node-bd14f48946cf95504e97` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `secret.read`
- Capabilities: `policy.enforce`
- Semantic operator: `require`
- Policy decision: `allow`
- R12 record: `r12-67a79d873255e89ad8fb`
- MCRT record: `mcrt-1f4d5ae4b7e121cd471b`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Compare ordered rule sets and decision traces.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 7: Conflict Resolution and Policy Composition

## Learning objectives

- Explain safe composition, precedence, and deterministic outcomes across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that composed policies produce one explainable decision under a declared precedence profile.
- Construct a positive case and a minimal counterexample involving nondeterministic or circular precedence.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **safe composition, precedence, and deterministic outcomes** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **composed policies produce one explainable decision under a declared precedence profile**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **nondeterministic or circular precedence**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00241`  
**Feature:** `conflict_resolution`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `ff74b907f56557f3773ff040586924338a8a21a1dbadf026fc2d679bc89bb9ea`

```jasec
ja source 0.3
module corpus.ja_security.example_00241
use Security
policy no_network

principal WorkerJASEC_00241
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport49 classification restricted
policy PolicyJASEC_00241 {
    deny network.* by default
    allow ModelExport49 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00241.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-53cb5c0e8eeb6e87eec7`
- Judgment: `Environment; Policy; {policy.evaluate} ⊢ node-46ddadee9dfffcd71521 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-46ddadee9dfffcd71521` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `policy.evaluate`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-51930679b4e129c1c5c4`
- MCRT record: `mcrt-d0ea761484af45c62849`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Compose two policies and prove their conflict outcome.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 8: Explanation and Human Approval

## Learning objectives

- Explain decision explanations and approval gates across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that high-risk effects require a recorded human decision when declared.
- Construct a positive case and a minimal counterexample involving approval after the effect or explanation without evidence.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **decision explanations and approval gates** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **high-risk effects require a recorded human decision when declared**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **approval after the effect or explanation without evidence**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00026`  
**Feature:** `human_approval`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `5db1b8fc18ba6052c8dda4e431b5d40f9a34327843dd62975c1d4cb17c816201`

```jasec
ja source 0.3
module corpus.ja_security.example_00026
use Security
policy no_network

principal WorkerJASEC_00026
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport28 classification restricted
policy PolicyJASEC_00026 {
    deny network.* by default
    allow ModelExport28 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00026.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-ced862e674926ff9c424`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-b522b883ac34e3d08bc1 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-b522b883ac34e3d08bc1` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `ledger.append`
- Semantic operator: `authorize`
- Policy decision: `allow`
- R12 record: `r12-b15494f03f27587b488a`
- MCRT record: `mcrt-dd7f7e1727cf8323bb34`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Build an approval packet and denial witness.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 9: Delegation and Attenuation

## Learning objectives

- Explain bounded transfer of authority across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that delegated authority is a subset of the delegator authority.
- Construct a positive case and a minimal counterexample involving delegation that widens resource, action, or time scope.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **bounded transfer of authority** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **delegated authority is a subset of the delegator authority**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **delegation that widens resource, action, or time scope**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00221`  
**Feature:** `delegation`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `b24ec76a4791d9c4c54b73879e7e6585f768580968f261a28378c83b301c872c`

```jasec
ja source 0.3
module corpus.ja_security.example_00221
use Security
policy no_network

principal WorkerJASEC_00221
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport29 classification restricted
policy PolicyJASEC_00221 {
    deny network.* by default
    allow ModelExport29 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00221.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-446ead075dd2f9427b4a`
- Judgment: `Environment; Policy; {secret.reference} ⊢ node-11c4d688e3228f51f56f : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-11c4d688e3228f51f56f` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `secret.reference`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-ae2199b3331d7323060f`
- MCRT record: `mcrt-025dd4bfe34707b2d270`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Construct a delegation chain and monotonicity proof.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 10: Revocation and Time-Bound Permission

## Learning objectives

- Explain authority lifecycle, expiry, and revocation across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that revoked or expired authority cannot authorize a new privileged effect.
- Construct a positive case and a minimal counterexample involving cached decisions that ignore lifecycle state.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **authority lifecycle, expiry, and revocation** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **revoked or expired authority cannot authorize a new privileged effect**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **cached decisions that ignore lifecycle state**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00251`  
**Feature:** `revocation`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `0a23dc323870c61198bc348d3b3640e36b272a4a19263f9843d09d7ce7e86950`

```jasec
ja source 0.3
module corpus.ja_security.example_00251
use Security
policy no_network

principal WorkerJASEC_00251
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport59 classification restricted
policy PolicyJASEC_00251 {
    deny network.* by default
    allow ModelExport59 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00251.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-8a360d3222b21fb94006`
- Judgment: `Environment; Policy; {secret.reference} ⊢ node-c3b82fefac17568c157e : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-c3b82fefac17568c157e` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `secret.reference`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-c6e2f04aa5e149d1dbe1`
- MCRT record: `mcrt-f883be12ce563890643f`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Test revocation and expiry at decision boundaries.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 11: Agent, Tool, and Model Access Policies

## Learning objectives

- Explain governed access for agents, tools, and models across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that autonomous components receive only explicit task-bound authority.
- Construct a positive case and a minimal counterexample involving tool invocation or model export through broad inherited roles.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **governed access for agents, tools, and models** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **autonomous components receive only explicit task-bound authority**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **tool invocation or model export through broad inherited roles**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00181`  
**Feature:** `agent_policy`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `d1be8eadd7c848b89a93aacb684f2e10a4f65a7773da6160d0a11a28f8bc8e34`

```jasec
ja source 0.3
module corpus.ja_security.example_00181
use Security
policy no_network

principal WorkerJASEC_00181
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport86 classification restricted
policy PolicyJASEC_00181 {
    deny network.* by default
    allow ModelExport86 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00181.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-6989aedd03499f8abcfc`
- Judgment: `Environment; Policy; {policy.evaluate} ⊢ node-72f1e8ef152b369b3694 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-72f1e8ef152b369b3694` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `policy.evaluate`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-9d5245c1998a5cbfc447`
- MCRT record: `mcrt-be313c49189181061265`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Design agent/tool/model admission policies.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 12: Secrets, Redaction, and Evidence Hygiene

## Learning objectives

- Explain reference-only secrets and complete redaction across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that secret material never appears in source, diagnostics, logs, or MCRT records.
- Construct a positive case and a minimal counterexample involving embedding or echoing secret values.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **reference-only secrets and complete redaction** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **secret material never appears in source, diagnostics, logs, or MCRT records**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **embedding or echoing secret values**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00016`  
**Feature:** `secret_policy`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `9b59ed141532e3a18af69cd71afaf5a12be19318d15b06cfda258f62de0b3c82`

```jasec
ja source 0.3
module corpus.ja_security.example_00016
use Security
policy no_network

principal WorkerJASEC_00016
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport18 classification restricted
policy PolicyJASEC_00016 {
    deny network.* by default
    allow ModelExport18 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00016.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-55f15b644872630c8d5b`
- Judgment: `Environment; Policy; {approval.verify} ⊢ node-6848473d67c1f8d992ce : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-6848473d67c1f8d992ce` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `approval.verify`
- Semantic operator: `authorize`
- Policy decision: `allow`
- R12 record: `r12-38542493beb90e338f50`
- MCRT record: `mcrt-dfe269cf5e006fd39be0`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Construct a secret flow and redaction audit.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 13: Network and Process Sandboxes

## Learning objectives

- Explain explicit egress and process-execution boundaries across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that undeclared network and unknown-code execution fail closed.
- Construct a positive case and a minimal counterexample involving quiet fallback to host network or shell execution.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **explicit egress and process-execution boundaries** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **undeclared network and unknown-code execution fail closed**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **quiet fallback to host network or shell execution**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00012`  
**Feature:** `network_sandbox`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `206f43c4241937aac0751bf7e908a2c9d49fc3a4a40338f7731e2529d232febe`

```jasec
ja source 0.3
module corpus.ja_security.example_00012
use Security
policy explicit_network

principal WorkerJASEC_00012
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport14 classification restricted
policy PolicyJASEC_00012 {
    deny network.* by default
    deny ModelExport14 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00012.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-516dfe4e6a4bc9a83f46`
- Judgment: `Environment; Policy; {policy.enforce} ⊢ node-e6085bd7bb23fef26cdd : PolicyDecision ! {ledger.append} ⇒ validated`
- AST node: `node-e6085bd7bb23fef26cdd` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `ledger.append`
- Capabilities: `policy.enforce`
- Semantic operator: `principal_declare`
- Policy decision: `allow`
- R12 record: `r12-dcd1ce176b483b3c766c`
- MCRT record: `mcrt-3b8228ca23777b32a9e8`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Build sandbox admission and escape tests.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 14: Retention and Deletion Rules

## Learning objectives

- Explain data lifecycle, legal hold, retention, and deletion across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that retention and deletion decisions remain class-aware and auditable.
- Construct a positive case and a minimal counterexample involving deletion that ignores hold or retention rules.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **data lifecycle, legal hold, retention, and deletion** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **retention and deletion decisions remain class-aware and auditable**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **deletion that ignores hold or retention rules**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00002`  
**Feature:** `retention_rule`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `80d733fe7cac9fba7b7302b09786466574712ada853c21eea89da50bbf712575`

```jasec
ja source 0.3
module corpus.ja_security.example_00002
use Security
policy no_network

principal WorkerJASEC_00002
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport4 classification restricted
policy PolicyJASEC_00002 {
    deny network.* by default
    allow ModelExport4 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00002.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-b3e0ced85ac7d780338c`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-31fffe98c86612f5a20e : PolicyDecision ! {ledger.append} ⇒ validated`
- AST node: `node-31fffe98c86612f5a20e` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `ledger.append`
- Capabilities: `ledger.append`
- Semantic operator: `principal_declare`
- Policy decision: `allow`
- R12 record: `r12-48bd792e9d2148dd4e21`
- MCRT record: `mcrt-60bb56050e89b7cb9c95`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Model a lifecycle transition and conflicting obligations.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 15: Audit Rules and Immutable Decision History

## Learning objectives

- Explain complete, tamper-evident privileged-decision history across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every privileged decision emits a stable, redacted receipt.
- Construct a positive case and a minimal counterexample involving best-effort logging or mutable audit identity.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **complete, tamper-evident privileged-decision history** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **every privileged decision emits a stable, redacted receipt**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **best-effort logging or mutable audit identity**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00006`  
**Feature:** `audit_rule`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `563cc2ab8088ab9a517b3bc30ad3834d2ea6b70cb99cfd8b2a08df7de080b7a8`

```jasec
ja source 0.3
module corpus.ja_security.example_00006
use Security
policy no_network

principal WorkerJASEC_00006
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport8 classification restricted
policy PolicyJASEC_00006 {
    deny network.* by default
    allow ModelExport8 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00006.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-2a8d15410c297a3b6855`
- Judgment: `Environment; Policy; {policy.enforce} ⊢ node-2d3140f5b6ba4a744695 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-2d3140f5b6ba4a744695` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `policy.enforce`
- Semantic operator: `authorize`
- Policy decision: `allow`
- R12 record: `r12-3b9243ba3b2fb2915448`
- MCRT record: `mcrt-54f4c47086895e958700`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Construct and verify an audit chain.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 16: Fail-Closed Policy and Recovery

## Learning objectives

- Explain safe behavior under missing evidence, parser errors, and runtime failure across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that uncertainty or unavailable enforcement produces denial or explicit unresolved state.
- Construct a positive case and a minimal counterexample involving fail-open retry and silent default allow.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **safe behavior under missing evidence, parser errors, and runtime failure** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **uncertainty or unavailable enforcement produces denial or explicit unresolved state**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **fail-open retry and silent default allow**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00201`  
**Feature:** `fail_closed`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `2c5aac3d628241c8902eb512622ed77192bf3ba2e4b2e71d6696eb1141484a61`

```jasec
ja source 0.3
module corpus.ja_security.example_00201
use Security
policy no_network

principal WorkerJASEC_00201
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport9 classification restricted
policy PolicyJASEC_00201 {
    deny network.* by default
    allow ModelExport9 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00201.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-4241efdbd1b5ac9ae082`
- Judgment: `Environment; Policy; {delegation.issue:bounded} ⊢ node-0606c83afbb9d52c7129 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-0606c83afbb9d52c7129` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `delegation.issue:bounded`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-2f89a92c7efaa4acff9c`
- MCRT record: `mcrt-9704c149df1fc4a04fe5`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Simulate proof, network, and runtime failures.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 17: Compiler Frontend and Typed Policy AST

## Learning objectives

- Explain stable parsing, resolution, typing, and proof obligations across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that source spans, types, effects, capabilities, and policy decisions remain inspectable.
- Construct a positive case and a minimal counterexample involving generic errors that hide rejected authority.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **stable parsing, resolution, typing, and proof obligations** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **source spans, types, effects, capabilities, and policy decisions remain inspectable**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **generic errors that hide rejected authority**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00191`  
**Feature:** `static_proof`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `70523409747706ad169ea4651ee481a045e27aa8c971e591573b823202e5bb0a`

```jasec
ja source 0.3
module corpus.ja_security.example_00191
use Security
policy no_network

principal WorkerJASEC_00191
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport96 classification restricted
policy PolicyJASEC_00191 {
    deny network.* by default
    allow ModelExport96 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00191.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-0d882e075d325ca944bc`
- Judgment: `Environment; Policy; {secret.reference} ⊢ node-cf00f92a577355f20af3 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-cf00f92a577355f20af3` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `secret.reference`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-25cdc5a6b01a34b51d39`
- MCRT record: `mcrt-e04485c7594c88400c25`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Specify syntax, resolution, and proof diagnostics.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 18: Static Proofs and Policy Verification

## Learning objectives

- Explain proof obligations for noninterference, attenuation, and precedence across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that accepted policies satisfy declared static obligations.
- Construct a positive case and a minimal counterexample involving stale or partial proofs treated as current.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **proof obligations for noninterference, attenuation, and precedence** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **accepted policies satisfy declared static obligations**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **stale or partial proofs treated as current**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00191`  
**Feature:** `static_proof`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `70523409747706ad169ea4651ee481a045e27aa8c971e591573b823202e5bb0a`

```jasec
ja source 0.3
module corpus.ja_security.example_00191
use Security
policy no_network

principal WorkerJASEC_00191
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport96 classification restricted
policy PolicyJASEC_00191 {
    deny network.* by default
    allow ModelExport96 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00191.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-0d882e075d325ca944bc`
- Judgment: `Environment; Policy; {secret.reference} ⊢ node-cf00f92a577355f20af3 : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-cf00f92a577355f20af3` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `secret.reference`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-25cdc5a6b01a34b51d39`
- MCRT record: `mcrt-e04485c7594c88400c25`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Build a proof bundle and invalidation test.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 19: Runtime Enforcement and Deterministic Replay

## Learning objectives

- Explain state-aware evaluation, sandbox enforcement, and replay across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that the same state and inputs reproduce the same decision and receipt.
- Construct a positive case and a minimal counterexample involving runtime drift from compiled policy semantics.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **state-aware evaluation, sandbox enforcement, and replay** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **the same state and inputs reproduce the same decision and receipt**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **runtime drift from compiled policy semantics**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00022`  
**Feature:** `runtime_enforcement`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `6f925334ecd4137288c829d0c2d27cfa2527941493eaae5e32b21f64616d10ed`

```jasec
ja source 0.3
module corpus.ja_security.example_00022
use Security
policy no_network

principal WorkerJASEC_00022
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport24 classification restricted
policy PolicyJASEC_00022 {
    deny network.* by default
    allow ModelExport24 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00022.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-af3fac05773158af1249`
- Judgment: `Environment; Policy; {approval.verify} ⊢ node-7d9d79128220ccd20f07 : PolicyDecision ! {ledger.append} ⇒ validated`
- AST node: `node-7d9d79128220ccd20f07` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `ledger.append`
- Capabilities: `approval.verify`
- Semantic operator: `principal_declare`
- Policy decision: `allow`
- R12 record: `r12-45e3574fe91b25338735`
- MCRT record: `mcrt-d730a96f30cf89dd7c5d`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Define a replayable decision transaction.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 20: Optimization Without Security Drift

## Learning objectives

- Explain safe indexing, normalization, caching, and rule simplification across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that optimization preserves decisions, precedence, explanations, lifecycle, and audit.
- Construct a positive case and a minimal counterexample involving cache reuse across changed identities or revocation state.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **safe indexing, normalization, caching, and rule simplification** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **optimization preserves decisions, precedence, explanations, lifecycle, and audit**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **cache reuse across changed identities or revocation state**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00008`  
**Feature:** `policy_composition`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `5a7d87c55b83181fe92a73d1d2c6399e38c3ad498d91623e97717f08dd8de3eb`

```jasec
ja source 0.3
module corpus.ja_security.example_00008
use Security
policy no_network

principal WorkerJASEC_00008
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport10 classification restricted
policy PolicyJASEC_00008 {
    deny network.* by default
    allow ModelExport10 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00008.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-0e5f29c7bfe177a5b2b9`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-4aa1d31f6978b1b64174 : PolicyDecision ! {state.read} ⇒ validated`
- AST node: `node-4aa1d31f6978b1b64174` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.read`
- Capabilities: `ledger.append`
- Semantic operator: `allow`
- Policy decision: `allow`
- R12 record: `r12-73b34f60a69ad485eb3c`
- MCRT record: `mcrt-987355ba8aac8fe205b1`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Create equivalence and invalidation tests.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 21: R12, MCRT, Certification, and Smithson 8S

## Learning objectives

- Explain provenance, uncertainty, relation classification, and evidence scope across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that modeled and native evidence remain distinct and limitations remain explicit.
- Construct a positive case and a minimal counterexample involving promoting projected or modeled results into unsupported claims.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **provenance, uncertainty, relation classification, and evidence scope** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **modeled and native evidence remain distinct and limitations remain explicit**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **promoting projected or modeled results into unsupported claims**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00301`  
**Feature:** `explanation`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `b78b4a428508d88ad74ed934dc453efce5fab87e53bf6585f4246be74bce4934`

```jasec
ja source 0.3
module corpus.ja_security.example_00301
use Security
policy no_network

principal WorkerJASEC_00301
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport12 classification restricted
policy PolicyJASEC_00301 {
    deny network.* by default
    allow ModelExport12 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00301.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-d4c47218aac472312f5d`
- Judgment: `Environment; Policy; {policy.evaluate} ⊢ node-4725907c6978d93592fc : PolicyDecision ! {state.write} ⇒ validated`
- AST node: `node-4725907c6978d93592fc` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `state.write`
- Capabilities: `policy.evaluate`
- Semantic operator: `deny`
- Policy decision: `allow`
- R12 record: `r12-ad4176291cbdca09e70e`
- MCRT record: `mcrt-55bd92222ece82ad0a14`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Construct a certification packet with limitations.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 22: Standalone JA Security Policy Toolchain Capstone

## Learning objectives

- Explain integrated authoring, compilation, proof, enforcement, audit, and publication across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that the release is navigable, fail-closed, air-gap-safe, and independently auditable.
- Construct a positive case and a minimal counterexample involving shipping rules without proofs, runtime tests, receipts, or recovery evidence.
- Separate modeled corpus evidence from native compiler, proof, and runtime evidence.

## Technical foundation

This chapter treats **integrated authoring, compilation, proof, enforcement, audit, and publication** as a compiled language concern. A JA Security program is not merely a list of permissions: it is a typed decision system whose source, identities, rule precedence, effects, capabilities, proof obligations, enforcement plan, and audit receipt are linked by stable evidence. That linkage lets authors review authority before execution and lets a future compiler reject ambiguity before privileged effects occur.

The central invariant is that **the release is navigable, fail-closed, air-gap-safe, and independently auditable**. The compiler must preserve that invariant through name resolution, policy composition, normalization, indexing, lowering, and caching. The runtime must enforce it against current identity, resource, lifecycle, and sandbox state. A result is incomplete when it lacks an explanation, stable source hash, policy decision, or evidence boundary.

The principal counterexample is **shipping rules without proofs, runtime tests, receipts, or recovery evidence**. Negative corpus records are therefore essential: they define where the language must stop, which diagnostic must be stable, and which authority must remain denied. Security correctness is not measured by the number of accepted programs; it is measured by consistent rejection of unsafe programs and faithful handling of uncertainty.

Implementation should proceed in explicit passes: parse stable source nodes; resolve principals, roles, groups, resources, and scopes; infer decision types, effects, and capabilities; evaluate composition and conflict precedence; generate static proof obligations; lower accepted policy to R12; execute only inside the declared sandbox; and emit an MCRT decision receipt. Optimization may index or normalize rules only when it preserves exact decisions, explanations, revocation, expiry, audit ordering, and evidence identities.

## Representative corpus program

**Record:** `JASEC-00022`  
**Feature:** `runtime_enforcement`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `6f925334ecd4137288c829d0c2d27cfa2527941493eaae5e32b21f64616d10ed`

```jasec
ja source 0.3
module corpus.ja_security.example_00022
use Security
policy no_network

principal WorkerJASEC_00022
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport24 classification restricted
policy PolicyJASEC_00022 {
    deny network.* by default
    allow ModelExport24 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == false
emit mcrt "PolicyJASEC_00022.decision.mcrt"
```

## Evidence trace

- Semantic identity: `sem-af3fac05773158af1249`
- Judgment: `Environment; Policy; {approval.verify} ⊢ node-7d9d79128220ccd20f07 : PolicyDecision ! {ledger.append} ⇒ validated`
- AST node: `node-7d9d79128220ccd20f07` (`PolicyDecl`)
- Declared / inferred type: `PolicyDecision` / `PolicyDecision`
- Effects: `ledger.append`
- Capabilities: `approval.verify`
- Semantic operator: `principal_declare`
- Policy decision: `allow`
- R12 record: `r12-45e3574fe91b25338735`
- MCRT record: `mcrt-d730a96f30cf89dd7c5d`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared rules actually express the intended security model. CHARLOTTE reviews the legibility of identity, scope, precedence, explanation, and remediation. LANDON reviews parser, proof checker, policy runtime, sandbox, audit, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and test oracle. Podium requires navigable publication, checksums, provenance, limitations, and a defensible certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify every privileged effect has explicit capability and scope.
- Verify deny, require, approval, revocation, and expiry behavior.
- Verify secrets are reference-only and fully redacted.
- Verify network and process authority fail closed.
- Verify explanations and audit receipts are stable and non-secret.
- Verify optimization and caching preserve the complete decision function.

## Laboratory

**Task:** Build and certify a small offline policy toolchain.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, proof result, R12 change, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, expected diagnostics, evidence map, replay inputs, limitations, and certification decision.

## Review questions

1. Which identity, scope, or rule carries the strongest authority here?
2. Which hash must change when the policy or lifecycle state changes?
3. At what stage should the primary unsafe case be rejected?
4. Which optimization is safe, and which would erase a security obligation?
5. What native test would promote the modeled outcome into execution evidence?

# Appendix A: Evidence Vocabulary

- **Modeled evidence:** expected behavior supplied by the corpus.
- **Structural validation:** counts, hashes, declarations, catalogs, and package integrity.
- **Native compiler evidence:** observed parse, semantic, proof, and lowering results.
- **Native runtime evidence:** observed decision, enforcement, sandbox, audit, and replay results.
- **Certification evidence:** signed decision identifying exact artifact, tools, tests, limitations, and authority.

# Appendix B: Capstone Evidence Packet

1. Source and module identities
2. Identity, role, group, resource, and scope graph
3. Rule precedence and composition report
4. Effect, capability, and proof report
5. R12 records
6. Sandbox and runtime enforcement plan
7. Revocation, expiry, retention, and deletion tests
8. Redaction and audit tests
9. Deterministic replay inputs and results
10. MCRT receipts
11. Structural and native test reports
12. Limitations and certification decision
