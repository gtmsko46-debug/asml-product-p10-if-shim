import pytest
from asml_product_p10_if_shim import KEEP_AND, shim_if
from asml_product_p10_if_shim.loader import reset_loader_cache

@pytest.fixture(autouse=True)
def _env(monkeypatch):
    monkeypatch.delenv("ASML_BENCH_ROOT", raising=False)
    monkeypatch.delenv("ASML_P10_SHIM_PATH", raising=False)
    reset_loader_cache()

def test_axes_present():
    r = shim_if({"coherence": 0.8, "bandwidth": 0.01, "power_frac": 0.75,
                 "pol_degree": 0.6, "pulse_structure": 0.7, "pointing_jitter": 0.02})
    assert r.pupil_fill_error >= 0
    assert 0 <= r.photons_kept <= 1
    assert r.pol_contrast_proxy is not None
    assert r.pulse_envelope_proxy is not None
    assert r.pointing_err_proxy is not None
    assert "pupil" in KEEP_AND

def test_etendue_is_pupil_proxy():
    r = shim_if({"coherence": 0.5})
    assert r.etendue_proxy == "pupil_fill_error"
