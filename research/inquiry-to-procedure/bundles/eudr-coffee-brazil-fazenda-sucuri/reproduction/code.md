---
type: Runbook
title: "Counterpart code"
fc-axis: REPRO
fc-round: 7
fc-supersedes: "reproduction/code.md@round-0006"
gsp-counterpart: GeorgeMadlis/eudr-dmi-gil@ebb74d93889b7114c629230d198ebd662044bc47
---
# GS-Tools counterpart

Counterpart: `GeorgeMadlis/eudr-dmi-gil@ebb74d93889b7114c629230d198ebd662044bc47`.

The authoritative run command is recorded in `source-evidence.json:generation_command`. It generated
the report, commodity differencing, Sentinel diagnostics, evidence PNGs, HTML, PDF, manifest, and
AOI config hash in one combined canonical CLI run. Round 5 records the literal
`--enable-hansen-post-2020-loss` flag in that command.

Round 2 additionally commits `tmp/acquire_fazenda_sucuri_inputs.py` changes that prevent a
least-cloudy single-scene Sentinel-2 image with partial spatial coverage from being frozen as visual
context.

Round 4 regenerated the evidence after committing the AOI admin label and report HTML/PDF rendering
changes in the counterpart repository. The refreshed handoff records `counterpart_dirty: false`.

Round 5 first committed the focused counterpart regression-test repair
`80192bcdbde9329f1a64a60901a52a11d5fcfca8`, then regenerated the Fazenda Sucuri handoff from that
clean tree. Focused counterpart regression tests passed:
`.venv/bin/python -m pytest tests/test_generate_okf_gsp_handoff.py tests/test_brazil_coffee_report_pdf_structure.py`
reported 24 passed.

Round 6 regenerated from `GeorgeMadlis/eudr-dmi-gil@e46d9a4c833c22805dc17e50315fd814e25043a0`,
which includes the coffee temporal-mask correction. The same focused counterpart regression suite
reported 24 passed before the evidence refresh.

Round 7 committed `GeorgeMadlis/eudr-dmi-gil@ebb74d93889b7114c629230d198ebd662044bc47`, which adds
an offline regional-overview fallback in `report_model.py`, marks `regional_overview_png` required
in the handoff writer, and adds a focused regression test. Focused counterpart tests passed:
`.venv/bin/python -m pytest tests/test_canonical_report_model.py::test_regional_overview_falls_back_to_local_recent_raster tests/test_generate_okf_gsp_handoff.py`
reported 4 passed.
