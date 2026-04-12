from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
import os
import subprocess
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
    Supports optional venv activation for perfect isolation (Python 3.12 side palace).
    """
    def __init__(self, venv_path: Optional[str] = None):
        self.venv_path = venv_path or str(Path.home() / "grokforge-palaces/mempalace-venv")
        # Import the already-perfect bridge class from the same package
        from .mempalace_bridge import MemPalaceBridge
        self.bridge = MemPalaceBridge()

    def _run_with_venv(self, func_name: str, **kwargs) -> Dict[str, Any]:
        """Call bridge method with venv activation if needed."""
        if not Path(self.venv_path).exists():
            return getattr(self.bridge, func_name)(**kwargs)

        # Activate venv for the call (bridge already uses subprocess to mempalace bin)
        activate_script = f"source {self.venv_path}/bin/activate && python -c "
        code = f'''
import sys
sys.path.insert(0, "/home/Irikash/AI_Projects/GrokForge/grokforge")
from memory.mempalace_bridge import MemPalaceBridge
bridge = MemPalaceBridge()
import json
result = bridge.{func_name}(**{kwargs})
print(json.dumps(result))
'''
        try:
            result = subprocess.run(
                ["bash", "-c", activate_script + f"'{code}'"],
                capture_output=True, text=True, check=True
            )
            return json.loads(result.stdout.strip())
        except Exception as e:
            return {"error": str(e), "command": "venv-activated bridge call"}

    def status(self) -> Dict[str, Any]:
        return self._run_with_venv("status")

    def wake_up(self, wing: Optional[str] = None) -> str:
        result = self._run_with_venv("wake_up", wing=wing)
        return result.get("raw_output", str(result))

    def search(self, query: str, wing: Optional[str] = None, limit: int = 5) -> List[Dict[str, Any]]:
        result = self._run_with_venv("search", query=query, wing=wing)
        return [{"raw": result.get("raw_output", str(result))}]

    def mine(self, source: str, mode: str = "convos") -> Dict[str, Any]:
        return self._run_with_venv("mine", path=source, mode=mode)

    def grokforge_wake_up(self) -> str:
        result = self._run_with_venv("grokforge_wake_up")
        return result.get("raw_output", str(result))
