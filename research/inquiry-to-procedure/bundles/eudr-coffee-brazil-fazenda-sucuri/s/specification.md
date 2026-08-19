---
type: Method
title: "Exact configuration"
fc-level: 3
fc-axis: S
fc-round: 7
fc-supersedes: "s/specification.md@round-0006"
gsp-engine: gee
---
# Exact configuration

Counterpart commit: `GeorgeMadlis/eudr-dmi-gil@ebb74d93889b7114c629230d198ebd662044bc47`.

Evidence bundle id: `fazenda_sucuri_screening_aoi_evidence_freeze_20260812T121500Z`.

Generation command is recorded verbatim in `../reproduction/source-evidence.json`. It uses:

- `--aoi-id fazenda_sucuri_screening_aoi`
- `--out-format both`
- `--enable-hansen-post-2020-loss`
- Hansen tile directory for the legacy branch:
  `/private/tmp/fazenda_sucuri_hansen_tiles`
- JRC GFC2020 V3 raster: `out/fazenda_sucuri_screening_aoi_inputs/jrc_gfc2020_v3.tif`
- Hansen lossyear raster: `out/fazenda_sucuri_screening_aoi_inputs/hansen_lossyear_2025_v1_13.tif`
- Hansen treecover2000 raster: `out/fazenda_sucuri_screening_aoi_inputs/hansen_treecover2000_2025_v1_13.tif`
- commodity config: `out/fazenda_sucuri_screening_aoi_inputs/coffee_config_fazenda_sucuri_two_source.json`
- Sentinel-2 baseline/recent rasters and scene diagnostics JSON.

The canonical report records `EUDR_DMI_GENERATED_AT_UTC=2026-08-12T12:15:00Z` and
`EUDR_DMI_GIT_COMMIT=ebb74d93889b7114c629230d198ebd662044bc47`. Round 7 is regenerated from this
clean counterpart commit; the refreshed handoff records `counterpart_dirty: false`.

Round 2 fixes the Sentinel-2 visual-context acquisition path: baseline/recent visual rasters are
seasonal masked median composites and acquisition now fails if either visual raster has less than
98% valid coverage overall or in its left half.

Round 4 adds AOI administrative labels to the raw/canonical report model (`Minas Gerais`,
`Coromandel`) and changes canonical HTML rendering so the AOI panel displays a renderable evidence
layer with a matching legend, the AOI image uses cover fitting, and the interactive map title is
offset from the zoom controls.

Round 5 keeps the same evidence bundle id but reruns through the canonical
`python -m eudr_dmi_gil.reports.cli` entry point with the explicit Hansen post-2020-loss branch
enabled. The refreshed handoff records 59 artifacts, root manifest hash
`a4663ba4659e2689462f522e2f2fff3d97dcbe25a34d7bf17ba3d61986b4a446`, and report PDF hash
`1ca879da2898941971f07ed6c369b2a245556d7814cacc110c27b0bb3cbd4d83`. The verdict remains based on
the report's JRC-baseline commodity-overlap metrics, not on the AOI brief's no-evidence framing.

Round 6 updates the coffee temporal-mask calculation. The current coffee layer preserves
baseline-year coffee by unioning latest observed 2024 coffee with 2020 baseline coffee. The new
commodity layer remains the latest 2024 coffee mask minus the 2020 baseline coffee mask. The
refreshed handoff records 58 artifacts, root manifest hash
`5e52311b1111042a01d4845bdff0351deb9bfdd62858bae88c07647eef4b1bc4`, and report PDF hash
`47b47a0164d15bda0665c847f5b7ed6472ac3ecbc9f21bfd7ca2db80a1769709`.

Round 7 fixes the page-4 regional overview as a recurring renderer failure. The counterpart now
uses a pinned local recent Sentinel-2 raster as the offline page-4 fallback whenever no dedicated
regional raster is supplied; the OKF/GSP handoff and publish gate also treat
`regional_overview_png` as a required Brazil/coffee artifact. The refreshed handoff records 59
artifacts, root manifest hash
`a481ea836ad47bd5d4fc56c68f0191d58b24637d27674aafaeea8d5389b927de`, report PDF hash
`e5c8da5dcf11afc2fae68129b59fa5c8c0fc48029df2ba528ba9c92a0666c87d`, and page-4 regional PNG hash
`3742da15bb7b15efe4ddf56de2cca55e66eead71f814056f45a4ca6a7b40eca1`.
