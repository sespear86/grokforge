import uuid
from typing import Any, Dict, List, Optional
from .mempalace_bridge import MemPalaceBridge

class SwarmMemory:
    """Natural-language swarm agent memory layer – Tier 4 full integration.
    One shared MemoryStack + per-agent logical drawers. Fully extensible to Rust, multi-modal, etc."""
    def __init__(self, swarm_id: str = None):
        self.bridge = MemPalaceBridge()
        self.swarm_id = swarm_id or f"swarm-{uuid.uuid4().hex[:8]}"
        self.agent_drawers: Dict[str, str] = {}
        print(f"✅ SwarmMemory online – swarm_id={self.swarm_id}")

    def register_agent(self, agent_id: str) -> str:
        drawer_id = f"{self.swarm_id}-agent-{agent_id}"
        self.agent_drawers[agent_id] = drawer_id
        return drawer_id

    def mine_collective(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine(text, meta)

    def mine_agent(self, agent_id: str, text: str, metadata: Optional[Dict] = None) -> Dict:
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine(text, meta)

    def search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        return self.bridge.search(query, limit=limit)

    def wake_agent(self, agent_id: str) -> Dict:
        drawer = self.agent_drawers.get(agent_id)
        if not drawer:
            drawer = self.register_agent(agent_id)
        return self.bridge.wake(drawer)

    def grokforge_wake_up(self) -> Dict:
        return self.bridge.grokforge_wake_up()

    def status(self) -> Dict:
        return {
            "swarm_id": self.swarm_id,
            "agents": len(self.agent_drawers),
            "palace": self.bridge.status()
        }

    # === RUST + MULTI-MODAL EXTENSIONS (added) ===
    def rust_search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        """Swarm-wide ultra-fast Rust search."""
        return self.bridge.rust_search(query, limit)

    def mine_multi_modal_collective(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        """Collective multi-modal mining."""
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine_multi_modal(content, modality, meta)

    def mine_multi_modal_agent(self, agent_id: str, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        """Agent-specific multi-modal mining."""
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine_multi_modal(content, modality, meta)

    # === RUST + MULTI-MODAL EXTENSIONS (re-confirmed clean) ===
    def rust_search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        """Swarm-wide ultra-fast Rust search."""
        return self.bridge.rust_search(query, limit)

    def mine_multi_modal_collective(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        """Collective multi-modal mining."""
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine_multi_modal(content, modality, meta)

    def mine_multi_modal_agent(self, agent_id: str, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        """Agent-specific multi-modal mining."""
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine_multi_modal(content, modality, meta)

# === RUST + MULTI-MODAL EXTENSIONS (re-confirmed clean) ===
    def rust_search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        """Swarm-wide ultra-fast Rust search."""
        return self.bridge.rust_search(query, limit)

    def mine_multi_modal_collective(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        """Collective multi-modal mining."""
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine_multi_modal(content, modality, meta)

    def mine_multi_modal_agent(self, agent_id: str, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        """Agent-specific multi-modal mining."""
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine_multi_modal(content, modality, meta)

# === RUST + MULTI-MODAL EXTENSIONS (re-confirmed) ===
    def rust_search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        return self.bridge.rust_search(query, limit)

    def mine_multi_modal_collective(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine_multi_modal(content, modality, meta)

    def mine_multi_modal_agent(self, agent_id: str, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine_multi_modal(content, modality, meta)

# === RUST + MULTI-MODAL EXTENSIONS (re-confirmed) ===
    def rust_search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        return self.bridge.rust_search(query, limit)

    def mine_multi_modal_collective(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine_multi_modal(content, modality, meta)

    def mine_multi_modal_agent(self, agent_id: str, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine_multi_modal(content, modality, meta)

# === RUST + MULTI-MODAL EXTENSIONS (re-confirmed) ===
    def rust_search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        return self.bridge.rust_search(query, limit)

    def mine_multi_modal_collective(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine_multi_modal(content, modality, meta)

    def mine_multi_modal_agent(self, agent_id: str, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine_multi_modal(content, modality, meta)

# === RUST + MULTI-MODAL EXTENSIONS (re-confirmed) ===
    def rust_search_swarm(self, query: str, limit: int = 20) -> List[Dict]:
        return self.bridge.rust_search(query, limit)

    def mine_multi_modal_collective(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine_multi_modal(content, modality, meta)

    def mine_multi_modal_agent(self, agent_id: str, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        drawer = self.agent_drawers.get(agent_id) or self.register_agent(agent_id)
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["agent_id"] = agent_id
        meta["drawer"] = drawer
        return self.bridge.mine_multi_modal(content, modality, meta)

    # === VISION + REDIS EXTENSIONS (added) ===
    def mine_image_collective(self, image_path: str, metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["swarm_id"] = self.swarm_id
        meta["source"] = "collective"
        return self.bridge.mine_image(image_path, meta)

    def search_by_image_swarm(self, image_path: str, limit: int = 5) -> List[Dict]:
        return self.bridge.search_by_image(image_path, limit)

    def enable_redis(self, redis_url: str = "redis://localhost:6379/0"):
        return self.bridge.enable_redis_sharding(redis_url)
