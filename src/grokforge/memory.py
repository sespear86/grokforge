import os
import json
from datetime import datetime
import numpy as np
from typing import List, Dict, Optional

class GrokMemory:
    def __init__(self):
        self.short_term = []  # ReAct + vision trace
        self.topics_dir = "memory/topics"
        self.embeddings_file = "memory/embeddings.json"
        os.makedirs(self.topics_dir, exist_ok=True)
        self.embeddings: Dict[str, List[float]] = self._load_embeddings()

    def _load_embeddings(self) -> Dict[str, List[float]]:
        if os.path.exists(self.embeddings_file):
            with open(self.embeddings_file) as f:
                return json.load(f)
        return {}

    def _save_embeddings(self):
        with open(self.embeddings_file, "w") as f:
            json.dump(self.embeddings, f)

    def _simple_embedding(self, text: str) -> List[float]:
        # Placeholder for Grok API embeddings later; deterministic hash-based for now + numpy
        words = text.lower().split()
        vec = np.zeros(64)
        for i, w in enumerate(words[:64]):
            vec[i] = hash(w) % 100 / 100.0
        return vec.tolist()

    def add_to_trace(self, entry: str, is_vision: bool = False):
        timestamp = datetime.now().isoformat()
        prefix = "[VISION]" if is_vision else "[TRACE]"
        self.short_term.append(f"{prefix} [{timestamp}] {entry}")
        print(f"Memory trace: {entry[:80]}...")

    def save_topic(self, topic: str, content: str, vision_analysis: Optional[str] = None):
        path = f"{self.topics_dir}/{topic.replace(' ', '_')}.md"
        with open(path, "a") as f:
            f.write(f"\n### {datetime.now().isoformat()}\n{content}\n")
            if vision_analysis:
                f.write(f"\n**Vision Analysis:**\n{vision_analysis}\n")
        # Auto-embed
        key = f"{topic}:{datetime.now().isoformat()}"
        self.embeddings[key] = self._simple_embedding(content + (vision_analysis or ""))
        self._save_embeddings()
        print(f"Saved enriched topic: {topic}")

    def semantic_search(self, query: str, top_k: int = 3) -> List[str]:
        if not self.embeddings:
            return ["No memories yet."]
        q_vec = np.array(self._simple_embedding(query))
        results = []
        for key, e_vec in self.embeddings.items():
            e_vec = np.array(e_vec)
            sim = np.dot(q_vec, e_vec) / (np.linalg.norm(q_vec) * np.linalg.norm(e_vec) + 1e-8)
            results.append((sim, key))
        results.sort(reverse=True)
        return [f"→ {key} (score: {score:.3f})" for score, key in results[:top_k]]
