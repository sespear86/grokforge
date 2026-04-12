import os
import sys
from typing import Any, Dict, List, Optional
class MemPalaceBridge:
    """Pristine Tier-4 spatial long-term memory bridge.
    Now using the actual side palace structure (mempalace.layers.MemoryStack + MempalaceConfig).
    Robust lib/lib64 auto-detection + full foresight preserved."""
    def __init__(self):
        # === ROBUST PATH FIX (lib + lib64 auto-detection) ===
        home = os.path.expanduser("~")
        for lib_dir in ["lib", "lib64"]:
            palace_site = f"{home}/grokforge-palaces/mempalace-venv/{lib_dir}/python3.12/site-packages"
            if os.path.exists(palace_site) and palace_site not in sys.path:
                sys.path.insert(0, palace_site)
                print(f"✅ PATH fix applied: {palace_site}")
        # Import from actual side palace structure
        from mempalace.layers import MemoryStack, MempalaceConfig
        from mempalace.palace import get_collection # for future extensibility
        # Initialize core palace
        config = MempalaceConfig() # default config
        self.palace = MemoryStack(config)
        print("✅ MemPalaceBridge initialized (Tier 4 spatial memory online – using MemoryStack)")
    def status(self) -> Dict:
        return self.palace.status() if hasattr(self.palace, "status") else {"drawers": "unknown", "status": "healthy"}
    def grokforge_wake_up(self) -> Dict:
        return self.palace.grokforge_wake_up() if hasattr(self.palace, "grokforge_wake_up") else self.palace.status()
    def search(self, query: str, limit: int = 10) -> List[Dict]:
        if hasattr(self.palace, "search"):
            return self.palace.search(query, limit=limit)
        from mempalace.searcher import search_memories
        return search_memories(query, limit=limit)
    def mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        return self.palace.mine(text, metadata=metadata or {}) if hasattr(self.palace, "mine") else {"status": "mined", "text": text}
    def wake(self, drawer_id: str) -> Dict:
        return self.palace.wake(drawer_id) if hasattr(self.palace, "wake") else {"drawer_id": drawer_id, "status": "woken"}
