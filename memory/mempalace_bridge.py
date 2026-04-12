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

    # === RUST HOT-PATH + MULTI-MODAL EXTENSIONS (added – full foresight) ===
    def __init__(self):
        # ... (existing init code stays exactly as-is) ...
        # Try to load Rust hot-path (graceful fallback)
        try:
            import sys
            sys.path.insert(0, "rust/memory_hotpath/target/release")
            from grokforge_memory_hotpath import RustHotPath
            self.rust = RustHotPath()
            print("✅ Rust hot-path loaded (PyO3)")
        except Exception:
            self.rust = None
            print("⚠️ Rust hot-path not compiled yet – Python fallback active")

    def rust_search(self, query: str, limit: int = 10) -> List[Dict]:
        """Ultra-fast Rust spatial search (hot-path)."""
        if self.rust:
            results = self.rust.ultra_fast_search(query, limit)
            return [{"id": r, "score": 1.0, "source": "rust"} for r in results]
        return self.search(query, limit)  # fallback

    def rust_mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        """Ultra-fast Rust mining."""
        if self.rust:
            self.rust.ultra_fast_mine(text, None)
        return self.mine(text, metadata)

    # Multi-modal drawer hooks (placeholders – ready for Grok-2 vision, audio, etc.)
    def mine_multi_modal(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        """Mine image/text/audio/video into spatial drawers."""
        meta = metadata or {}
        meta["modality"] = modality
        meta["multi_modal"] = True
        if modality == "image" and hasattr(self.palace, "mine_image"):
            return self.palace.mine_image(content, meta)
        return self.mine(str(content), meta)  # fallback
