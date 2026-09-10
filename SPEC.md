# asml-product-p10-if-shim — Product Spec

**Parent:** asml-bench [#52](https://github.com/gtmsko46-debug/asml-bench/issues/52)  
**Showcase:** [asml-factory-showcase](https://github.com/gtmsko46-debug/asml-factory-showcase) (canonical decks / product pages — avoid docs sprawl)  
**Stage:** M2 Dual-KEEP stamped → **M3 product sync (this PR, merge review)**  
**Rule:** Bots orchestrate; solver/sandbox via lasercode (Foreman→Operator). Docs/product sync PRs OK offline. **No auto-promote.**

## Champion job
Own the intermediate-focus (IF) contract even without owning the linac — etendue, pupil fill, polarization, pulse envelope, pointing shim researchers can bind.

## Public API
```python
from asml_product_p10_if_shim import shim_if
report = shim_if(source_state)
```

## Product baseline (this sync)
| Field | Value |
|-------|-------|
| `reference_shim` | **HT-1028** KEEP (Grok) |
| Dual partner | **HT-1033** (mock-mistral) — DUAL-KEEP STAMPED |
| Soft note | **HT-1033 soft no-gain travels** — must stay visible in SPEC/README; do not claim mock-lane improvement |
| HOLDOUT | `d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be` |
| Metrics (1028) | pupil_err=0.0895; photons_kept=1.0000 |
| Metrics (1033) | pupil_err=0.0950; photons_kept=1.0000 |
| Critic / Repro / Diplomat | PASS / PASS / DUAL-KEEP STAMP |
| VOID lesson | HT-1029 hardcode VOID; HT-1032 VOID (pupil_in−k / PUPIL_CORRECT write-down) — no dual claims |


## Sacred KEEP ANDs (IF Spec)

Cite: asml-bench [`tickets/IF_SPEC_FEL10_CONTRACT.md`](https://github.com/gtmsko46-debug/asml-bench/blob/main/tickets/IF_SPEC_FEL10_CONTRACT.md).

| Gate | Rule |
|------|------|
| **KEEP AND** | `pupil_fill_error ≤ 0.10` **∧** `photons_kept ≥ 0.55` |
| Soft score | `if_compat_score` ranks only — **never KEEP alone** |
| Holdout power | holdout mean `photons_kept == 1.0` required; discard / `< 1.0` → **hard VOID** |

Axes list alone is **not** the threshold stamp. Package `KEEP_AND` string mirrors the contract; ship copy must not treat soft `0.4*(1−pupil)+0.6` floor as KEEP.

## IF Spec axes (mandatory)
`pupil_fill_error`, `photons_kept`, `if_loss_db`, `pol_contrast_proxy`, `pulse_envelope_proxy`, `pointing_err_proxy`, `if_compat_score`

## KEEP / promote bar
- Dual-provider KEEP on same frozen eval + digest
- Critic clear (no oracle / residual write-down)
- Repro Bot clean-tree PASS
- Diplomat dual stamp before product `reference_*` sync
- **Merge review required** — dual-KEEP ≠ auto-promote

## Must not
- Edit `eval.py` / fixtures from solver tickets
- Ship single-provider KEEP as product baseline
- Claim fab-grounded numbers (synthetic cards only)
- Drop soft no-gain on HT-1033 from ship docs

## Milestones
1. M0 Spec — done
2. M1 Package — done
3. M2 Dual-gate HT-1028∧HT-1033 — stamped
4. **M3 Ship** — this PR: `reference_shim` ← HT-1028 + soft notes (await merge review)
