import os
import sys
from typing import Any, Dict, List, Optional
import inspect

class MemPalaceBridge:
    """Pristine Tier-4 spatial long-term memory bridge.
    Now fully adaptive to the real side-palace MemoryStack API.
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

    def _call_method(self, method_name: str, *args, **kwargs) -> Any:
        """Adaptive caller – tries full kwargs, then falls back gracefully."""
        if not hasattr(self.palace, method_name):
            return {"status": "method_not_found", "method": method_name}
        method = getattr(self.palace, method_name)
        try:
            # First try with full kwargs
            return method(*args, **kwargs)
        except TypeError as e:
            # If limit or other kwarg is rejected, strip unknown kwargs
            if "unexpected keyword argument" in str(e):
                sig = inspect.signature(method)
                valid_kwargs = {k: v for k, v in kwargs.items() if k in sig.parameters}
                return method(*args, **valid_kwargs)
            raise

    def status(self) -> Dict:
        """Full palace health/status."""
        return self._call_method("status")

    def grokforge_wake_up(self) -> Dict:
        """Full GrokForge wake-up sequence."""
        return self._call_method("grokforge_wake_up")

    def search(self, query: str, limit: int = 10) -> List[Dict]:
        """Natural-language spatial memory search – adaptive to real API."""
        return self._call_method("search", query, limit=limit)

    def mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        """Store new knowledge + metadata."""
        return self._call_method("mine", text, metadata=metadata or {})

    def wake(self, drawer_id: str) -> Dict:
        """Retrieve exact drawer by ID."""
        return self._call_method("wake", drawer_id)
