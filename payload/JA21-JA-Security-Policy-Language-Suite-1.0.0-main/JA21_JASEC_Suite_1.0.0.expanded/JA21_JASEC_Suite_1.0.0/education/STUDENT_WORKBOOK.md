# JA21 JA Security Policy Language Student Workbook

Preserve exact record IDs, source hashes, expected diagnostics, and evidence scope.

## Chapter 1: Security Policy as a Language Suite

- State the invariant: source, judgment, enforcement, and receipt remain connected.
- Describe the failure: treating policy as scattered configuration.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 2: Program Anatomy, Modules, and No-Network Policy

- State the invariant: every decision executes in a named module and declared policy context.
- Describe the failure: implicit authority inherited from the host.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 3: Principals, Identities, Groups, and Roles

- State the invariant: identity resolution is deterministic and auditable.
- Describe the failure: ambiguous or mutable identity aliases.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 4: Resources, Classification, and Scope

- State the invariant: authority is evaluated against exact resource identity and classification.
- Describe the failure: wildcard scope that bypasses classification.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 5: Capabilities and Least Authority

- State the invariant: every privileged effect has an explicit capability.
- Describe the failure: ambient authority and capability inference from names.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 6: Allow, Deny, and Require Rules

- State the invariant: explicit deny and mandatory requirements cannot be erased by permissive rules.
- Describe the failure: first-match logic that hides conflicts.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 7: Conflict Resolution and Policy Composition

- State the invariant: composed policies produce one explainable decision under a declared precedence profile.
- Describe the failure: nondeterministic or circular precedence.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 8: Explanation and Human Approval

- State the invariant: high-risk effects require a recorded human decision when declared.
- Describe the failure: approval after the effect or explanation without evidence.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 9: Delegation and Attenuation

- State the invariant: delegated authority is a subset of the delegator authority.
- Describe the failure: delegation that widens resource, action, or time scope.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 10: Revocation and Time-Bound Permission

- State the invariant: revoked or expired authority cannot authorize a new privileged effect.
- Describe the failure: cached decisions that ignore lifecycle state.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 11: Agent, Tool, and Model Access Policies

- State the invariant: autonomous components receive only explicit task-bound authority.
- Describe the failure: tool invocation or model export through broad inherited roles.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 12: Secrets, Redaction, and Evidence Hygiene

- State the invariant: secret material never appears in source, diagnostics, logs, or MCRT records.
- Describe the failure: embedding or echoing secret values.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 13: Network and Process Sandboxes

- State the invariant: undeclared network and unknown-code execution fail closed.
- Describe the failure: quiet fallback to host network or shell execution.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 14: Retention and Deletion Rules

- State the invariant: retention and deletion decisions remain class-aware and auditable.
- Describe the failure: deletion that ignores hold or retention rules.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 15: Audit Rules and Immutable Decision History

- State the invariant: every privileged decision emits a stable, redacted receipt.
- Describe the failure: best-effort logging or mutable audit identity.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 16: Fail-Closed Policy and Recovery

- State the invariant: uncertainty or unavailable enforcement produces denial or explicit unresolved state.
- Describe the failure: fail-open retry and silent default allow.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 17: Compiler Frontend and Typed Policy AST

- State the invariant: source spans, types, effects, capabilities, and policy decisions remain inspectable.
- Describe the failure: generic errors that hide rejected authority.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 18: Static Proofs and Policy Verification

- State the invariant: accepted policies satisfy declared static obligations.
- Describe the failure: stale or partial proofs treated as current.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 19: Runtime Enforcement and Deterministic Replay

- State the invariant: the same state and inputs reproduce the same decision and receipt.
- Describe the failure: runtime drift from compiled policy semantics.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 20: Optimization Without Security Drift

- State the invariant: optimization preserves decisions, precedence, explanations, lifecycle, and audit.
- Describe the failure: cache reuse across changed identities or revocation state.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 21: R12, MCRT, Certification, and Smithson 8S

- State the invariant: modeled and native evidence remain distinct and limitations remain explicit.
- Describe the failure: promoting projected or modeled results into unsupported claims.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 22: Standalone JA Security Policy Toolchain Capstone

- State the invariant: the release is navigable, fail-closed, air-gap-safe, and independently auditable.
- Describe the failure: shipping rules without proofs, runtime tests, receipts, or recovery evidence.
- Record the source SHA-256 and selected record.
- Draw source → AST → judgment/proof → R12 → enforcement → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.
