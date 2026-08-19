---
type: Claim
title: "Full context"
fc-level: 3
fc-axis: PF
fc-round: 5
fc-supersedes: "pf/full-context.md@round-0001"
gsp-aoi: "liberia_fmc_area_k_contract_boundary"
---
# Full Context

The parent method records that EUDR wood/timber cannot be represented by the coffee-style
`baseline and loss and commodity mask` path without semantic distortion. Wood requires separate
deforestation and degradation evidence, and it requires an explicit source/provenance geometry state.

The Liberia public-source assessment at `inputs/liberia-eudr-wood-data-source-assessment.md`
records FMC Area K as a user-supplied concession boundary with contract-stated area 266,910 ha and
a reconstructed straight-chord area of approximately 266,342.1 ha. The Forest Atlas FMC layer
independently returns FMC `"K"` as contract number `FMC-005`, company `International Consult
Capital`, active status and `area_ha = 266910`.

This bundle keeps those observations separated:

- the user/contract-reconstructed GeoJSON is a source-grounded approximation;
- the Forest Atlas polygon is an allocation-boundary observation artifact emitted by an
  administrative publication/query process;
- neither polygon is a harvesting block, tree/log origin or chain-of-custody record;
- disagreement between boundaries is context for review, not a silent replacement.

The source-authenticity dimension is still a limitation: this bundle can record pinned counterpart
paths and hashes, but it does not prove that a public or user-supplied source is legally authentic
unless a future round pins and validates that source-authenticity evidence.
