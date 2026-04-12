"""GrokForge Memory Package – Tier 1-4 pluggable system."""

from .backends import MemoryBackend, MemPalaceBackend

__all__ = ["MemoryBackend", "MemPalaceBackend"]

# Default backend for GrokForge (can be swapped via config later)
default_backend: MemoryBackend = MemPalaceBackend()

def get_backend(backend_type: str = "mempalace") -> MemoryBackend:
    """Factory for future backends (Rust, vector DBs, etc.)."""
    if backend_type == "mempalace":
        return MemPalaceBackend()
    raise NotImplementedError(f"Backend {backend_type} not yet implemented (Rust hot-path coming)")
