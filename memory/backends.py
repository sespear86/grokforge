"""GrokForge memory backends – Tier 4 MemPalaceBackend (pluggable)."""
from memory.mempalace_bridge import MemPalaceBridge
from typing import Dict, List, Any

class MemPalaceBackend:
    """Direct wrapper of MemPalaceBridge – zero limitations, full foresight."""
    
    def __init__(self):
        self.bridge = MemPalaceBridge()
    
    def status(self) -> Dict:
        return self.bridge.status()
    
    def query(self, query: str, limit: int = 10) -> List[Dict]:
        """Tool-friendly query alias."""
        return self.bridge.search(query, limit=limit)
    
    def mine(self, text: str, metadata: Dict = None) -> Dict:
        return self.bridge.mine(text, metadata)
    
    def wake(self, drawer_id: str) -> Dict:
        return self.bridge.wake(drawer_id)
    
    def wake_up(self) -> Dict:
        return self.bridge.grokforge_wake_up()
