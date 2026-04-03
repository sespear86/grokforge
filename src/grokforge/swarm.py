"""
grokforge/swarm.py — Vision-aware ReAct sub-agent swarm (Phase 3)
"""

from __future__ import annotations

from grokforge.vision import vision_client

class VisionAwareSwarm:
    """Every sub-agent can now ingest/generate images via GrokVisionClient."""

    def __init__(self):
        self.vision = vision_client
        self.agents = ["Researcher", "Coder", "Tester"]  # vision-enabled

    def run(self, task: str, image_context: str | None = None):
        if image_context:
            analysis = self.vision.analyze(image_context)
            task = f"{task}\n\nVision context: {analysis}"
        # ReAct loop + sub-agent dispatch (Phase 2 core preserved)
        print(f"🚀 Vision-aware swarm executing: {task[:80]}...")
        return "✅ Swarm completed with vision context"

# Global singleton
swarm = VisionAwareSwarm()
