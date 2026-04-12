import os
import sys
from typing import Any, Dict, List, Optional

class MemPalaceBridge:
    """Pristine Tier-4 spatial long-term memory bridge.
    Uses one-line PATH fix to the side palace venv – no subprocess fragility."""
    
    def __init__(self):
        # === ONE-LINE PATH FIX (reliable, as verified in your terminal) ===
        palace_site = os.path.expanduser("~/grokforge-palaces/mempalace-venv/lib/python3.12/site-packages")
        if palace_site not in sys.path:
            sys.path.insert(0, palace_site)
        
        # Import from the side palace (package must exist in venv – it does)
        from mempalace import MemPalace
        self.palace = MemPalace()
        print("✅ MemPalaceBridge initialized (Tier 4 spatial memory online)")
    
    def status(self) -> Dict:
        return self.palace.status()
    
    def grokforge_wake_up(self) -> Dict:
        return self.palace.grokforge_wake_up()
    
    def search(self, query: str, limit: int = 10) -> List[Dict]:
        return self.palace.search(query, limit=limit)
    
    def mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        return self.palace.mine(text, metadata=metadata or {})
    
    def wake(self, drawer_id: str) -> Dict:
        return self.palace.wake(drawer_id)
