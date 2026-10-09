# Grammar Specification

The provisional grammar captures the common source surface: module identity, Security import, network policy, principals, groups, roles, capabilities, classified resources, allow/deny/require rules, audit, redaction, conflict resolution, delegation, revocation, assertions, and MCRT emission. A production grammar must define comments, escapes, source recovery, annotations, time and duration syntax, scope patterns, proof declarations, and stable diagnostic spans.

Expected-failure records must remain parseable when the intended failure is semantic, capability, proof, policy, or runtime-related. Recovery must never invent authority or convert a deny/require failure into an allow decision.
