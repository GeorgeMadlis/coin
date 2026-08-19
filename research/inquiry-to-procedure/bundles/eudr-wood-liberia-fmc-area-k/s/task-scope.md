---
type: Method
title: "Task scope"
fc-level: 2
fc-axis: S
fc-round: 4
fc-supersedes: "s/task-scope.md@round-0003"
gsp-aoi: "liberia_fmc_area_k_contract_boundary"
---
# Task Scope

The authoritative structured scope is `../bundle.json`. This page is the explicit human-readable
Frame Declaration for the Liberia wood/timber task.

## Frame Declaration

### Method-family coordinates

| dimension | value |
|---|---|
| Regulatory purpose | EUDR evidence collection/screening |
| Commodity | wood/timber |
| Conceptual method semantics | Wood evidence is a structured evidence state, not an agricultural commodity-mask intersection. |
| Method engine | `gee` parent method-family semantics inherited from `eudr-gee` |
| Method-family parent | `eudr-gee` |
| Counterpart repository role | `single-earth/eudr-dmi-gil` supplies the current handoff commit; the local checkout also has a `georgemadlis` remote. |

The method distinguishes:

- deforestation: stand-replacement or forest-loss evidence after 2020-12-31;
- forest degradation: separate disturbance/degradation evidence for forest remaining forested;
- production/source geometry: concession, AOP area, harvesting block, tree/log origin or unknown;
- source linkage / chain of custody: evidence linking source geometry to logs, shipments or
  operator records.

Evidence consists of pinned source records, clipped or referenced observations emitted by documented
processes, counterpart outputs with checksums, and documented legal/source records. It does not
consist of assumptions, synthetic replacement geometry, geographic overlap alone, or hash
verification alone.

### Task coordinates

| dimension | value |
|---|---|
| Purpose | EUDR evidence collection/screening |
| Commodity | wood/timber |
| Country | Liberia (`LR`) |
| AOI/context | Forest Management Contract Area K |
| Geometry role | forest concession |
| Role in EUDR evidence | screening AOI / legal-provenance context |
| Production-plot status | unresolved |
| Source-linkage status | missing public harvesting-block/tree/log/CoC linkage |
| Starting spatial hierarchy | `FMC Area K -> Annual Operational Plan -> Harvesting Block -> trees/logs -> Chain of Custody` |

## In-Scope Questions

- What public and counterpart-observed sources exist for Area K wood/timber screening?
- Which sources can support deforestation, degradation, forest type, legal-provenance context,
  production geometry or source-linkage evidence?
- Which Area K source, boundary or production-geometry gaps remain unresolved?
- How do legacy `eudr-gee` rounds 30 and 31 map into this clearer task frame?

## Out-Of-Scope Questions

- automatic EUDR compliance or non-compliance decisions;
- treating FMC Area K as an EUDR production plot;
- inventing AOP, harvesting-block, tree/log or shipment geometry;
- inferring shipment-to-tree linkage without evidence;
- replacing missing public evidence with synthetic geometry;
- silently generalizing Liberia-specific findings into the global wood method;
- coffee/cocoa commodity-mask semantics;
- unrelated countries or commodities.

## Round Changes

These are same-frame evidence evolution and may append rounds here:

- pinning additional public Area K source records or access failures;
- adding reproducible deforestation, degradation or confirmation process outputs for Area K;
- comparing the contract-reconstructed boundary observation with Forest Atlas and other boundary
  observations;
- adding a report/contact sheet after a report PDF is pinned;
- resolving or narrowing existing evidence gaps without changing the task identity.

## New Task Bundle Required

Create a new task bundle rather than broadening this one when the identity changes to:

- a specific shipment, loading request, log batch, operator claim or chain-of-custody event;
- a specific AOP or harvesting block that becomes the long-lived AOI identity;
- a different concession, country or commodity;
- a legal-provenance adjudication task rather than geospatial/source collection and screening.

## Method-Family Change Required

Open a method-family round in `eudr-gee`, or a successor parent if one is formed, when the change:

- alters wood verdict-class mapping or admissible outputs generally;
- changes required wood evidence-state fields;
- creates or replaces the processing engine semantics;
- converts a Liberia-specific convention into a global wood/timber rule.

Verdict/result changes do not create a new bundle by themselves. Bundle identity is fixed by the
Frame Declaration, not by a future output value.

## Scope-Change Protocol

For every proposed future move:

1. compare it against this Frame Declaration;
2. classify it as same-frame evidence evolution, task-boundary change, method-family/rule change,
   or unresolved;
3. append a round only for same-frame evidence evolution;
4. for task-boundary or method-family/rule changes, do not silently broaden this bundle; propose a
   new bundle/frame or parent round;
5. for unresolved cases, ask the human before writing.
