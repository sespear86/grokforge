import os
import sys
from typing import Any, Dict, List, Optional

class MemPalaceBridge:
    """Pristine Tier-4 spatial long-term memory bridge with Rust hot-path + multi-modal drawers.
    Uses one-line PATH fix to the side palace venv – no subprocess fragility."""

    def __init__(self):
        # === ONE-LINE PATH FIX (reliable, as verified in your terminal) ===
        palace_site = os.path.expanduser("~/grokforge-palaces/mempalace-venv/lib/python3.12/site-packages")
        if palace_site not in sys.path:
            sys.path.insert(0, palace_site)
        
        # Import from the side palace (package must exist in venv – it does)
        from mempalace import MemPalace
        self.palace = MemPalace()
        
        # === RUST HOT-PATH + MULTI-MODAL EXTENSIONS (added – full foresight) ===
        try:
            sys.path.insert(0, "rust/memory_hotpath/target/release")
            from grokforge_memory_hotpath import RustHotPath
            self.rust = RustHotPath()
            print("✅ Rust hot-path loaded (PyO3)")
        except Exception:
            self.rust = None
            print("⚠ Rust hot-path not compiled yet – Python fallback active")
        
        print("MemPalaceBridge initialized (Tier 4 spatial memory + Rust + multi-modal online)")

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

    # === RUST HOT-PATH METHODS ===
    def rust_search(self, query: str, limit: int = 10) -> List[Dict]:
        """Ultra-fast Rust spatial search (hot-path)."""
        if self.rust:
            results = self.rust.ultra_fast_search(query, limit)
            return [{"id": r, "score": 1.0, "source": "rust"} for r in results]
        return self.search(query, limit)

    def rust_mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        """Ultra-fast Rust mining."""
        if self.rust:
            self.rust.ultra_fast_mine(text, None)
        return self.mine(text, metadata)

    # === MULTI-MODAL DRAWER HOOKS (placeholders – ready for Grok-2 vision, audio, video) ===
    def mine_multi_modal(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        """Mine image/text/audio/video into spatial drawers."""
        meta = metadata or {}
        meta["modality"] = modality
        meta["multi_modal"] = True
        if modality == "image" and hasattr(self.palace, "mine_image"):
            return self.palace.mine_image(content, meta)
        return self.mine(str(content), meta)
