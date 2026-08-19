---
type: Method
title: Modeling
fc-level: 2
fc-axis: S
fc-round: 8
fc-supersedes: s/modeling.md@round-0004
gsp-aoi: liberia_fmc_area_k_contract_boundary
---
# Modeling

This bundle uses the parent `eudr-gee` wood evidence-state shape:

```yaml
wood_evidence_state:
  deforestation:
    state: underdetermined
    observers: []  # process/run labels, not static raster artifacts
    area_by_source_ha: {}
  degradation:
    state: underdetermined
    observers: []  # process/run labels, not static raster artifacts
    area_by_source_ha: {}
  production_geometry:
    role: concession
    production_plot_status: unresolved
  harvest_or_source_linkage:
    state: missing
  legal_provenance_context:
    state: present/incomplete
  evidence_conflicts: []
  evidence_gaps: []
  manual_review_required: true
```

Round 4 populates this state from the verified `area-k-real-005` report:

```yaml
wood_evidence_state:
  deforestation:
    state: detected_for_screening
    observers:
      - hansen_loss_on_jrc_gfc2020_baseline_run
      - jrc_tmf_deforestation_year_run
      - radd_sentinel1_confirmed_alert_run
    area_by_source_ha:
      hansen_loss_on_jrc_gfc2020_baseline: 10914.48
      hansen_loss_on_hansen10pct_baseline: 11216.61
      jrc_tmf_deforestation_on_gfc2020_baseline: 5386.32
      radd_confirmed_alerts: 13502.16
      radd_low_confidence_alerts: 4569.93
  degradation:
    state: detected_for_screening
    observers:
      - jrc_tmf_degradation_year_run
      - radd_sentinel1_alert_run
    area_by_source_ha:
      jrc_tmf_degradation_on_gfc2020_baseline: 7088.13
      radd_confirmed_alerts: 13502.16
      radd_low_confidence_alerts: 4569.93
  production_geometry:
    role: concession
    production_plot_status: unresolved
  harvest_or_source_linkage:
    state: missing
  legal_provenance_context:
    state: present/incomplete
  manual_review_required: true
```

The `observers` labels above refer to observation-producing process/run families, not to static
raster files. Differing areas across Hansen/JRC, TMF and RADD are reported as source/process
disagreement and different operational definitions, not averaged and not treated as automatic
contradictions. No non-wood commodity layer is converted into wood attribution, and no missing source
linkage is turned into a zero.
