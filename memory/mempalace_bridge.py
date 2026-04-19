import os
import sys
import importlib
import inspect
from typing import Any, Dict, List, Optional

class MemPalaceBridge:
    """Pristine Tier-4 spatial long-term memory bridge — FULLY SELF-DIAGNOSING + ADAPTIVE to any mempalace package layout."""
    def __init__(self):
        palace_site = os.path.expanduser("~/grokforge-palaces/mempalace-venv/lib/python3.12/site-packages")
        if palace_site not in sys.path:
            sys.path.insert(0, palace_site)

        self.palace = None
        try:
            mempalace_mod = importlib.import_module("mempalace")
            
            # 1. Try exact common names
            candidate_names = ["MemPalace", "MemoryStack", "Palace", "MemoryPalace", "CoreMemory", "SpatialMemory", "Memory"]
            for name in candidate_names:
                if hasattr(mempalace_mod, name):
                    self.palace = getattr(mempalace_mod, name)()
                    print(f"✅ Using exact class '{name}' from mempalace")
                    break
            
            # 2. Try common submodules (many packages hide the main class here)
            if self.palace is None:
                for sub in ["core", "memory", "palace", "stack", "base", "models"]:
                    try:
                        sub_mod = importlib.import_module(f"mempalace.{sub}")
                        for name in candidate_names + ["MemoryStack", "Palace"]:
                            if hasattr(sub_mod, name):
                                self.palace = getattr(sub_mod, name)()
                                print(f"✅ Using {name} from mempalace.{sub}")
                                break
                        if self.palace:
                            break
                    except ImportError:
                        pass
            
            # 3. Ultra-broad auto-discovery (any class with memory-like methods)
            if self.palace is None:
                for name, obj in inspect.getmembers(mempalace_mod, inspect.isclass):
                    methods = [m for m in dir(obj) if not m.startswith("_")]
                    if any(m in methods for m in ["search", "mine", "status", "wake", "query", "store"]):
                        self.palace = obj()
                        print(f"✅ Auto-discovered '{name}' with methods: {methods}")
                        break
            
            if self.palace is None:
                # 4. FULL DEBUG PRINT — this will show us exactly what is inside your mempalace package
                print("❌ No suitable class found. FULL MEMPALACE PACKAGE DEBUG:")
                print("   Top-level names:", [x for x in dir(mempalace_mod) if not x.startswith("_")])
                print("   All classes and their public methods:")
                for name, obj in inspect.getmembers(mempalace_mod, inspect.isclass):
                    methods = [m for m in dir(obj) if not m.startswith("_")]
                    print(f"     {name}: {methods}")
                # Also check submodules quickly
                for sub in ["core", "memory", "palace", "stack"]:
                    try:
                        sub_mod = importlib.import_module(f"mempalace.{sub}")
                        print(f"   Submodule mempalace.{sub} names: {[x for x in dir(sub_mod) if not x.startswith('_')]}")
                    except:
                        pass
                raise ImportError("No suitable memory/palace class found — see debug output above")
            
            print(f"MemPalaceBridge initialized using {self.palace.__class__.__name__} (Tier 4 spatial memory online)")
            
        except Exception as e:
            print(f"❌ Failed to initialize mempalace: {e}")
            print("   → Falling back to mock (tests will still run, but real memory is disabled)")
            self.palace = None

        # === RUST HOT-PATH + MULTI-MODAL (unchanged) ===
        try:
            sys.path.insert(0, "rust/memory_hotpath/target/release")
            from grokforge_memory_hotpath import RustHotPath
            self.rust = RustHotPath()
            print("✅ Rust hot-path loaded (PyO3)")
        except Exception:
            self.rust = None
            print("⚠ Rust hot-path not compiled yet – Python fallback active")

    # All the delegation methods stay exactly the same (search, mine, rust_*, mine_multi_modal, etc.)
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
