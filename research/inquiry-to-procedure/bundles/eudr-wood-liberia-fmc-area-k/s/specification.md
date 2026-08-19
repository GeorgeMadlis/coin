---
type: Method
title: Specification
fc-level: 3
fc-axis: S
fc-round: 8
fc-supersedes: s/specification.md@round-0004
gsp-engine: gee
gsp-aoi: liberia_fmc_area_k_contract_boundary
---
# Specification

Current round-4 pins:

- Counterpart repository: `single-earth/eudr-dmi-gil`.
- Counterpart commit:
  `61285bd6ac2ef45708dee660620bd9db4181d3c2`.
- Evidence handoff:
  `/Users/server/projects/eudr-dmi-gil/out/okf_handoffs/eudr-wood-liberia-fmc-area-k.json`.
- Handoff SHA-256:
  `1658fc3fde056d0a154f50dd8b36c78974185323115e863f766951920b50a142`.
- Manifest SHA-256:
  `bef58f2d0c372231d76e8b213eb929884f6acd60a8a01de476998fb78f457084`.
- Report JSON/HTML/PDF SHA-256:
  `5e67f0e069d97ebbb1a44c5ff6691df9888bb872dbfe94068cd70f90f2a05922`,
  `db115bf4829b98c6e0703d98e110929d05c6a84edc93859757ecc814f1e95a42`,
  `8a065c495ead890082948e48a0c913dae9c84de9ef02ddf4269d13dbad50ebc1`.
- Metrics CSV SHA-256:
  `c890c51427d5c2024f9d0a5a8412791975b3a85852333d2057155b2d8e73c13c`.
- Report page count: `12`.
- Analysis target CRS/resolution: `EPSG:6933`, `30 m`, nearest-neighbour categorical alignment.
- Evidence temporal window: `2021-2025` after cutoff date `2020-12-31`.

Current source pins include:

- AOI GeoJSON SHA-256:
  `db386f478d9b461418155cb5db4ed9bd70d26d0b554786d61e76aad6280a210b`.
- JRC GFC2020 V3 raster SHA-256:
  `00e59adfd855b7b79693ffec38b485feacee64a5c2c471705844c7b0f48ac5ac`.
- Hansen GFC v1.13 lossyear SHA-256:
  `d4cdb9d3426e0b4e371b5af694db7d0f8c7e421a8353e37b8bfc6bac0bf7af1c`.
- Hansen treecover2000 SHA-256:
  `117803b6657a9c9bf081215a3c5d5b47136ae578f0163a251ef18b3e2d3b9024`.
- TMF deforestation/degradation/duration/intensity SHA-256:
  `76d6b1657735a7eade01c593ec789008fde27b0ca266e90fe60021d4e2274274`,
  `469fc82fcf1d3f54264c06c4d1dcbd9b5c9698811e055ff2ffc524b098d7ecb3`,
  `0ca9d52d4daa28835f3dd8edc8613f6fe9b43b2a18fea45389cc9a3abc0398e7`,
  `3be18e4e4cdd4790819d9b7b4692d9b26bc08bd8aa6cd202a12c1812251ca86e`.
- RADD Alert/Date SHA-256:
  `691ff92c4790d91643e10046b7fe826c43c1d6661826edae76f79581ab8800bb`,
  `a416bc69a3b8f47d83cdb9ad1741ef4f5047dc099ec6674c66c2a1807950402a`.

Known limitation: the local counterpart checkout has untracked derived outputs, but its tracked tree
was clean and the handoff records `counterpart_dirty: false`. This bundle records the clean commit
and handoff state as references. It does not treat untracked local output as source.
