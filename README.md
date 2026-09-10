# asml-product-p10-if-shim

**Own the intermediate-focus (IF) contract even without owning the linac — etendue, pupil fill, polarization, pulse envelope, pointing shim researchers can bind.**

| | |
|--|--|
| Spec | [`SPEC.md`](SPEC.md) · asml-bench [#52](https://github.com/gtmsko46-debug/asml-bench/issues/52) |
| Factory | [FACTORY.md](https://github.com/gtmsko46-debug/asml-bench/blob/main/products/FACTORY.md) |
| Stage | **Spec (M0)** — package/build waits bay |

```bash
# after M1
pip install -e '.[dev]'
```

Sandbox hill-climbs live on asml-bench (`labs/p10-if-shim/shim.py (scaffold → Foreman)`); set `ASML_BENCH_ROOT` to pick up live weights once the loader exists.
