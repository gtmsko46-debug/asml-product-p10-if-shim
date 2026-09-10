# asml-product-p10-if-shim — Product Spec (M0)

**Parent:** asml-bench [#52](https://github.com/gtmsko46-debug/asml-bench/issues/52)  
**Stage:** Spec → Build → Review → Ship  
**Rule:** Bots orchestrate; all *solver/sandbox* code via lasercode (Foreman→Operator). Docs/spec PRs OK offline.

## Champion job
Own the intermediate-focus (IF) contract even without owning the linac — etendue, pupil fill, polarization, pulse envelope, pointing shim researchers can bind.

## Public API (target)
```python
from asml_product_p10_if_shim import shim_if
out = shim_if(source_state=..., if_targets=...)
```

## Lab bind
| Field | Value |
|-------|-------|
| Sandbox | `labs/p10-if-shim/shim.py (scaffold → Foreman)` |
| Frozen eval | product eval to bind IF Spec Owner floor + FEL-10 card when stamped |
| Assumption card | `if-ownership-v1` |
| Dual-gate | dual-gate; LPP Reality Warden may challenge IF claims vs tin-LPP fixtures |
| HOLDOUT | pin when EI freezes product holdout (no eval edits by solvers) |

## KEEP / promote bar
- Dual-provider KEEP on same frozen eval + digest
- Critic clear (no oracle / metric reuse)
- Repro Bot clean-tree PASS
- Diplomat dual stamp before product `reference_*` sync

## Must not
- Edit `eval.py` / `fixture/*` from solver tickets
- Ship single-provider KEEP as product baseline
- Claim fab-grounded numbers (synthetic cards only)

## Milestones
1. **M0 Spec** — this document + README champion job (this PR)
2. **M1 Package** — importable module + SEED `reference_*` + tests
3. **M2 Dual-gate** — HT pair via Foreman; Critic+Repro+Diplomat
4. **M3 Ship** — `reference_*` sync + ship-queue Issue close

## Bay
Queued behind P1 deepen / P2 HT-1023/1024 unless CoS assigns spare Operator. Spec/docs do not steal bay.
