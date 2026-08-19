---
type: Event
title: "Round 7: repository structure and reference audit"
description: Audited stubs, current-source correspondence, and foundation citations; clarified stub status, superseded stale v2-current bundle pages, and added reference links to literature anchors.
fc-axis: INQUIRY
fc-round: 7
fc-move: objection
fc-stage: critique
fc-party: codex
fc-touches: [pf/formal.md, s/method.md, s/specification.md, r/overview.md, r/results.md, reproduction/code.md, reproduction/data.md, s/foundations/aumann-agreement.md, s/foundations/simon-bounded-rationality.md, s/foundations/ait-compression.md, s/foundations/coarse-graining-statmech.md, s/foundations/second-order-cybernetics.md, s/foundations/bayesian-agm-belief-revision.md, s/foundations/peirce-inquiry.md, s/foundations/argumentation-theory.md, s/foundations/quine-duhem.md, s/foundations/analytic-historiography.md, s/foundations/provenance-reproducibility.md]
fc-status: open
timestamp: 2026-07-19
---

# Move

The human instruction requested a critical audit of repository structure and correspondence between linked files and their stated purpose, with special attention to stubs and missing references. The audit found that the Step 0-9 deliverables are intentional stubs, but their source prompts were not linked from the stubs themselves; that several current self-bundle pages still described v2 as current after round 4 adopted `docs/framework_v3.md`; and that the foundation anchor pages named author-year sources without reference links.

# Evidence added

- New repository-level audit note: [docs/repository-structure-audit.md](../../../docs/repository-structure-audit.md).
- Stub files updated to say why they remain empty and which Step prompt in `docs/framework_v3.md` governs their future content.
- Stable citation links verified for the named foundation anchors, including Aumann 1976, Simon 1955, Kolmogorov 1965, Rissanen 1978, Boltzmann 1877, von Foerster, Luhmann 1984, Bayes 1763, AGM 1985, Peirce 1877, Dung 1995, Duhem 1906, Quine 1951, Danto 1965, Ankersmit 1983, W3C PROV, and FAIR.

# Effect on state

Context window: added a structural audit over the repository's planned deliverables, current framework brief, populated pilot bundle, and case-study bundle stubs.

Frame: unchanged. The current frame remains statement evolution under `docs/framework_v3.md`; the changes align current bundle pages and stub signposting with that frame.

# Resulting revisions

- `pf/formal.md` — `fc-supersedes: pf/formal.md@r1`; updated from "inquiry chains and disagreement types" to statement trajectories, stages, and the contestation-only type taxonomy.
- `s/method.md` — `fc-supersedes: s/method.md@r1`; added the five-stage dynamic model, P4', and stage metadata requirement.
- `s/specification.md` — `fc-supersedes: s/specification.md@r1`; now points to `docs/framework_v3.md` as the current provisional specification and keeps v2 as historical.
- `r/overview.md` and `r/results.md` — superseded from round 1; now describe v3 as current, v2 as historical, and Step 0-9 deliverables as formal stubs.
- `reproduction/code.md` and `reproduction/data.md` — superseded; now list current framework inputs and checksums rather than a single v2 source.
- `s/foundations/*.md` — superseded from round 1 where reference sections were added. The summaries remain compact anchors, not a full Step 1 related-work review.
- Repository docs outside the bundle (`README.md`, `bundles/README.md`, Step stubs, and `docs/repository-structure-audit.md`) were updated and are ledgered here in prose because they are not bundle concept files.

# Classification rationale

This is a critique-stage round. The move probes whether the repository's file structure and links correspond to their stated purpose and fixes mismatches in current files, but it does not establish a standing counter-position against the v3 framework. Because there is no live contestation, `fc-type-at-round` is intentionally omitted.
