"""Product reference IF shim — HT-1028 KEEP (dual HT-1033). Synthetic; not fab-grounded."""
from __future__ import annotations

PHOTON_KEEP = 1.0
FILL_GAIN = 0.40
PUPIL_FILL_TARGET = 0.72

# Dual-gate provenance
BASELINE_TICKET = "HT-1028"
DUAL_PARTNER = "HT-1033"
HOLDOUT_DIGEST = "d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be"
# Soft note (Critic/Diplomat): HT-1033 no-gain travels — do not claim mock-lane improvement.
SOFT_NOTES = ("HT-1033 soft no-gain travels",)


def shim(row: dict) -> dict:
    """Reconstruct fill from coherence/bandwidth/power; correct toward 0.72 (HT-1028)."""
    coherence = float(row.get("coherence", 0.5))
    bandwidth = float(row.get("bandwidth", 0.02))
    power_frac = float(row.get("power_frac", 0.7))
    pol = float(row.get("pol_degree", row.get("pol_contrast_proxy", 0.5)))
    pulse = float(row.get("pulse_structure", row.get("pulse_envelope_proxy", 0.5)))
    pointing = float(row.get("pointing_jitter", row.get("pointing_err_proxy", 0.05)))

    fill = 0.45 + 0.25 * coherence - 1.5 * bandwidth + 0.1 * power_frac
    fill = fill + FILL_GAIN * (PUPIL_FILL_TARGET - fill)
    fill = max(0.0, min(1.0, fill))
    pupil_err = abs(fill - PUPIL_FILL_TARGET)

    return {
        "pupil_fill_error": float(pupil_err),
        "photons_kept": float(PHOTON_KEEP * float(row.get("photons", 1.0))),
        "if_loss_db": float(1.0 + (1.0 - power_frac)),
        "pol_contrast_proxy": float(0.3 * pol),
        "pulse_envelope_proxy": float(0.4 * pulse + 8.0),
        "pointing_err_proxy": float(pointing * 1.1),
        "if_compat_score": float(max(0.0, 1.0 - pupil_err) * 0.4 + 0.6),
        "etendue_proxy": "pupil_fill_error",
    }
