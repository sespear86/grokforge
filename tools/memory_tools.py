"""GrokForge Tool Registry – Tier 4 MemPalace tools (pluggable for swarm)."""
from memory.backends import MemPalaceBackend
from typing import Dict, List, Any

# Global backend instance (lazy init – ready for swarm agents)
_mem_backend = None

def _get_backend():
    global _mem_backend
    if _mem_backend is None:
        _mem_backend = MemPalaceBackend()
    return _mem_backend

def mempalace_status() -> Dict:
    """Tool: mempalace_status – returns full palace health."""
    return _get_backend().status()

def mempalace_query(query: str, limit: int = 10) -> List[Dict]:
    """Tool: mempalace_query – natural-language spatial memory search."""
    return _get_backend().query(query, limit)

def mempalace_mine(text: str, metadata: Dict = None) -> Dict:
    """Tool: mempalace_mine – store new knowledge + metadata."""
    return _get_backend().mine(text, metadata or {})

def mempalace_wake(drawer_id: str) -> Dict:
    """Tool: mempalace_wake – retrieve exact drawer by ID."""
    return _get_backend().wake(drawer_id)

def mempalace_wake_up() -> Dict:
    """Tool: mempalace_wake_up – full GrokForge wake-up sequence."""
    return _get_backend().wake_up()

# Registry hook for swarm / ReAct / any agent system
MEMORY_TOOLS = {
    "mempalace_status": mempalace_status,
    "mempalace_query": mempalace_query,
    "mempalace_mine": mempalace_mine,
    "mempalace_wake": mempalace_wake,
    "mempalace_wake_up": mempalace_wake_up,
}

__all__ = ["MEMORY_TOOLS", "mempalace_status", "mempalace_query", "mempalace_mine", "mempalace_wake", "mempalace_wake_up"]
