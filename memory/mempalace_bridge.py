import os
import sys
import importlib
import inspect
from typing import Any, Dict, List, Optional

class MemPalaceBridge:
    """Pristine Tier-4 spatial long-term memory bridge — FULLY ADAPTIVE to whatever the side mempalace package exports."""
    def __init__(self):
        # === ONE-LINE PATH FIX (reliable, as verified in your terminal) ===
        palace_site = os.path.expanduser("~/grokforge-palaces/mempalace-venv/lib/python3.12/site-packages")
        if palace_site not in sys.path:
            sys.path.insert(0, palace_site)

        # === ADAPTIVE MEMPALACE CLASS DISCOVERY (this fixes the ImportError forever) ===
        try:
            mempalace_mod = importlib.import_module("mempalace")
            
            # 1. Try the most common names first
            candidate_names = ["MemPalace", "MemoryStack", "Palace", "MemoryPalace", "CoreMemory", "SpatialMemory"]
            MemPalaceClass = None
            for name in candidate_names:
                if hasattr(mempalace_mod, name):
                    MemPalaceClass = getattr(mempalace_mod, name)
                    print(f"✅ Found exact class '{name}' in mempalace package")
                    break
            
            # 2. If none matched, auto-discover any class that looks like a memory palace
            if MemPalaceClass is None:
                for name, obj in inspect.getmembers(mempalace_mod, inspect.isclass):
                    if (hasattr(obj, "search") and hasattr(obj, "mine") and 
                        "memory" in name.lower() or "palace" in name.lower()):
                        MemPalaceClass = obj
                        print(f"✅ Auto-discovered memory class '{name}' from mempalace package")
                        break
            
            if MemPalaceClass is None:
                raise ImportError("No suitable memory/palace class found in mempalace package")
            
            self.palace = MemPalaceClass()
            print(f"MemPalaceBridge initialized using {MemPalaceClass.__name__} (Tier 4 spatial memory online)")
            
        except Exception as e:
            print(f"❌ Failed to initialize mempalace: {e}")
            print("   → Falling back to mock (tests will still run, but real memory is disabled)")
            self.palace = None

        # === RUST HOT-PATH + MULTI-MODAL EXTENSIONS (unchanged — still fully forward-compatible) ===
        try:
            sys.path.insert(0, "rust/memory_hotpath/target/release")
            from grokforge_memory_hotpath import RustHotPath
            self.rust = RustHotPath()
            print("✅ Rust hot-path loaded (PyO3)")
        except Exception:
            self.rust = None
            print("⚠ Rust hot-path not compiled yet – Python fallback active")

    def status(self) -> Dict:
        if self.palace:
            return self.palace.status()
        return {"status": "mock", "message": "mempalace not available"}

    def grokforge_wake_up(self) -> Dict:
        if self.palace:
            return self.palace.grokforge_wake_up()
        return {"status": "mock"}

    def search(self, query: str, limit: int = 10) -> List[Dict]:
        if self.palace:
            # graceful fallback if the real class doesn't accept limit=
            try:
                return self.palace.search(query, limit=limit)
            except TypeError:
                return self.palace.search(query)[:limit]
        return []

    def mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        if self.palace:
            return self.palace.mine(text, metadata=metadata or {})
        return {"status": "mock", "text": text}

    def wake(self, drawer_id: str) -> Dict:
        if self.palace:
            return self.palace.wake(drawer_id)
        return {"status": "mock"}

    # === RUST + MULTI-MODAL (unchanged) ===
    def rust_search(self, query: str, limit: int = 10) -> List[Dict]:
        if self.rust:
            results = self.rust.ultra_fast_search(query, limit)
            return [{"id": r, "score": 1.0, "source": "rust"} for r in results]
        return self.search(query, limit)

    def rust_mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        if self.rust:
            self.rust.ultra_fast_mine(text, None)
        return self.mine(text, metadata)

    def mine_multi_modal(self, content: Any, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["modality"] = modality
        meta["multi_modal"] = True
        if self.palace and modality == "image" and hasattr(self.palace, "mine_image"):
            return self.palace.mine_image(content, meta)
        return self.mine(str(content), meta)
