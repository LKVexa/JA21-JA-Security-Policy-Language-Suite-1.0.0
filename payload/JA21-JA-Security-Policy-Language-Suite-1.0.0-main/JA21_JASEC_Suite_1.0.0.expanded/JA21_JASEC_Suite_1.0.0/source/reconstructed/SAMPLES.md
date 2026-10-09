# JA Security Policy Language — Corpus Samples



Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## 8S Coupled Mechanics Integration

This document is normalized to the **Smithson 8S Coupled Mechanics v1.0** framework. Candidate \(S^3\) fibers occupy latent penteract centers
\[
\mathbf c_n=\ell\mathbf n,\qquad \mathbf n\in\mathbb Z^5,\qquad \|\mathbf n\|_1\le M.
\]
The fifth coordinate \(t_8\) is an elucidation axis and is admitted only when
\[
\mathbf e_\perp=(I-C_4C_4^+)\mathbf e,\qquad
\eta_{\mathrm{ind}}=\frac{\|\mathbf e_\perp\|_2^2}{\|\mathbf e\|_2^2+\varepsilon}\ge\varepsilon_{\mathrm{ind}},
\]
and the held-out efficacy gain satisfies \(\Delta_{8S}=\operatorname{Score}(\mathcal M_8)-\operatorname{Score}(\mathcal M_7)>\varepsilon_{\mathrm{gain}}\).

Sparse geometric-semantic coupling and selective triadic escalation use
\[
W_{ij}=A_{ij}\exp\!\left[-\frac{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)}{2\sigma_c^2}-\frac{d_J(i,j)^2}{2\sigma_J^2}\right],
\]
\[
\dot\theta_i=\omega_i+K_2\sum_jW_{ij}\sin(\theta_j-\theta_i)+K_3\sum_{j,k}H_{ijk}\sin(\theta_j+\theta_k-2\theta_i).
\]
Activation, effective support, and radius are
\[
p_i=\sigma(h_i),\qquad
s_i=p_i\kappa_i(1-\chi_i)(1-\zeta_i)v(\omega_i),\qquad
r_i=r_{\max}B_{5,\infty}(\mathbf c_i)^\alpha s_i^{1/3}.
\]
Each active site carries
\[
F_i=S^3_{r_i}=\{\mathbf y\in\mathbb R^4:\|\mathbf y\|_2=r_i\},
\]
so the noncollapsed total space is locally \(5+3=8\) dimensional.

Relation testing remains independent across latent geometry, product-state separation, visible projection, and judgement space:
\[
g^{(5)}_{ij}=\sqrt{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)}-(\lambda_i+\lambda_j),
\]
\[
\delta^{(8)}_{ij}=\sqrt{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)+(r_i-r_j)^2},
\]
\[
g^{(3)}_{ij}=\|\Pi_5\mathbf c_i-\Pi_5\mathbf c_j\|_2-(\widehat r_i+\widehat r_j),
\qquad
g^{(J)}_{ij}=d_J(\mathfrak J_i,\mathfrak J_j)-\theta_J.
\]
R12 must retain the fifth-coordinate meaning, \(\eta_{\mathrm{ind}}\), \(W\), optional \(H\), phase, activation/support, \(g^{(5)}\), \(\delta^{(8)}\), \(g^{(3)}\), \(g^{(J)}\), projection version, uncertainty, relation class, interaction order, \(\Delta_{8S}\), provenance, and limitations.

**Example:** If \(g^{(5)}>\mathrm{tol}_5\) but \(g^{(3)}\le\mathrm{tol}_3\), record `PROJECTION_ONLY`; do not replace latent structure with visible appearance.

**Claim boundary:** this is a proposed penteract–\(S^3\) computational framework. The local dimension count is eight where the fiber is noncollapsed, but the construction is not proclaimed to be the standard sphere \(S^8\) without a separate topological proof.
## JASEC-00001 — allow_rule

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasec
ja source 0.3
module corpus.ja_security.example_00001
use Security
policy no_network

principal WorkerJASEC_00001
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport3 classification restricted
policy PolicyJASEC_00001 {
    deny network.* by default
    allow ModelExport3 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00001.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-98c69e678e4c1cd88fc3",
  "meaning": "Demonstrates allow rule at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {policy.evaluate} ⊢ node-d0226ad9dc88f507d385 : PolicyDecision ! {state.write} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "state.write"
  ],
  "capabilities": [
    "policy.evaluate"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-d0226ad9dc88f507d385",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "ec1fa31839c0cecd4c4964b94884a5450bcae55a7d1e2e8c6bfa11fbb2ed164c",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "allow_rule",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "state.write"
  ],
  "capability_requirements": [
    "policy.evaluate"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-83a1ea408154b56ef75a",
  "mcrt_reference": "mcrt-787e454eff40a7232ca0",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-2227ee0f4956e5ce7049",
      "kind": "allow_rule"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-83a1ea408154b56ef75a",
    "statement_identity": "JASEC-00001",
    "node_identity": "node-d0226ad9dc88f507d385",
    "language_profile": "ja.security",
    "semantic_operator": "deny",
    "sequence": 1,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "state.write"
    ],
    "capabilities": [
      "policy.evaluate"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "ec1fa31839c0cecd4c4964b94884a5450bcae55a7d1e2e8c6bfa11fbb2ed164c"
    ],
    "output_hashes": [
      "bb6a39e5fdf6aace563683edde41ba3e7b0c231317df79d7584c0c402ad115e2"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00001",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-787e454eff40a7232ca0",
    "canonical_tuple": "<v00001, phi_ja_security, s00001, d0, rho:ja.security.record_00001, operator:deny, OMEGA_JASEC_deny, state:integrated, error0, theta00001, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00001.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00001:allow_rule:complete",
  "effects_observed": [
    "state.write"
  ],
  "capabilities_consumed": [
    "policy.evaluate"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-787e454eff40a7232ca0",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "ec1fa31839c0cecd4c4964b94884a5450bcae55a7d1e2e8c6bfa11fbb2ed164c",
    "ast_node": "node-d0226ad9dc88f507d385",
    "semantic_judgment": "sem-98c69e678e4c1cd88fc3",
    "r12_record": "r12-83a1ea408154b56ef75a",
    "sequence": 1,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00001 vector=v00001 category=ja-security op=deny key=ja.security.record_00001 value=\"allow_rule:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates allow rule at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `deny`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00002 — retention_rule

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00002.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-b3e0ced85ac7d780338c",
  "meaning": "Demonstrates retention rule at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {ledger.append} ⊢ node-31fffe98c86612f5a20e : PolicyDecision ! {ledger.append} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "ledger.append"
  ],
  "capabilities": [
    "ledger.append"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-31fffe98c86612f5a20e",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "80d733fe7cac9fba7b7302b09786466574712ada853c21eea89da50bbf712575",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "retention_rule",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "ledger.append"
  ],
  "capability_requirements": [
    "ledger.append"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-48bd792e9d2148dd4e21",
  "mcrt_reference": "mcrt-60bb56050e89b7cb9c95",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-48e48df5a1b331a45822",
      "kind": "retention_rule"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-48bd792e9d2148dd4e21",
    "statement_identity": "JASEC-00002",
    "node_identity": "node-31fffe98c86612f5a20e",
    "language_profile": "ja.security",
    "semantic_operator": "principal_declare",
    "sequence": 2,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "ledger.append"
    ],
    "capabilities": [
      "ledger.append"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "80d733fe7cac9fba7b7302b09786466574712ada853c21eea89da50bbf712575"
    ],
    "output_hashes": [
      "b511f2d6b786ab24e5969bdc1a568780e57224ea835cb92879c05eab65561591"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00002",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-60bb56050e89b7cb9c95",
    "canonical_tuple": "<v00002, phi_ja_security, s00002, d0, rho:ja.security.record_00002, operator:principal_declare, OMEGA_JASEC_principal_declare, state:integrated, error0, theta00002, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00002.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00002:retention_rule:complete",
  "effects_observed": [
    "ledger.append"
  ],
  "capabilities_consumed": [
    "ledger.append"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-60bb56050e89b7cb9c95",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "80d733fe7cac9fba7b7302b09786466574712ada853c21eea89da50bbf712575",
    "ast_node": "node-31fffe98c86612f5a20e",
    "semantic_judgment": "sem-b3e0ced85ac7d780338c",
    "r12_record": "r12-48bd792e9d2148dd4e21",
    "sequence": 2,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00002 vector=v00002 category=ja-security op=principal_declare key=ja.security.record_00002 value=\"retention_rule:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates retention rule at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `principal_declare`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00003 — process_sandbox

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasec
ja source 0.3
module corpus.ja_security.example_00003
use Security
policy no_network

principal WorkerJASEC_00003
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport5 classification restricted
policy PolicyJASEC_00003 {
    deny network.* by default
    deny ModelExport5 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00003.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-a9e1dd977cf72506ec46",
  "meaning": "Demonstrates process sandbox at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {delegation.issue:bounded} ⊢ node-7b8354be0dec54b94f95 : PolicyDecision ! {state.read} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "state.read"
  ],
  "capabilities": [
    "delegation.issue:bounded"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-7b8354be0dec54b94f95",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "5f357a4ecf7e150fd202f8680067d0765e89f359c5f49af958d45441caea2ce7",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "process_sandbox",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "state.read"
  ],
  "capability_requirements": [
    "delegation.issue:bounded"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-3dcf152bca8bf2f6fd7a",
  "mcrt_reference": "mcrt-bf5fe0dcdb5ff5acb97f",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-41600ca3cb084b9fb4e2",
      "kind": "process_sandbox"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-3dcf152bca8bf2f6fd7a",
    "statement_identity": "JASEC-00003",
    "node_identity": "node-7b8354be0dec54b94f95",
    "language_profile": "ja.security",
    "semantic_operator": "classify",
    "sequence": 3,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "state.read"
    ],
    "capabilities": [
      "delegation.issue:bounded"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "5f357a4ecf7e150fd202f8680067d0765e89f359c5f49af958d45441caea2ce7"
    ],
    "output_hashes": [
      "500a1c8fd48237673bc8776e72478a1d39076432d6274d89650080fa6cd095c5"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00003",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-bf5fe0dcdb5ff5acb97f",
    "canonical_tuple": "<v00003, phi_ja_security, s00003, d0, rho:ja.security.record_00003, operator:classify, OMEGA_JASEC_classify, state:integrated, error0, theta00003, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00003.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00003:process_sandbox:complete",
  "effects_observed": [
    "state.read"
  ],
  "capabilities_consumed": [
    "delegation.issue:bounded"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-bf5fe0dcdb5ff5acb97f",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "5f357a4ecf7e150fd202f8680067d0765e89f359c5f49af958d45441caea2ce7",
    "ast_node": "node-7b8354be0dec54b94f95",
    "semantic_judgment": "sem-a9e1dd977cf72506ec46",
    "r12_record": "r12-3dcf152bca8bf2f6fd7a",
    "sequence": 3,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00003 vector=v00003 category=ja-security op=classify key=ja.security.record_00003 value=\"process_sandbox:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates process sandbox at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `classify`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00004 — redaction

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasec
ja source 0.3
module corpus.ja_security.example_00004
use Security
policy no_network

principal WorkerJASEC_00004
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport6 classification restricted
policy PolicyJASEC_00004 {
    deny network.* by default
    allow ModelExport6 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00004.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-bfef78631108ff735f67",
  "meaning": "Demonstrates redaction at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {approval.verify} ⊢ node-084ff6569cc0ff1a8d49 : PolicyDecision ! {secret.read} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "secret.read"
  ],
  "capabilities": [
    "approval.verify"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-084ff6569cc0ff1a8d49",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "40f83bf4becd57b0acbe06f7aa88148e0b5a3831abd21a840a56ec620daa1393",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "redaction",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "secret.read"
  ],
  "capability_requirements": [
    "approval.verify"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-e139cda731d834b41817",
  "mcrt_reference": "mcrt-ee348e16c906c087f0cf",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-87cddabf7a0cb1b1ed5a",
      "kind": "redaction"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-e139cda731d834b41817",
    "statement_identity": "JASEC-00004",
    "node_identity": "node-084ff6569cc0ff1a8d49",
    "language_profile": "ja.security",
    "semantic_operator": "require",
    "sequence": 4,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "secret.read"
    ],
    "capabilities": [
      "approval.verify"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "40f83bf4becd57b0acbe06f7aa88148e0b5a3831abd21a840a56ec620daa1393"
    ],
    "output_hashes": [
      "5d71c47a51a15deb0a7197e5691ae2f3e0564dcf63fe7a43b41426fcc2f48c64"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00004",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-ee348e16c906c087f0cf",
    "canonical_tuple": "<v00004, phi_ja_security, s00004, d0, rho:ja.security.record_00004, operator:require, OMEGA_JASEC_require, state:integrated, error0, theta00004, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00004.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00004:redaction:complete",
  "effects_observed": [
    "secret.read"
  ],
  "capabilities_consumed": [
    "approval.verify"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-ee348e16c906c087f0cf",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "40f83bf4becd57b0acbe06f7aa88148e0b5a3831abd21a840a56ec620daa1393",
    "ast_node": "node-084ff6569cc0ff1a8d49",
    "semantic_judgment": "sem-bfef78631108ff735f67",
    "r12_record": "r12-e139cda731d834b41817",
    "sequence": 4,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00004 vector=v00004 category=ja-security op=require key=ja.security.record_00004 value=\"redaction:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates redaction at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `require`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00005 — group

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasec
ja source 0.3
module corpus.ja_security.example_00005
use Security
policy no_network

principal WorkerJASEC_00005
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport7 classification restricted
policy PolicyJASEC_00005 {
    deny network.* by default
    allow ModelExport7 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00005.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-9ddb58daad18c74f5160",
  "meaning": "Demonstrates group at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {secret.reference} ⊢ node-b62ca849604e4750854f : PolicyDecision ! {pure} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "pure"
  ],
  "capabilities": [
    "secret.reference"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-b62ca849604e4750854f",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "d990d2f1637e05ef23f0f9cc2cc79eda7067cd61de34849727f237063eb6155d",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "group",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "pure"
  ],
  "capability_requirements": [
    "secret.reference"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-7f65f4b2f668b14eb11e",
  "mcrt_reference": "mcrt-378d5a439ba3be1c5688",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-0a18f006176ae34cc2eb",
      "kind": "group"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-7f65f4b2f668b14eb11e",
    "statement_identity": "JASEC-00005",
    "node_identity": "node-b62ca849604e4750854f",
    "language_profile": "ja.security",
    "semantic_operator": "capability_declare",
    "sequence": 5,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "pure"
    ],
    "capabilities": [
      "secret.reference"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "d990d2f1637e05ef23f0f9cc2cc79eda7067cd61de34849727f237063eb6155d"
    ],
    "output_hashes": [
      "24eee30fb850ce3ad924cae33fc49ecf8bd05b9125d0d5a4b487d4897489ae6b"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00005",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-378d5a439ba3be1c5688",
    "canonical_tuple": "<v00005, phi_ja_security, s00005, d0, rho:ja.security.record_00005, operator:capability_declare, OMEGA_JASEC_capability_declare, state:integrated, error0, theta00005, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00005.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00005:group:complete",
  "effects_observed": [],
  "capabilities_consumed": [
    "secret.reference"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-378d5a439ba3be1c5688",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "d990d2f1637e05ef23f0f9cc2cc79eda7067cd61de34849727f237063eb6155d",
    "ast_node": "node-b62ca849604e4750854f",
    "semantic_judgment": "sem-9ddb58daad18c74f5160",
    "r12_record": "r12-7f65f4b2f668b14eb11e",
    "sequence": 5,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00005 vector=v00005 category=ja-security op=capability_declare key=ja.security.record_00005 value=\"group:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates group at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `capability_declare`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00006 — audit_rule

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00006.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-2a8d15410c297a3b6855",
  "meaning": "Demonstrates audit rule at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {policy.enforce} ⊢ node-2d3140f5b6ba4a744695 : PolicyDecision ! {state.write} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "state.write"
  ],
  "capabilities": [
    "policy.enforce"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-2d3140f5b6ba4a744695",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "563cc2ab8088ab9a517b3bc30ad3834d2ea6b70cb99cfd8b2a08df7de080b7a8",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "audit_rule",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "state.write"
  ],
  "capability_requirements": [
    "policy.enforce"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-3b9243ba3b2fb2915448",
  "mcrt_reference": "mcrt-54f4c47086895e958700",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-f03ee5beb9171c77dd9d",
      "kind": "audit_rule"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-3b9243ba3b2fb2915448",
    "statement_identity": "JASEC-00006",
    "node_identity": "node-2d3140f5b6ba4a744695",
    "language_profile": "ja.security",
    "semantic_operator": "authorize",
    "sequence": 6,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "state.write"
    ],
    "capabilities": [
      "policy.enforce"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "563cc2ab8088ab9a517b3bc30ad3834d2ea6b70cb99cfd8b2a08df7de080b7a8"
    ],
    "output_hashes": [
      "d99754fc68be6364425ced50ce7220a260479775b0a4325ca18bcaa30a17c9ba"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00006",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-54f4c47086895e958700",
    "canonical_tuple": "<v00006, phi_ja_security, s00006, d0, rho:ja.security.record_00006, operator:authorize, OMEGA_JASEC_authorize, state:integrated, error0, theta00006, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00006.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00006:audit_rule:complete",
  "effects_observed": [
    "state.write"
  ],
  "capabilities_consumed": [
    "policy.enforce"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-54f4c47086895e958700",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "563cc2ab8088ab9a517b3bc30ad3834d2ea6b70cb99cfd8b2a08df7de080b7a8",
    "ast_node": "node-2d3140f5b6ba4a744695",
    "semantic_judgment": "sem-2a8d15410c297a3b6855",
    "r12_record": "r12-3b9243ba3b2fb2915448",
    "sequence": 6,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00006 vector=v00006 category=ja-security op=authorize key=ja.security.record_00006 value=\"audit_rule:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates audit rule at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `authorize`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00007 — model_access_policy

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasec
ja source 0.3
module corpus.ja_security.example_00007
use Security
policy no_network

principal WorkerJASEC_00007
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport9 classification restricted
policy PolicyJASEC_00007 {
    deny network.* by default
    allow ModelExport9 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00007.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-0c84fa632b3ab328c386",
  "meaning": "Demonstrates model access policy at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {policy.evaluate} ⊢ node-fc401571ab64d766bea7 : PolicyDecision ! {ledger.append} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "ledger.append"
  ],
  "capabilities": [
    "policy.evaluate"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-fc401571ab64d766bea7",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "c38bcd1583b08c73492ba14de385cd2d4138714ff0cd41c9f9701ea944d98ed3",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "model_access_policy",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "ledger.append"
  ],
  "capability_requirements": [
    "policy.evaluate"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-da612d7bba39744a61f9",
  "mcrt_reference": "mcrt-c1d44f52e2048aa7f5fc",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-bb32ec8b8f1eec0dcefc",
      "kind": "model_access_policy"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-da612d7bba39744a61f9",
    "statement_identity": "JASEC-00007",
    "node_identity": "node-fc401571ab64d766bea7",
    "language_profile": "ja.security",
    "semantic_operator": "audit",
    "sequence": 7,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "ledger.append"
    ],
    "capabilities": [
      "policy.evaluate"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "c38bcd1583b08c73492ba14de385cd2d4138714ff0cd41c9f9701ea944d98ed3"
    ],
    "output_hashes": [
      "1af2d8ef7ca8106c25010d05042197a44c4e0aa33ee973e7630e7b6729befc51"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00007",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-c1d44f52e2048aa7f5fc",
    "canonical_tuple": "<v00007, phi_ja_security, s00007, d0, rho:ja.security.record_00007, operator:audit, OMEGA_JASEC_audit, state:integrated, error0, theta00007, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00007.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00007:model_access_policy:complete",
  "effects_observed": [
    "ledger.append"
  ],
  "capabilities_consumed": [
    "policy.evaluate"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-c1d44f52e2048aa7f5fc",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "c38bcd1583b08c73492ba14de385cd2d4138714ff0cd41c9f9701ea944d98ed3",
    "ast_node": "node-fc401571ab64d766bea7",
    "semantic_judgment": "sem-0c84fa632b3ab328c386",
    "r12_record": "r12-da612d7bba39744a61f9",
    "sequence": 7,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00007 vector=v00007 category=ja-security op=audit key=ja.security.record_00007 value=\"model_access_policy:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates model access policy at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `audit`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00008 — policy_composition

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00008.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-0e5f29c7bfe177a5b2b9",
  "meaning": "Demonstrates policy composition at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {ledger.append} ⊢ node-4aa1d31f6978b1b64174 : PolicyDecision ! {state.read} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "state.read"
  ],
  "capabilities": [
    "ledger.append"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-4aa1d31f6978b1b64174",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "5a7d87c55b83181fe92a73d1d2c6399e38c3ad498d91623e97717f08dd8de3eb",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "policy_composition",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "state.read"
  ],
  "capability_requirements": [
    "ledger.append"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-73b34f60a69ad485eb3c",
  "mcrt_reference": "mcrt-987355ba8aac8fe205b1",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-35d418b75e8369ac36fc",
      "kind": "policy_composition"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-73b34f60a69ad485eb3c",
    "statement_identity": "JASEC-00008",
    "node_identity": "node-4aa1d31f6978b1b64174",
    "language_profile": "ja.security",
    "semantic_operator": "allow",
    "sequence": 8,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "state.read"
    ],
    "capabilities": [
      "ledger.append"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "5a7d87c55b83181fe92a73d1d2c6399e38c3ad498d91623e97717f08dd8de3eb"
    ],
    "output_hashes": [
      "ef870673f4e8a3c94f4753eddd911577361e764fb916bf7202cb9b8ffb768fcf"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00008",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-987355ba8aac8fe205b1",
    "canonical_tuple": "<v00008, phi_ja_security, s00008, d0, rho:ja.security.record_00008, operator:allow, OMEGA_JASEC_allow, state:integrated, error0, theta00008, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00008.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00008:policy_composition:complete",
  "effects_observed": [
    "state.read"
  ],
  "capabilities_consumed": [
    "ledger.append"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-987355ba8aac8fe205b1",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "5a7d87c55b83181fe92a73d1d2c6399e38c3ad498d91623e97717f08dd8de3eb",
    "ast_node": "node-4aa1d31f6978b1b64174",
    "semantic_judgment": "sem-0e5f29c7bfe177a5b2b9",
    "r12_record": "r12-73b34f60a69ad485eb3c",
    "sequence": 8,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00008 vector=v00008 category=ja-security op=allow key=ja.security.record_00008 value=\"policy_composition:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates policy composition at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `allow`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00009 — fail_closed

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasec
ja source 0.3
module corpus.ja_security.example_00009
use Security
policy no_network

principal WorkerJASEC_00009
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport11 classification restricted
policy PolicyJASEC_00009 {
    deny network.* by default
    allow ModelExport11 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00009.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-5fb12061401ca0087e25",
  "meaning": "Demonstrates fail closed at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {delegation.issue:bounded} ⊢ node-235455913368ba705958 : PolicyDecision ! {secret.read} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "secret.read"
  ],
  "capabilities": [
    "delegation.issue:bounded"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-235455913368ba705958",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-703298452bb917bf",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "bc5653c1b2eeefd309cdf69eff95bcdec9e0045795446375eee4ac7d6d92c26a",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "fail_closed",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "secret.read"
  ],
  "capability_requirements": [
    "delegation.issue:bounded"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-08e7a8a5c679502cf589",
  "mcrt_reference": "mcrt-c8e077ab7d96f793a98f",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-c225dcbc9ae9e798803c",
      "kind": "fail_closed"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-08e7a8a5c679502cf589",
    "statement_identity": "JASEC-00009",
    "node_identity": "node-235455913368ba705958",
    "language_profile": "ja.security",
    "semantic_operator": "explain",
    "sequence": 9,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "secret.read"
    ],
    "capabilities": [
      "delegation.issue:bounded"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "bc5653c1b2eeefd309cdf69eff95bcdec9e0045795446375eee4ac7d6d92c26a"
    ],
    "output_hashes": [
      "2372fe6f1814abefde74e7e9a35b0741a81603b5c41d20375ab7ce8477a38a63"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00009",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-c8e077ab7d96f793a98f",
    "canonical_tuple": "<v00009, phi_ja_security, s00009, d0, rho:ja.security.record_00009, operator:explain, OMEGA_JASEC_explain, state:integrated, error0, theta00009, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00009.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00009:fail_closed:complete",
  "effects_observed": [
    "secret.read"
  ],
  "capabilities_consumed": [
    "delegation.issue:bounded"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-c8e077ab7d96f793a98f",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "bc5653c1b2eeefd309cdf69eff95bcdec9e0045795446375eee4ac7d6d92c26a",
    "ast_node": "node-235455913368ba705958",
    "semantic_judgment": "sem-5fb12061401ca0087e25",
    "r12_record": "r12-08e7a8a5c679502cf589",
    "sequence": 9,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00009 vector=v00009 category=ja-security op=explain key=ja.security.record_00009 value=\"fail_closed:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates fail closed at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `explain`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00010 — scope

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasec
ja source 0.3
module corpus.ja_security.example_00010
use Security
policy no_network

principal WorkerJASEC_00010
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport12 classification restricted
policy PolicyJASEC_00010 {
    deny network.* by default
    allow ModelExport12 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00010.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-2fd2c6badb1c01eccaa6",
  "meaning": "Demonstrates scope at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {approval.verify} ⊢ node-716437202957f127b859 : PolicyDecision ! {pure} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "pure"
  ],
  "capabilities": [
    "approval.verify"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-716437202957f127b859",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-98c69e678e4c1cd8",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "a134a5b0a8a3747574e40b3a5072db3eab5ee52ec252046e9f9e25876ac721e5",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "scope",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "pure"
  ],
  "capability_requirements": [
    "approval.verify"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-38fb5219b9d589e996ec",
  "mcrt_reference": "mcrt-a5732e15234bdaed7786",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-2150f6f86ee1c91164bc",
      "kind": "scope"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-38fb5219b9d589e996ec",
    "statement_identity": "JASEC-00010",
    "node_identity": "node-716437202957f127b859",
    "language_profile": "ja.security",
    "semantic_operator": "delegate",
    "sequence": 10,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "pure"
    ],
    "capabilities": [
      "approval.verify"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "a134a5b0a8a3747574e40b3a5072db3eab5ee52ec252046e9f9e25876ac721e5"
    ],
    "output_hashes": [
      "b6cc5c1b31974db667f67d452c891fd87e24bb1137a04f7115b092ab434a3214"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00010",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-a5732e15234bdaed7786",
    "canonical_tuple": "<v00010, phi_ja_security, s00010, d0, rho:ja.security.record_00010, operator:delegate, OMEGA_JASEC_delegate, state:integrated, error0, theta00010, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00010.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00010:scope:complete",
  "effects_observed": [],
  "capabilities_consumed": [
    "approval.verify"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-a5732e15234bdaed7786",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "a134a5b0a8a3747574e40b3a5072db3eab5ee52ec252046e9f9e25876ac721e5",
    "ast_node": "node-716437202957f127b859",
    "semantic_judgment": "sem-2fd2c6badb1c01eccaa6",
    "r12_record": "r12-38fb5219b9d589e996ec",
    "sequence": 10,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00010 vector=v00010 category=ja-security op=delegate key=ja.security.record_00010 value=\"scope:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates scope at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `delegate`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00011 — data_classification

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasec
ja source 0.3
module corpus.ja_security.example_00011
use Security
policy no_network

principal WorkerJASEC_00011
role TrainingWorker {
    grant device.gpu
    grant dataset.read:approved
}
resource ModelExport13 classification restricted
policy PolicyJASEC_00011 {
    deny network.* by default
    allow ModelExport13 when principal.role == TrainingWorker
    require human_approval for model.export
    audit all privileged_effects
    redact secret.values
    resolve conflicts explicit_deny_wins
}
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00011.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-24e80a1fb9bd46f26b44",
  "meaning": "Demonstrates data classification at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {secret.reference} ⊢ node-0f2c8e8d1132d90de6aa : PolicyDecision ! {state.write} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "state.write"
  ],
  "capabilities": [
    "secret.reference"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-0f2c8e8d1132d90de6aa",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-98c69e678e4c1cd8",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "c46aebcdc5a4f376588400656072c9a053bcceaad6a7e4c3bce3da8da8136526",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "data_classification",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "state.write"
  ],
  "capability_requirements": [
    "secret.reference"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-bb64c30f91280557a276",
  "mcrt_reference": "mcrt-537a6e7d40745f9f992c",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-80d526182a209452c9ca",
      "kind": "data_classification"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-bb64c30f91280557a276",
    "statement_identity": "JASEC-00011",
    "node_identity": "node-0f2c8e8d1132d90de6aa",
    "language_profile": "ja.security",
    "semantic_operator": "deny",
    "sequence": 11,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "state.write"
    ],
    "capabilities": [
      "secret.reference"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "c46aebcdc5a4f376588400656072c9a053bcceaad6a7e4c3bce3da8da8136526"
    ],
    "output_hashes": [
      "a4ff8d59a6abb69c0d15947451120d3c5e01e92873f12a3834e7e80219c920d6"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00011",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-537a6e7d40745f9f992c",
    "canonical_tuple": "<v00011, phi_ja_security, s00011, d0, rho:ja.security.record_00011, operator:deny, OMEGA_JASEC_deny, state:integrated, error0, theta00011, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00011.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00011:data_classification:complete",
  "effects_observed": [
    "state.write"
  ],
  "capabilities_consumed": [
    "secret.reference"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-537a6e7d40745f9f992c",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "c46aebcdc5a4f376588400656072c9a053bcceaad6a7e4c3bce3da8da8136526",
    "ast_node": "node-0f2c8e8d1132d90de6aa",
    "semantic_judgment": "sem-24e80a1fb9bd46f26b44",
    "r12_record": "r12-bb64c30f91280557a276",
    "sequence": 11,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00011 vector=v00011 category=ja-security op=deny key=ja.security.record_00011 value=\"data_classification:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates data classification at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `deny`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASEC-00012 — network_sandbox

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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
assert policy.secret_leak == true
emit mcrt "PolicyJASEC_00012.decision.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-516dfe4e6a4bc9a83f46",
  "meaning": "Demonstrates network sandbox at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {policy.enforce} ⊢ node-e6085bd7bb23fef26cdd : PolicyDecision ! {ledger.append} ⇒ validated",
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effects": [
    "ledger.append"
  ],
  "capabilities": [
    "policy.enforce"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-e6085bd7bb23fef26cdd",
  "node_kind": "PolicyDecl",
  "language_id": "ja.security",
  "module_id": "module-98c69e678e4c1cd8",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "206f43c4241937aac0751bf7e908a2c9d49fc3a4a40338f7731e2529d232febe",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "network_sandbox",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "PolicyDecision",
  "inferred_type": "PolicyDecision",
  "effect_set": [
    "ledger.append"
  ],
  "capability_requirements": [
    "policy.enforce"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-dcd1ce176b483b3c766c",
  "mcrt_reference": "mcrt-3b8228ca23777b32a9e8",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-31fa45b0bc35a5a8482f",
      "kind": "network_sandbox"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-dcd1ce176b483b3c766c",
    "statement_identity": "JASEC-00012",
    "node_identity": "node-e6085bd7bb23fef26cdd",
    "language_profile": "ja.security",
    "semantic_operator": "principal_declare",
    "sequence": 12,
    "dependencies": [],
    "type": "PolicyDecision",
    "effects": [
      "ledger.append"
    ],
    "capabilities": [
      "policy.enforce"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "206f43c4241937aac0751bf7e908a2c9d49fc3a4a40338f7731e2529d232febe"
    ],
    "output_hashes": [
      "08d197efb38aa4dc6523ce307d9658167a5ae99e95228b9e4d9cec7b2c4cb172"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASEC-00012",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-3b8228ca23777b32a9e8",
    "canonical_tuple": "<v00012, phi_ja_security, s00012, d0, rho:ja.security.record_00012, operator:principal_declare, OMEGA_JASEC_principal_declare, state:integrated, error0, theta00012, confidence1.0000, status:stable>"
  },
  "artifact": "JASEC-00012.jasec.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Policy Decision Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASEC-00012:network_sandbox:complete",
  "effects_observed": [
    "ledger.append"
  ],
  "capabilities_consumed": [
    "policy.enforce"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-3b8228ca23777b32a9e8",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.security",
    "source_hash": "206f43c4241937aac0751bf7e908a2c9d49fc3a4a40338f7731e2529d232febe",
    "ast_node": "node-e6085bd7bb23fef26cdd",
    "semantic_judgment": "sem-516dfe4e6a4bc9a83f46",
    "r12_record": "r12-dcd1ce176b483b3c766c",
    "sequence": 12,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00012 vector=v00012 category=ja-security op=principal_declare key=ja.security.record_00012 value=\"network_sandbox:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates network sandbox at the beginner level for JA Security Policy Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `principal_declare`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit policy indexing but never reorder rules in a way that changes explicit-deny precedence.

Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.
