---
inquiry: inquiry-to-procedure
record_type: recorded-inquiries-index
formal_bundle: false
status: draft
updated: 2026-08-29
---

# Recorded inquiries

A recorded inquiry is a source-grounded ordered record preserving enough of an
inquiry trajectory to reconstruct materially relevant changes without claiming
formal OKF-FC bundle conformance.

Recorded inquiries sit between ordinary notes and formal bundles. They are more
structured than notes because they preserve the sequence, source roles, and
interpretive transitions that matter later. They are not raw transcripts,
because they may include later retrospective analysis and source-role
classification. They are not lightweight bundles or full bundles unless a later
promotion explicitly supplies the required OKF-FC profile machinery.

```text
recorded inquiry != simplified bundle
recorded inquiry != automatically fact-check
```

Representation proportionality is the governing rule: preserve enough structure
to support the intended future use of the trajectory; do not require formal
bundle machinery merely because the trajectory is worth retaining.

Recommended minimum structure:

```text
README.md
inquiry-record.md
analysis.md
sources.md
```

Use neutral metadata such as `record_type`, `formal_bundle: false`, `status`,
and `role_in_parent_inquiry`. Do not use `fc-*` frontmatter unless the record is
explicitly promoted to an OKF-FC bundle profile.

Promotion to a formal bundle may be justified by high stakes, research-critical
provenance, long-running evolution, genuine observer contestation, repeated
handoffs, formal supersession or reopening, reproducibility requirements,
machine validation, controlled counterfactual experiments, trajectory metrics,
or repeated future reuse. Promotion changes governance and representation; it
does not prove the earlier recorded inquiry was defective.
