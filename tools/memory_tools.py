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

# === SWARM AGENT MEMORY TOOLS (appended – no breaking changes) ===
def swarm_mine_collective(text: str, metadata: dict = None) -> dict:
    """Tool: Swarm agents collectively mine knowledge into shared spatial memory."""
    from memory.swarm_memory import SwarmMemory
    swarm = SwarmMemory()  # singleton pattern can be added later
    return swarm.mine_collective(text, metadata)

def swarm_search(query: str, limit: int = 15) -> list:
    """Tool: Natural-language swarm-wide search."""
    from memory.swarm_memory import SwarmMemory
    swarm = SwarmMemory()
    return swarm.search_swarm(query, limit)

def swarm_wake_agent(agent_id: str) -> dict:
    """Tool: Wake specific agent memory drawer."""
    from memory.swarm_memory import SwarmMemory
    swarm = SwarmMemory()
    return swarm.wake_agent(agent_id)

# Register them (keeps MEMORY_TOOLS fully extensible)
MEMORY_TOOLS["swarm_mine_collective"] = swarm_mine_collective
MEMORY_TOOLS["swarm_search"] = swarm_search
MEMORY_TOOLS["swarm_wake_agent"] = swarm_wake_agent
print("✅ Swarm memory tools registered – ready for natural-language swarm agents")
