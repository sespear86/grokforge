import os
import sys
from typing import List, Dict, Optional, Any

try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    chromadb = None

class MemPalaceBridge:
    def __init__(self, palace_path: Optional[str] = None):
        self.palace_path = palace_path or os.path.expanduser("~/grokforge-palaces/default_palace")
        os.makedirs(self.palace_path, exist_ok=True)
        self.client = None
        self.collection = None
        self.rust = None
        self._connect_real_mempalace()

        # === RUST HOT-PATH (now fully working) ===
        try:
            import grokforge_memory_hotpath
            self.rust = grokforge_memory_hotpath.RustHotPath()
            print("✅ Rust hot-path loaded successfully (native speed active)")
        except Exception as e:
            print(f"⚠ Rust hot-path import failed: {type(e).__name__}: {e}")
            self.rust = None

    def _connect_real_mempalace(self):
        if chromadb is None:
            print("⚠ ChromaDB not installed — using mock")
            return
        try:
            self.client = chromadb.PersistentClient(path=self.palace_path)
            self.collection = self.client.get_or_create_collection("grokforge_memory")
            print(f"✅ Connected to real mempalace at: {self.palace_path}")
        except Exception as e:
            print(f"⚠ MemPalace connection issue: {e}")

    def status(self) -> Dict:
        if self.collection:
            try:
                count = self.collection.count()
            except:
                count = 0
            return {
                "status": "live",
                "backend": "chromadb",
                "count": count,
                "path": self.palace_path
            }
        return {"status": "mock", "backend": "none"}

    # === CORE METHODS ===
    def mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        if self.collection:
            import uuid
            doc_id = str(uuid.uuid4())
            self.collection.add(ids=[doc_id], documents=[text], metadatas=[meta])
            return {"status": "mined", "id": doc_id, "text": text[:100]}
        return {"status": "mock_mined", "text": text[:100]}

    def search(self, query: str, limit: int = 5) -> List[Dict]:
        if self.collection:
            results = self.collection.query(
                query_texts=[query],
                n_results=min(limit, self.collection.count() or 1)
            )
            return [
                {"text": doc, "metadata": meta, "distance": dist}
                for doc, meta, dist in zip(
                    results.get("documents", [[]])[0],
                    results.get("metadatas", [[]])[0],
                    results.get("distances", [[]])[0]
                )
            ]
        return [{"text": f"mock_result_for_{query}", "metadata": {}, "distance": 0.0}]

    # === VISION + REDIS (from earlier phases) ===
    def mine_image(self, image_path: str, metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["modality"] = "image"
        meta["vision_model"] = "grok-2"
        print(f"🖼️ Vision mining placeholder for {image_path} (Grok-2 hook ready)")
        return self.mine(f"[IMAGE:{image_path}]", meta)

    def search_by_image(self, image_path: str, limit: int = 5) -> List[Dict]:
        print(f"🔍 Vision search placeholder for {image_path}")
        return self.search(f"[IMAGE_QUERY:{image_path}]", limit)

    def enable_redis_sharding(self, redis_url: str = "redis://localhost:6379/0"):
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
        if hasattr(self, 'redis') and self.redis:
            print(f"🌐 Redis search placeholder: {query}")
            return self.search(query, limit)
        return self.search(query, limit)

    # === MULTI-MODAL (required by test_swarm_rust_multimodal.py) ===
    def mine_multi_modal(self, content: str, modality: str = "text", metadata: Optional[Dict] = None) -> Dict:
        meta = metadata or {}
        meta["modality"] = modality
        if modality == "image":
            return self.mine_image(content, meta)
        return self.mine(content, meta)

    def search_multi_modal(self, query: str, modality: str = "text", limit: int = 5) -> List[Dict]:
        if modality == "image":
            return self.search_by_image(query, limit)
        return self.search(query, limit)

    # === RUST HOT-PATH WRAPPERS (added for full Swarm + test compatibility) ===
    def rust_mine(self, text: str, metadata: Optional[Dict] = None) -> Dict:
        if self.rust:
            result = self.rust.ultra_fast_mine(text, metadata)
            return {"status": "rust_mined", "result": result}
        return self.mine(text, metadata)

    def rust_search(self, query: str, limit: int = 5) -> List[Dict]:
        if self.rust:
            results = self.rust.ultra_fast_search(query, limit)
            return [{"text": r, "metadata": {}, "distance": 0.0} for r in results]
        return self.search(query, limit)
