---
type: Finding
title: Itemized current state
description: Current project state, framework-self-only pilot findings, Step 8 limits, and round 20 observer audit.
fc-level: 2
fc-axis: R
fc-status: open
fc-round: 20
fc-supersedes: r/results.md@r17
timestamp: 2026-08-16
---

- Current framework document: [docs/framework_v3.md](../../../docs/framework_v3.md), which supersedes [docs/framework_v2.md](../../../docs/framework_v2.md).
- Step 0 glossary: [docs/glossary.md](../../../docs/glossary.md), filled at an interim level.
- Step 1 related-work positioning: [docs/related-work.md](../../../docs/related-work.md), filled at an interim level.
- Step 2 formal core: [docs/formal-core.md](../../../docs/formal-core.md), filled at an interim level.
- Step 3 OKF-FC specification: [spec/SPEC.md](../../../spec/SPEC.md), filled at an interim level.
- Step 4 generator, append, and validator tooling: [tools/](../../../tools), implemented at an interim level.
- Step 5 observer-distance metrics: [docs/metrics.md](../../../docs/metrics.md), filled at an interim level.
- Step 6 derived predictions: [docs/predictions.md](../../../docs/predictions.md), filled at an interim level with falsifiable prediction designs and framework-self exploratory coding notes.
- Step 7 status: this PR completes only the framework-self longitudinal case-study pilot recorded in [inquiry/round-0016.md](../inquiry/round-0016.md). The four originally planned external case-study bundles remain deferred and are not claimed as complete.
- Step 8 limitations and falsifiability: [docs/limitations.md](../../../docs/limitations.md), filled at an interim level with adversarial limits, stage-taxonomy stress tests, behavioral and provenance failure modes, and a falsification registry.
- Round 20 observer-theory audit:
  [docs/observer-theory-audit.md](../../../docs/observer-theory-audit.md),
  added after testing observer ontology, Wolfram attribution, and bundle
  reconstruction claims.
- Framework-self metric measurements: [r/full-results.md](full-results.md), with machine-readable values in [r/metrics-rounds-0001-0013.csv](metrics-rounds-0001-0013.csv). These are a reproducible demonstration over this bundle's rounds 1-13, not validation of the framework.
- Framework-self prediction observations: [r/full-results.md](full-results.md) records genuinely computed Step 6 exploratory values over rounds 1-14, including the Prediction 8 calculation boundary. These values are not population-level validation.
- Framework-self retrospective classification: [r/retrospective-round-classification.csv](retrospective-round-classification.csv) separates contemporaneous metadata from later inferred stage/type classifications over rounds 1-15.
- P2 is a derivable proposition under the Type III assumptions stated in `docs/formal-core.md`.
- P1 is a theorem candidate under explicit complexity assumptions; otherwise a proposed extension and empirical regularity.
- P3 is a conjecture and empirical regularity about lost recorder specifications causing Type III disputes to be misread as Type II.
- P4 is derivable only under strong truthfulness, recording, monotonicity, and fairness assumptions; in the general framework it remains an empirical regularity and theorem candidate.
- P4' has a definitional part, formation precedes later stages, and a conjectural part about stage-level movement toward consolidation.
- P5 is a conjecture and theorem candidate under rich trajectory assumptions; it is not established as a repository theorem.
- Step 8 does not close the framework. It records ways the framework can fail: redundant theory, circular self-evidence, unstable stage labels, unmeasurable frames, strategic behavior, stale provenance, and failed external prediction tests.
- Step 9 remains a future paper-draft deliverable.
- This pilot bundle was created at bundle round 1 and repo round 1, then updated through the recorded inquiry rounds.

# Framework-Self Case-Study Account

Initial formation: round 1 created the self-description bundle from
`docs/framework_v2.md` and records the initial bundle input checksum
([round 1](../inquiry/round-0001.md); [reproduction/data.md](../reproduction/data.md)).
The normal PR workflow was not yet in force for that content; the current code
runbook points to initial commit `a1fc43c`
([reproduction/code.md](../reproduction/code.md)).

Rendering and publication enrichment: round 2 added static HTML inspection
([round 2](../inquiry/round-0002.md)); round 5 added self-contained snapshots,
manifest generation, and structure visualization ([round 5](../inquiry/round-0005.md));
round 6 added publish/catalog/evolution visualization and produced the first
published framework-self snapshot
([round 6](../inquiry/round-0006.md);
`../okf-bundle-snapshots/framework-self/2026-07-19-r0006-0445f09/manifest.json`).

Critique and objections: round 3 is the only contestation-stage point in the
retrospective type trajectory. It fixed two Type I mechanical defects while
leaving Type II judgment/specification residue open
([round 3](../inquiry/round-0003.md);
[retrospective CSV](retrospective-round-classification.csv)). Round 7 is
classified as critique rather than contestation because it audits and revises
stale structure/reference pages without maintaining a rival framework
([round 7](../inquiry/round-0007.md)).

Scope change and self-disagreement: round 4 superseded the narrower
observer-disagreement frame with the broader statement-evolution frame in
`docs/framework_v3.md`, making disagreement the contestation stage of a larger
trajectory ([round 4](../inquiry/round-0004.md);
[docs/framework_v3.md](../../../docs/framework_v3.md)). This is the bundle's
clearest self-disagreement and frame revision: the current repository describes
its own earlier name and scope as historically narrower, not false but
incomplete.

Consolidation and concept supersession: round 4 consolidated the new frame and
superseded `answer.md`, `pf/overview.md`, and `s/overview.md`
([round 4](../inquiry/round-0004.md)). Round 8 consolidated the repository-round
versus bundle-round distinction and superseded bookkeeping/reproduction
concepts ([round 8](../inquiry/round-0008.md);
[docs/round-ledgers.md](../../../docs/round-ledgers.md)). Later enrichment
rounds continued to supersede current concepts without erasing prior records,
including formal/method/results pages at round 11, specification at round 12,
reproduction/foundation metadata at round 13, results at rounds 14 and 15, and
this case-study layer at round 16.

Codex and Claude as sequential observers: the party sequence is Codex for
rounds 1-2, Claude for rounds 3-6, and Codex for rounds 7-16
([inquiry/index.md](../inquiry/index.md)). The repository-level workflow change
that made this a sequential multi-observer model is recorded in repository
round 4 and bundle round 4 ([log.md](../../../log.md);
[round 4](../inquiry/round-0004.md)).

Repository-round versus bundle-round divergence: round 8 records the ambiguity
caused by root repository round 8 and framework-self bundle round 7 being
different counters, then adopts the two-counter convention
([round 8](../inquiry/round-0008.md)). The r0009 published manifest records
`bundle_round: 9` and `source_repo_round: 10`, demonstrating the distinction in
a derived artifact
(`../okf-bundle-snapshots/framework-self/2026-07-20-r0009-43c1962/manifest.json`).

Stage trajectory: rounds 1-15 classify as formation, enrichment, contestation,
consolidation, enrichment, enrichment, critique, consolidation, and enrichment
for rounds 9-15. Rounds 1-3 are inferred later, while rounds 4-15 use
contemporary `fc-stage` metadata
([retrospective CSV](retrospective-round-classification.csv);
[inquiry/index.md](../inquiry/index.md)).

Contestation-type trajectory: only round 3 remains in the usable type
trajectory. Because all other rounds are non-contestation under the current
spec, their legacy or absent type values are treated as not applicable rather
than edited in place ([retrospective CSV](retrospective-round-classification.csv);
[spec/SPEC.md section 5.2](../../../spec/SPEC.md#52-round-fields)).

Measurable stalls, reversals, and oscillations: stage persistence is visible in
the enrichment runs at rounds 5-6 and 9-15, and consolidation is visibly
non-terminal because rounds 5 and 9 return to enrichment after consolidation
rounds 4 and 8 ([retrospective CSV](retrospective-round-classification.csv)).
Type stalls, type reversals, and type oscillations are not measurable because
there is only one contestation-stage round ([r/full-results.md](full-results.md)).

Limits of reconstruction: records do not support confident direct measurement
of re-litigation rate because stable issue identifiers were not recorded in
rounds 1-15 ([metrics-rounds-0001-0013.csv](metrics-rounds-0001-0013.csv)).
The record also cannot prove external validity because this is one
self-referential trajectory and the external cases are still stubs.

Limitations and falsifiability: Step 8 makes the framework's failure conditions
explicit rather than treating limitations as a defensive footnote
([docs/limitations.md](../../../docs/limitations.md);
[round 17](../inquiry/round-0017.md)). The current evidence can show that this
repository can preserve rounds, supersession, provenance notes, metrics, and
missing values. It cannot show that the taxonomy is reliable across domains,
that P1-P5 or P4'(b) hold empirically, or that explicit recording causally
reduces re-litigation. The framework remains open and provisional.

Re-litigation and trajectory influence: the bundle appears to reduce
re-litigation about its own history in specific cases: round 8 records the
round-counter ambiguity, round 9 repairs the metadata failure, and later rounds
use the two-counter convention rather than reopening it ([round 8](../inquiry/round-0008.md);
[round 9](../inquiry/round-0009.md); [round 15](../inquiry/round-0015.md)).
The bundle also influenced the trajectory it records: renderer, snapshot,
publish/catalog, metadata repair, validator, metrics, prediction, and this
classification work were all created because the bundle made those needs
inspectable ([rounds 2](../inquiry/round-0002.md),
[5](../inquiry/round-0005.md), [6](../inquiry/round-0006.md),
[9](../inquiry/round-0009.md), [13](../inquiry/round-0013.md),
[14](../inquiry/round-0014.md), [15](../inquiry/round-0015.md),
[16](../inquiry/round-0016.md)).
