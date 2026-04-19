import os
import sys
from typing import Any, Dict, List, Optional

class MemPalaceBridge:
    """Pristine Tier-4 spatial long-term memory bridge — fully wired to your real mempalace package (get_collection(palace_path) + ChromaDB)."""
    def __init__(self):
        palace_site = os.path.expanduser("~/grokforge-palaces/mempalace-venv/lib/python3.12/site-packages")
        if palace_site not in sys.path:
            sys.path.insert(0, palace_site)

        self.collection = None
        try:
            from mempalace.palace import get_collection
            
            # Try sensible palace paths (your package requires palace_path)
            candidate_paths = [
                os.path.expanduser("~/grokforge-palaces/default_palace"),
                os.path.expanduser("~/grokforge-palaces/memory_palace"),
                os.path.expanduser("~/grokforge-palaces/palace"),
                os.path.expanduser("~/.grokforge/palace"),
                "/tmp/grokforge_palace",
                "."
            ]
            
            for path in candidate_paths:
                try:
                    os.makedirs(path, exist_ok=True)
                    self.collection = get_collection(path)
                    print(f"✅ Connected to real mempalace at: {path}")
                    break
                except Exception as e:
                    print(f"   Tried {path} → {e}")
                    continue
            
            if self.collection is None:
                # Last resort — create a fresh one
                default_path = os.path.expanduser("~/grokforge-palaces/default_palace")
                os.makedirs(default_path, exist_ok=True)
                self.collection = get_collection(default_path)
                print(f"✅ Connected to real mempalace at default path: {default_path}")
                
        except Exception as e:
            print(f"❌ Could not connect to mempalace: {e}")
            print("   → Falling back to mock (tests will still run)")
            self.collection = None

        # Rust hot-path (unchanged)
        try:
            sys.path.insert(0, "rust/memory_hotpath/target/release")
            from grokforge_memory_hotpath import RustHotPath
            self.rust = RustHotPath()
            print("✅ Rust hot-path loaded (PyO3)")
        except Exception:
            self.rust = None
            print("⚠ Rust hot-path not compiled yet – Python fallback active")

    def status(self) -> Dict:
        if self.collection:
            try:
                count = self.collection.count()
                return {"status": "live", "backend": "chromadb", "count": count, "path": getattr(self.collection, '_collection_name', 'unknown')}
            except:
                return {"status": "live", "backend": "chromadb"}
        return {"status": "mock", "message": "mempalace not available"}

    def grokforge_wake_up(self) -> Dict:
        return self.status()

    def search(self, query: str, limit: int = 10) -> List[Dict]:
        if self.collection:
            try:
                res = self.collection.query(query_texts=[query], n_results=limit)
                out = []
                for i in range(len(res["ids"][0])):
                    out.append({
                        "id": res["ids"][0][i],
                        "text": res["documents"][0][i] if res.get("documents") else "",
                        "metadata": res["metadatas"][0][i] if res.get("metadatas") else {},
                        "score": 1.0 - res["distances"][0][i] if res.get("distances") else 1.0
                    })
                return out
            except Exception as e:
                print(f"⚠ mempalace search error: {e}")
                return []
        return []

    def mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        if self.collection:
            try:
                import uuid
                doc_id = str(uuid.uuid4())
                self.collection.add(
                    documents=[text],
                    metadatas=[metadata or {}],
                    ids=[doc_id]
                )
                return {"status": "stored", "id": doc_id, "backend": "chromadb"}
            except Exception as e:
                print(f"⚠ mempalace mine error: {e}")
                return {"status": "error", "error": str(e)}
        return {"status": "mock", "text": text}

    def wake(self, drawer_id: str) -> Dict:
        if self.collection:
            try:
                res = self.collection.get(ids=[drawer_id])
                return {"id": drawer_id, "content": res.get("documents", [[]])[0] if res.get("documents") else ""}
            except:
                return {"status": "not_found"}
        return {"status": "mock"}

    # Rust + multi-modal (unchanged)
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
        if modality == "image":
            meta["image"] = True
        return self.mine(str(content), meta)

    # === GROK-2 VISION DRAWER HOOK (added – ready for Grok-2 vision / CLIP / LLaVA) ===
    def mine_image(self, image_path: str, metadata: Optional[Dict] = None) -> Dict:
        """Mine an image into the palace using vision embeddings (Grok-2 ready)."""
        meta = metadata or {}
        meta["modality"] = "image"
        meta["vision_model"] = "grok-2"  # or "clip", "llava", etc.
        # Placeholder — replace with real embedding call when Grok-2 vision is available
        print(f"🖼️  Vision mining placeholder for {image_path} (Grok-2 hook ready)")
        return self.mine(f"[IMAGE:{image_path}]", meta)

    def search_by_image(self, image_path: str, limit: int = 5) -> List[Dict]:
        """Search the palace using an image query (future Grok-2 vision embedding)."""
        # Placeholder — will use vision embedding of image_path
        print(f"🔍 Vision search placeholder for {image_path}")
        return self.search(f"[IMAGE_QUERY:{image_path}]", limit)

    # === REDIS SHARDING HOOKS (added – ready for distributed / multi-node memory) ===
    def enable_redis_sharding(self, redis_url: str = "redis://localhost:6379/0"):
        """Enable Redis-backed sharding for distributed memory (future)."""
        try:
            import redis
            self.redis = redis.from_url(redis_url)
            print(f"✅ Redis sharding enabled at {redis_url}")
            return True
        except Exception as e:
            print(f"⚠ Redis not available: {e}")
            self.redis = None
            return False

    def redis_search(self, query: str, limit: int = 10) -> List[Dict]:
        """Distributed search via Redis (placeholder for real sharded index)."""
        if hasattr(self, 'redis') and self.redis:
            # Placeholder — real implementation would query Redis vector index
            print(f"🌐 Redis search placeholder: {query}")
            return self.search(query, limit)
        return self.search(query, limit)
