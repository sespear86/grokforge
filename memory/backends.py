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
    """Concrete MemPalace v3.1.0 backend using the existing bridge.
    Supports optional venv activation for perfect isolation.
    """
    def __init__(self, venv_path: Optional[str] = None):
        self.venv_path = venv_path or str(Path.home() / "grokforge-palaces/mempalace-venv")
        self.bridge_module = "memory.mempalace_bridge"

    def _run_bridge(self, method: str, **kwargs) -> Dict[str, Any]:
        """Internal helper that activates venv if needed and calls bridge."""
        cmd = ["python", "-m", self.bridge_module, method]
        for k, v in kwargs.items():
            if v is not None:
                cmd.extend([f"--{k.replace('_', '-')}", str(v)])

        env = os.environ.copy()
        if Path(self.venv_path).exists():
            activate = f"source {self.venv_path}/bin/activate && "
            cmd = ["bash", "-c", activate + " ".join(cmd)]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            # Bridge already returns dicts; we just pass through
            import json
            return json.loads(result.stdout) if result.stdout.strip() else {"success": True, "raw_output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"error": str(e), "stderr": e.stderr, "command": " ".join(cmd)}

    def status(self) -> Dict[str, Any]:
        return self._run_bridge("status")

    def wake_up(self, wing: Optional[str] = None) -> str:
        result = self._run_bridge("wake-up", wing=wing)
        return result.get("raw_output", str(result))

    def search(self, query: str, wing: Optional[str] = None, limit: int = 5) -> List[Dict[str, Any]]:
        result = self._run_bridge("search", query=query, wing=wing)
        # Bridge search already returns formatted text; we keep raw for now
        return [{"raw": result.get("raw_output", str(result))}]

    def mine(self, source: str, mode: str = "convos") -> Dict[str, Any]:
        return self._run_bridge("mine", source=source, mode=mode)

    def grokforge_wake_up(self) -> str:
        result = self._run_bridge("wake-up", wing="sean_grok_chats")
        return result.get("raw_output", str(result))
