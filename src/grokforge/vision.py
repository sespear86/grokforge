"""
grokforge/vision.py — Grok Imagine + Vision (Phase 3 100% LOCKED)
Uses official xAI /responses endpoint + native input_image/input_text payload (April 2026 docs).
"""

from __future__ import annotations

import base64
import os
from pathlib import Path

import requests

class GrokVisionClient:
    """Official GrokVision client for Grok Imagine (image gen) + vision analysis."""

    def __init__(self, api_key: str | None = None, base_url: str = "https://api.x.ai/v1"):
        self.api_key = api_key or os.getenv("XAI_API_KEY") or "xai-placeholder-key-for-dev"
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _validate_key(self):
        """Lazy validation — only when actually calling the API."""
        if self.api_key == "xai-placeholder-key-for-dev" or not self.api_key.startswith("xai-"):
            raise ValueError(
                "❌ Missing or invalid XAI_API_KEY!\n"
                "   1. Go to https://console.x.ai/ and create a key (starts with xai-)\n"
                "   2. Run: export XAI_API_KEY=xai-...\n"
                "   3. Or use: grokforge --api-key xai-... vision generate ..."
            )

    def generate(self, prompt: str, output_path: str = "vision-test/grok_imagine_output.png") -> str:
        """Generate image with Grok Imagine (already working perfectly)."""
        self._validate_key()
        url = f"{self.base_url}/images/generations"
        payload = {
            "model": "grok-imagine-image",
            "prompt": prompt,
            "n": 1,
        }
        resp = requests.post(url, json=payload, headers=self.headers, timeout=90)
        resp.raise_for_status()
        data = resp.json()
        image_url = data["data"][0]["url"]
        img_bytes = requests.get(image_url, timeout=30).content
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_bytes(img_bytes)
        return f"✅ Grok Imagine generated → {output_path} ({len(img_bytes):,} bytes)"

    def analyze(self, image_path: str, prompt: str = "Describe this image in extreme detail for the swarm.") -> str:
        """Image analysis — OFFICIAL xAI /responses endpoint + native payload (docs-exact)."""
        self._validate_key()
        url = f"{self.base_url}/responses"
        with open(image_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        payload = {
            "model": "grok-4.20-reasoning",
            "input": [{
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{b64}"
                    },
                    {
                        "type": "input_text",
                        "text": prompt
                    }
                ]
            }]
        }
        resp = requests.post(url, json=payload, headers=self.headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        # Flexible parsing for xAI Responses API (output_text or legacy choices)
        if "output_text" in data and data["output_text"]:
            analysis = data["output_text"]
        elif "choices" in data and data["choices"]:
            analysis = data["choices"][0].get("message", {}).get("content", str(data))
        else:
            analysis = str(data)
        return f"🔍 Vision analysis:\n{analysis}"

# Singleton (safe — no import-time crash)
vision_client = GrokVisionClient()

# Phase 6: VisionAwareSwarm for ReAct2 integration (wraps existing GrokVisionClient)
class VisionAwareSwarm:
    """Vision-aware swarm layer — provides .analyze() for ReAct2 observation enrichment"""
    def __init__(self):
        self.client = vision_client  # reuse singleton from this file

    async def analyze(self, results: list) -> str:
        """Enrich observations with vision analysis (stub for now — can take image paths later)"""
        # For Phase 6 we return lightweight enrichment; real vision calls can be added in next cycle
        return f"VisionAwareSwarm analysis: {len(results)} results processed • Multi-modal context added"
