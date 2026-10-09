# JA Security Policy Language Architecture

```text
JA Security source (.jasec)
        │
        ▼
Parser and identity resolver
        │  principals, groups, roles, resources, scopes
        ▼
Typed Policy AST
        │  allow, deny, require, delegation, revocation, retention
        ▼
Effect / capability / proof analysis
        │  precedence, attenuation, secret, network, process, audit
        ▼
R12 policy record
        │  stable identity, inputs, decision, proof and explanation
        ▼
JA Policy Decision Runtime
        │  fail-closed evaluation, sandbox enforcement, audit journal
        ▼
MCRT decision receipt
```

## Invariants

- Explicit deny dominates conflicting allow unless a declared profile proves another safe precedence rule.
- Delegation cannot widen authority; attenuation is monotonic.
- Revocation and expiry are checked before privileged effects.
- Secrets remain references and are redacted from every evidence surface.
- Network and process capabilities are denied unless explicitly admitted.
- Static proofs do not replace runtime checks where state may change.
- Every privileged decision is explainable, auditable, and tied to stable source identity.
