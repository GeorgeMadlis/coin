---
inquiry: inquiry-to-procedure
title: From Inquiry to Procedure — Human–AI Research as Progressive Reduction
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

- **C0** *[inferential]* The methodological value of a recorded human–AI inquiry trajectory lies in progressive reduction — turning an underspecified problem into deterministic procedures, improved AI instructions, and explicitly retained uncertainty — rather than in indefinite preservation of every step.
- **C0-neg** *[inferential]* The defensible negative: the trajectory has little methodological value if the same procedure, instructions, and open-question set can be derived reliably from the final evidence alone, or if intermediate states mainly propagate obsolete assumptions and scope errors. This negative is available, which is what makes C0 falsifiable.

## Boundedness of inquiry

- **C1** *[inferential]* Human and AI inquiry are both bounded, and the bounds compound: a human's partial command of the relevant science produces an incomplete decomposition, and the model executing within that frame can amplify rather than question it.
- **C2** *[inferential]* Recording an inquiry is methodologically useful only when the record helps expose and repair framing errors, not when it merely stores them. (Distinguishes a documenting log from a correcting log.)

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

- **C14** *[inferential]* Three readings of the log compete: (a) provenance record; (b) external memory; (c) intermediate representation / compilation substrate. The external-memory reading is the strongest rival to (c) and was the inquiry's own earlier position.
- **C15** *[inferential]* The external-memory reading justifies indefinite retention and gives no account of when history should stop being consulted — its principal weakness relative to the compilation reading.

## Critical synthesis

- **C16** *[inferential]* The two cases support the weaker core of C0 (reduction into procedure / instruction / retained uncertainty is demonstrable) but do not establish the strong general form (that recorded inquiry generally reduces error or transfers across problems).
- **C17** *[sourced: repository state — fabricated-input episode]* "Deterministic" is not "true": hashes and reruns preserved an invalid evidence state until later inquiry exposed a source-authenticity problem. Reproducibility preserves whatever it is given, including error.
- **C18** *[inferential]* A reduction may be retired from routine computation only after it has itself survived scrutiny; for a public research trail the historical trajectory should be archived rather than deleted even after it leaves the AI's operational context.

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
