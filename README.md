# asml-product-p10-if-shim

> **Champion FREEZE (2026-09-10):** no new hills / no new tickets. This README is the ship surface — polish docs only. See asml-bench `corpus/notes/champion-freeze-2026-09-10-product-ship.md`.

Own the IF even without the linac. Mandatory axes: pupil/etendue, power, pol, pulse, pointing.

KEEP AND (eval-owned): pupil_fill_error ≤ 0.10 AND photons_kept ≥ 0.55.

```python
from asml_product_p10_if_shim import shim_if
report = shim_if(source_state)
```

M1 SEED — not product KEEP. Live: `ASML_BENCH_ROOT` / `ASML_P10_SHIM_PATH`.
Parent: asml-bench #52.
