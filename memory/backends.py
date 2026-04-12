from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
import os
from pathlib import Path

class MemoryBackend(ABC):
    """Abstract base class for all memory backends in GrokForge.
    Pluggable design per PROJECT-BIBLE.md – supports Python, future Rust hot-paths,
    multi-modal drawers, distributed backends, natural-language swarm agents,
    and maximal openness. No scope limits baked in.
    """
    @abstractmethod
    def status(self) -> Dict[str, Any]:
        """Return current memory system status."""
        ...

    @abstractmethod
    def wake_up(self, wing: Optional[str] = None) -> str:
        """Return minimal wake-up context (compressed essential story)."""
        ...

    @abstractmethod
    def search(self, query: str, wing: Optional[str] = None, limit: int = 5) -> List[Dict[str, Any]]:
        """Semantic search across wings/rooms."""
        ...

    @abstractmethod
    def mine(self, source: str, mode: str = "convos") -> Dict[str, Any]:
        """Mine new content into the palace."""
        ...

    @abstractmethod
    def grokforge_wake_up(self) -> str:
        """Project-specific wake-up text for GrokForge continuity."""
        ...


class MemPalaceBackend(MemoryBackend):
    """Concrete MemPalace v3.1.0 backend – directly wraps the excellent MemPalaceBridge class.
    One-line PATH fix ensures the correct venv mempalace CLI is always used.
    """
    def __init__(self, venv_path: Optional[str] = None):
        self.venv_path = venv_path or str(Path.home() / "grokforge-palaces/mempalace-venv")
        from .mempalace_bridge import MemPalaceBridge
        self.bridge = MemPalaceBridge()

        # Ensure venv bin is first in PATH so 'mempalace' CLI resolves correctly
        if Path(self.venv_path).exists():
            venv_bin = str(Path(self.venv_path) / "bin")
            current_path = os.environ.get("PATH", "")
            if venv_bin not in current_path:
                os.environ["PATH"] = f"{venv_bin}:{current_path}"

    def status(self) -> Dict[str, Any]:
        return self.bridge.status()

    def wake_up(self, wing: Optional[str] = None) -> str:
        result = self.bridge.wake_up(wing=wing)
        return result.get("raw_output", str(result))

    def search(self, query: str, wing: Optional[str] = None, limit: int = 5) -> List[Dict[str, Any]]:
        result = self.bridge.search(query=query, wing=wing)
        return [{"raw": result.get("raw_output", str(result))}]

    def mine(self, source: str, mode: str = "convos") -> Dict[str, Any]:
        return self.bridge.mine(path=source, mode=mode)

    def grokforge_wake_up(self) -> str:
        result = self.bridge.grokforge_wake_up()
        return result.get("raw_output", str(result))
