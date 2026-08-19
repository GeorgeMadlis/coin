---
type: Concept
title: Provenance and reproducibility
description: Engineering practices for preserving records and making results re-derivable.
fc-level: 2
fc-axis: S
fc-group: C
fc-status: open
fc-round: 13
fc-supersedes: s/foundations/provenance-reproducibility.md@r7
timestamp: 2026-07-21
---

## Summary

W3C 2013 provenance standards describe entities, activities, and agents involved in producing records. Wilkinson 2016 FAIR principles emphasize that data should be findable, accessible, interoperable, and reusable. Reproducibility practice adds pinned code, datasets, environments, and checksums. These are engineering answers to the problem of later re-derivation.

## What it explains

It explains how to keep evidence and computation traceable enough for later observers to inspect or re-run.

## What it fails to explain

It does not by itself provide a theory of why observers disagree or how disagreement types change over statement trajectories.

## What this framework adds

This framework adds a disagreement theory on top of provenance practice. Its explicit recording function treats provenance as the defense against Type III disputes, while its computational-boundedness dimension explains why full provenance may still leave hard Type II translation problems.

## Classification

Addresses Type I and Type III in both static and sequential regimes.

## References

- Paul Groth and Luc Moreau, eds., "An Overview of the PROV Family of Documents," W3C Working Group Note, 30 April 2013. [W3C](https://www.w3.org/TR/prov-overview/).
- Mark D. Wilkinson et al., "The FAIR Guiding Principles for scientific data management and stewardship," Scientific Data 3, 2016. DOI: [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18).
