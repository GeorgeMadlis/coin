---
inquiry: inquiry-to-procedure
title: From Inquiry to Procedure — Recorded Inquiry, Method Evolution, and Operational Method
status: draft
updated: 2026-08-19
---

# Claims ledger

Each claim is tagged:

- **[sourced]** — supported directly by a cited external source or by the recorded repository state.
- **[inferential]** — a defensible reading built on sourced material, but not stated by any source verbatim.
- **[flagged]** — asserted in the inquiry but not yet adequately verified; needs work before it can be relied on.

The originating proposition and its negative are recorded first so that later claims can be checked against them.

## Proposition under test

- **C0** *[inferential]* Recorded human–AI inquiry is primarily provenance of method formation: a historical record of observable assumptions, corrections, supersessions, frame changes, evidence changes, rejected approaches, and state transitions. Its methodological value, if any, lies in whether a disciplined method-evolution protocol can use that provenance to produce or revise a more reliable operational method than could be obtained from the current evidence/state alone.
- **C0-neg** *[inferential]* The defensible negative: if history-blind derivation from the final evidence/problem reliably produces the same or a better operational method, and archived provenance provides no material advantage during later method revision, then the trajectory's durable role is provenance/auditability rather than a necessary component of method. This negative has not been tested by the existing two-bundle analysis.
- **C0a** *[inferential]* The inquiry should distinguish three objects: recorded trajectory `H`; method-evolution protocol `P`, which decides what a finding becomes; and operational method `M`, consisting of the specifications, code, tests, validators, AI instructions, evidence semantics, decision procedures, and explicit unresolved questions required to perform the task now.
- **C0b** *[inferential]* Routine execution should normally use `M + current/new evidence E -> result`, not `H + M + E -> result`. Archived trajectory may become relevant again when revising `M`, for example after a contradiction, source-authenticity failure, frame change, unexplained constraint, scope drift, or evidence that the current method is inadequate.

## Boundedness of inquiry

- **C1** *[inferential]* Human and AI inquiry are both bounded, and the bounds compound: a human's partial command of the relevant science produces an incomplete decomposition, and the model executing within that frame can amplify rather than question it.
- **C2** *[inferential]* Recording an inquiry is methodologically useful for method formation or revision only when a process can use the record to expose and repair framing errors, identify superseded assumptions, or explain why an operational constraint exists. Mere storage is provenance/auditability, not itself an operational rule.

## Evidence base — the two trajectories

- **C3** *[sourced: repository state]* Two recorded human–AI trajectories are used as evidence: the observer-disagreement framework (general, partly self-referential) and the EUDR geospatial evidence repository (applied).
- **C4** *[sourced: repository state]* The geospatial repository's early architecture was shaped around coffee; later work established that wood requires a materially different evidence structure — degradation, production geometry, source linkage.
- **C5** *[sourced: repository state]* The geospatial agent contract now requires agents to review sibling history while prohibiting silent generalisation of dataset-specific thresholds, commodity-specific inference, AOI assumptions, country source hierarchy, legal interpretation, and evidence semantics.

## EUDR regulatory decomposition

- **C6** *[sourced: EUR-Lex 32023R1115, consolidated 2025-12-26]* EUDR defines a deforestation-free condition common across the relevant commodities in terms of land not subject to deforestation after 31 December 2020.
- **C7** *[sourced: EUR-Lex 32023R1115, Art. 3]* Article 3 prohibits relevant commodities and products from being placed or made available on the Union market, or exported, unless the regulation's conditions are met.
- **C8** *[sourced: EUR-Lex 32023R1115]* EUDR due diligence requires geolocation of the plots where the relevant commodities were produced; a remote-sensing observation that deforestation occurred somewhere is not sufficient without production linkage.
- **C9** *[sourced: EU environment FAQ, 5th iteration]* Wood carries an additional condition concerning harvesting without inducing forest degradation after the cutoff.
- **C10** *[inferential]* Given C6–C9, the method decomposes more cleanly as Layer A (commodity-independent land evidence) → Layer B (production linkage) → Layer C (commodity-specific evidence) than as either a "coffee method" or a "wood method."
- **C11** *[inferential]* The deforestation test is not fully independent of commodity semantics, because the product must be connected to the relevant production geometry (Layer B couples A and C).

## Source evaluation

- **C12** *[sourced: repository state]* The logs record observable state transitions — supersessions, corrections, boundary changes, produced artefacts — but not the full human thought process or model internal reasoning.
- **C13** *[inferential]* Therefore the trajectories support claims about research-state evolution, not a complete cognitive reconstruction of either party.

## Competing interpretations

- **C14** *[inferential]* "Provenance," "external memory," and "compilation substrate" name roles at different conceptual levels rather than mutually exclusive interpretations. Provenance describes what the record is epistemically; external memory describes one possible access/use pattern; compilation substrate describes one possible role the record can play inside a transformation process.
- **C15** *[inferential]* The process that consumes recorded provenance and decides whether a finding becomes code, test, validator, specification, agent instruction, evidence-semantic rule, unresolved question, or provenance-only is best treated as a candidate method-evolution protocol, not as the recorded trajectory itself.

## Critical synthesis

- **C16** *[inferential]* The two bundles support a narrow empirical claim: recorded findings were observably transformed into later code, tests, specifications, instructions, evidence semantics, and explicit uncertainty. They do not establish that the recorded history was necessary to obtain those artifacts, that history-aware derivation beats history-blind derivation, or that replaying history is necessary for routine execution.
- **C17** *[sourced: repository state — fabricated-input episode]* "Deterministic" is not "true": hashes and reruns preserved an invalid evidence state until later inquiry exposed a source-authenticity problem. Reproducibility preserves whatever it is given, including error.
- **C18** *[inferential]* A recorded trajectory should generally be archived rather than deleted, but once a finding has been successfully compiled into the operational method and independently scrutinized, unnecessary history can leave routine active context. Archived provenance should be reactivated for method revision when current practice fails or becomes unexplained.

## Terminology discipline

- **C19** *[flagged]* Wolfram's computational irreducibility and bounded-observer vocabulary is used as naming, not as demonstrated explanation. Claim to guard against: treating the mere absence of a discovered deterministic reduction as evidence of genuine irreducibility.

## Evidence provenance — committed bundles (resolves V1, V2)

The source `observer-disagreement-framework` repository is private; its public evidence is the
committed `framework-self` bundle. The applied EUDR evidence uses the public
`geospatial-evidence-framework` Fazenda Sucuri bundle, copied into COIN as a reading snapshot with
JSON, GeoJSON, PDF, and canonical `report.html` artifacts omitted. Bundle-sourced claims below
upgrade the earlier generic "repository state" tag to specific round/file references.

- **C3′** *[sourced: bundles/framework-self/log.md; bundles/eudr-coffee-brazil-fazenda-sucuri/log.md]* Two committed bundles: framework-self (20 rounds, parties codex/claude) and the Fazenda Sucuri EUDR coffee bundle (7 native rounds).
- **C4′** *[sourced: bundles/eudr-coffee-brazil-fazenda-sucuri/log.md; bundles/eudr-coffee-brazil-fazenda-sucuri/answer.md]* The applied trajectory records repeated conversion of review findings into corrected artifacts: Sentinel-2 visual repair, AOI label/report-map fixes, coffee temporal-mask correction, and page-4 regional-overview repair, while preserving the screening verdict class.
- **C5′** *[sourced: bundles/eudr-coffee-brazil-fazenda-sucuri/s/task-scope.md; bundles/eudr-coffee-brazil-fazenda-sucuri/s/gsp-mapping.md]* The task scope fixes EUDR coffee screening for Brazil/Minas Gerais/Fazenda Sucuri and keeps production/evidence linkage explicit rather than silently generalizing from a commodity mask alone.
- **C-schema** *[sourced: bundles/eudr-coffee-brazil-fazenda-sucuri/s/modeling.md; bundles/eudr-coffee-brazil-fazenda-sucuri/r/results.md]* The modeling and results separate FDP-only, MapBiomas-only, and both-source agreement signals; new coffee/post-2020 loss overlap is source-specific rather than averaged into a single warrant.
- **C-frame4** *[sourced: bundles/framework-self/inquiry/round-0004.md]* Round 4 records a human-instructed scope widening (observer disagreement → statement evolution) as a frame transition f(t)→f(t+1) with SHA256 hashes and fc-supersedes on answer/pf/s pages. Direct support for C1–C2 and the "human framing is itself under inquiry" claim.
- **C-wolfram** *[sourced: bundles/framework-self/inquiry/round-0019.md; s/specification.md]* Rounds 18–19 make Wolfram observer theory a mandatory `fc-foundation-role: formal-analogy` disclosure with validator rejection conditions; specification frontmatter records `fc-irreducibility: none`. Upgrades C19 from [flagged] to [sourced].
- **C-metrics** *[sourced: bundles/framework-self/r/metrics-rounds-0001-0013.csv]* Frame-change frequency 2/13; observer-handoff 2/12; observer-distance family NOT_MEASURABLE with stated reasons; round 14 excluded to avoid circular self-measurement. Support for C12–C13 and C16's honest-negative half.
- **C-review** *[sourced: bundles/eudr-coffee-brazil-fazenda-sucuri/answer.md]* Current answer is `human_review_required`, provenance `pinned-not-reproduced`; the bundle records a screening flag, not a legal non-compliance determination. Support for C17–C18 and the structural human-in-the-loop boundary.

## Items still to verify

- **V3** Re-check C6–C9 against the current consolidated EUDR text and latest environment FAQ iteration at publication time; the cutoff date and Article 3 wording are stable, but degradation-condition phrasing has moved across FAQ iterations.
- **V4** No measurement yet exists for C16's open part (does compression reduce error recurrence?); mark as unresolved, not supported. The framework-self metrics confirm this is NOT_MEASURABLE from the current record, not merely unmeasured.
- **V5** Resolved in the committed COIN snapshot: the framework-self `_site/` rendered tree is not present; Markdown source and CSVs are retained; the applied EUDR bundle is the Fazenda Sucuri reading snapshot, with JSON, GeoJSON, PDF, and canonical `report.html` artifacts omitted.
- **V6** Some framework-self commit refs read "NOT AVAILABLE until merge" (rounds 19–20); pin the committed snapshot to a resolved state or note them as pending.
- **V7** No controlled comparison has yet tested history-aware derivation against history-blind derivation: competent agents given the same problem and final evidence, with only one condition receiving the recorded trajectory.
- **V8** No controlled method-revision experiment has yet tested whether archived provenance materially improves diagnosis and revision when the current operational method encounters a contradiction, unexplained rule, frame failure, source-authenticity problem, or new class of case.
