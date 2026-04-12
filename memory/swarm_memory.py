import uuid
from typing import Any, Dict, List, Optional
from .mempalace_bridge import MemPalaceBridge

class SwarmMemory:
    """Natural-language swarm agent memory layer – Tier 4 full integration.
    One shared MemoryStack + per-agent logical drawers. Fully extensible to Rust, multi-modal, etc."""
    def __init__(self, swarm_id: str = None):
        self.bridge = MemPalaceBridge()
        self.swarm_id = swarm_id or f"swarm-{uuid.uuid4().hex[:8]}"
        self.agent_drawers: Dict[str, str] = {}  # agent_id -> drawer_id
        print(f"✅ SwarmMemory online – swarm_id={self.swarm_id}")

    def register_agent(self, agent_id: str) -> str:
        """Give each swarm agent its own logical drawer."""
        drawer_id = f"{self.swarm_id}-agent-{agent_id}"
        self.agent_drawers[agent_id] = drawer_id
        return drawer_id

    def mine_collective(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        """All agents contribute to shared knowledge."""
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine(text, meta)

    def mine_agent(self, agent_id: str, text: str, metadata: Optional[Dict] = None) -> Dict:
        """Agent-specific knowledge (still searchable by whole swarm)."""
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine(text, meta)

    def search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        """Natural-language search across entire swarm memory."""
        return self.bridge.search(query, limit=limit)

    def wake_agent(self, agent_id: str) -> Dict:
        """Wake an individual agent’s drawer."""
        drawer = self.agent_drawers.get(agent_id)
        if not drawer:
            drawer = self.register_agent(agent_id)
        return self.bridge.wake(drawer)

    def grokforge_wake_up(self) -> Dict:
        """Full swarm wake-up for GrokForge."""
        return self.bridge.grokforge_wake_up()

    def status(self) -> Dict:
        """Swarm + palace health."""
        return {
            "swarm_id": self.swarm_id,
            "agents": len(self.agent_drawers),
            "palace": self.bridge.status()
        }
