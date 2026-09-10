"""SEED IF shim — synthetic; not product KEEP. Mirrors IF Spec FEL-10 contract axes."""
from __future__ import annotations


def shim(row: dict) -> dict:
    coherence = float(row.get("coherence", 0.5))
    bandwidth = float(row.get("bandwidth", 0.02))
    power_frac = float(row.get("power_frac", 0.7))
    pol = float(row.get("pol_degree", 0.5))
    pulse = float(row.get("pulse_structure", 0.5))
    pointing = float(row.get("pointing_jitter", 0.05))

    fill = 0.55 + 0.25 * coherence - 2.0 * bandwidth
    fill = max(0.0, min(1.0, fill))
    pupil_fill_error = abs(fill - 0.72)

    photons_kept = max(0.0, min(1.0, power_frac * (0.85 + 0.1 * coherence)))
    if_loss_db = 0.8 + 0.4 * (1.0 - photons_kept)
    pol_contrast_proxy = 0.35 * pol
    pulse_envelope_proxy = pulse
    pointing_err_proxy = pointing
    if_compat_score = max(0.0, 1.0 - pupil_fill_error) * 0.5 + photons_kept * 0.5

    return {
        "pupil_fill_error": float(pupil_fill_error),
        "photons_kept": float(photons_kept),
        "if_loss_db": float(if_loss_db),
        "pol_contrast_proxy": float(pol_contrast_proxy),
        "pulse_envelope_proxy": float(pulse_envelope_proxy),
        "pointing_err_proxy": float(pointing_err_proxy),
        "if_compat_score": float(if_compat_score),
        "etendue_proxy": "pupil_fill_error",
    }
