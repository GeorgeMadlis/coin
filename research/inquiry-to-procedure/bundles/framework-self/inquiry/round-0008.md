---
type: Event
title: "Round 8: repository and bundle round scopes clarified"
description: "Round-scope policy clarified: repository rounds and bundle rounds are separate counters; manifests/catalogs record both; snapshots remain named by bundle round."
fc-axis: INQUIRY
fc-round: 8
fc-move: frame-change
fc-stage: consolidation
fc-party: codex
fc-touches: [agent-contract.md, s/specification.md, reproduction/code.md, reproduction/data.md]
fc-status: open
timestamp: 2026-07-20
---

# Move

The human objection identified a real ambiguity: root `log.md` had advanced to repository round 8 while `bundles/framework-self/` had advanced to bundle round 7. A manually named viewer artifact `r0008` was therefore misleading because its internal bundle index and manifest correctly reported bundle round 7. The corrected approach is to use two explicit counters.

# Evidence added

- [docs/round-ledgers.md](../../../docs/round-ledgers.md) defines repository rounds and bundle rounds.
- `docs/agent-guide.md` now states when each ledger is updated and when affected bundles must be published.
- `docs/framework_v3.md` now states that published snapshots are named by bundle round and record `source_repo_round` separately.
- `okf-fc` manifests and catalogs now carry both bundle round and source repository round.

# Effect on state

Context window: added the root repository ledger and the `framework-self` bundle ledger as distinct records with different scopes.

Frame: changed from an overloaded "round" vocabulary to a two-counter model: `repo_round` for root repository history, `bundle_round` for each bundle's statement trajectory. This resolves apparent round-number divergence without renaming generated bundle artifacts to numbers they do not contain.

# Resulting revisions

- `agent-contract.md` — `fc-supersedes: agent-contract.md@r1`; now instructs agents to distinguish repository and bundle rounds and publish affected bundles.
- `s/specification.md` — `fc-supersedes: s/specification.md@r7`; now points to the round-ledger policy.
- `reproduction/code.md` and `reproduction/data.md` — superseded to record the current generation inputs and publishing command.
- Tooling (`tools/src/okf_fc/{render,catalog,publish,cli}.py`) and tests updated so manifests/catalogs expose `source_repo_round` separately from bundle round.

# Classification rationale

This is a consolidation-stage frame-change: the round adopts a clearer bookkeeping convention after an ambiguity was exposed. It does not maintain a rival position, and it is not a contestation-stage disagreement; `fc-type-at-round` is intentionally omitted.
