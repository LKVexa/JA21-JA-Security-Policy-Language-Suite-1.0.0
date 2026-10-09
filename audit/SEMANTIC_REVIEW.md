# ja.security audit findings

Passing examples asserted secret_leak=true while intended failure examples asserted false. All 10,000 current assertions now use the corrected polarity, with hashes and qualifications refreshed.

Upgrade status: applied source or tool repair and qualified. Security leak assertion polarity repair.

Proposed fabric role: Principal/resource scope, capability attenuation, deny precedence, revocation/expiry, approval witnesses, secret redaction and fail-closed decisions.

Import rule: Import syntax, contracts and source as reviewed reference; never import modeled outcomes as observed facts.

Source locations: `JA21_JASEC_Suite_1.0.0/corpus/technical/JA21_JASEC_TECHNICAL_CORPUS_10000.jsonl.gz`, `JA21_JASEC_Suite_1.0.0/specification/LANGUAGE_SPECIFICATION.md`
