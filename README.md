# asml-product-p10-if-shim

> **Champion docs:** [asml-factory-showcase](https://github.com/gtmsko46-debug/asml-factory-showcase) (single narrative surface — avoid duplicate writeups).

Own the IF even without the linac. Mandatory axes: pupil/etendue, power, pol, pulse, pointing.

KEEP AND (eval-owned): pupil_fill_error ≤ 0.10 AND photons_kept ≥ 0.55.

```python
from asml_product_p10_if_shim import shim_if
report = shim_if(source_state)
```

## Product sync (merge review)

| | |
|--|--|
| Baseline | **HT-1028** → bundled `reference_shim` |
| Dual | HT-1028 ∧ **HT-1033** (Diplomat DUAL-KEEP) |
| Soft note | **HT-1033 soft no-gain travels** — do not claim mock-lane gain |
| HOLDOUT | `d0dc1f8a…` |
| Promote | **No auto-promote** — Lab Dir / IF Spec merge review |

Live override: `ASML_BENCH_ROOT` / `ASML_P10_SHIM_PATH`. Parent: asml-bench #52.
