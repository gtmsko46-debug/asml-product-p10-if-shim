from __future__ import annotations
import importlib.util, os, sys
from pathlib import Path
from types import ModuleType
from typing import Callable
from . import reference_shim

ShimFn = Callable[[dict], dict]
_CACHED: tuple[str, ShimFn] | None = None

def _load(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("asml_p10_shim_sandbox", path)
    if spec is None or spec.loader is None:
        raise ImportError(str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["asml_p10_shim_sandbox"] = mod
    spec.loader.exec_module(mod)
    return mod

def get_shim(*, force_reload: bool = False) -> tuple[str, ShimFn]:
    global _CACHED
    if _CACHED is not None and not force_reload:
        return _CACHED
    explicit = os.environ.get("ASML_P10_SHIM_PATH")
    if explicit:
        p = Path(explicit).expanduser().resolve()
        if p.is_dir():
            p = p / "shim.py"
        if p.is_file():
            mod = _load(p)
            fn = getattr(mod, "shim", None) or getattr(mod, "solve", None)
            if fn is None:
                raise AttributeError(str(p))
            _CACHED = (str(p), fn)
            return _CACHED
    bench = os.environ.get("ASML_BENCH_ROOT")
    if bench:
        for name in ("shim.py", "solver.py"):
            p = Path(bench).expanduser().resolve() / "labs" / "p10-if-shim" / name
            if p.is_file():
                mod = _load(p)
                fn = getattr(mod, "shim", None) or getattr(mod, "solve", None)
                if fn is None:
                    raise AttributeError(str(p))
                _CACHED = (str(p), fn)
                return _CACHED
    _CACHED = ("reference", reference_shim.shim)
    return _CACHED

def reset_loader_cache() -> None:
    global _CACHED
    _CACHED = None
