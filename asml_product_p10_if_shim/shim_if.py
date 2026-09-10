"""Champion-facing IF shim API — IF Spec FEL-10 contract axes."""
from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Mapping
from .loader import get_shim

ASSUMPTION_CARDS = (
    "coherence-if-v1",
    "fel-source-v1",
    "imaging-optics-v1",
    "fel-scanner-twin-v1",
)
KEEP_AND = "pupil_fill_error<=0.10 AND photons_kept>=0.55"

@dataclass
class IfShimReport:
    pupil_fill_error: float
    photons_kept: float
    if_loss_db: float
    pol_contrast_proxy: float
    pulse_envelope_proxy: float
    pointing_err_proxy: float
    if_compat_score: float
    etendue_proxy: str = "pupil_fill_error"
    assumption_cards: tuple[str, ...] = ASSUMPTION_CARDS
    keep_and_rule: str = KEEP_AND
    shim_source: str = "reference"
    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["assumption_cards"] = list(self.assumption_cards)
        return d

def shim_if(row: Mapping[str, Any]) -> IfShimReport:
    source, fn = get_shim()
    out = fn(dict(row))
    for key in (
        "pupil_fill_error",
        "photons_kept",
        "if_loss_db",
        "pol_contrast_proxy",
        "pulse_envelope_proxy",
        "pointing_err_proxy",
        "if_compat_score",
    ):
        if key not in out or out[key] is None:
            raise KeyError(f"IF axis missing/null: {key}")
    return IfShimReport(
        pupil_fill_error=float(out["pupil_fill_error"]),
        photons_kept=float(out["photons_kept"]),
        if_loss_db=float(out["if_loss_db"]),
        pol_contrast_proxy=float(out["pol_contrast_proxy"]),
        pulse_envelope_proxy=float(out["pulse_envelope_proxy"]),
        pointing_err_proxy=float(out["pointing_err_proxy"]),
        if_compat_score=float(out["if_compat_score"]),
        etendue_proxy=str(out.get("etendue_proxy", "pupil_fill_error")),
        shim_source=source,
    )
