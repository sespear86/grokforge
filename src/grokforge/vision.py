"""
grokforge/vision.py — Grok Imagine + Vision (Phase 3)
Real xAI API endpoints for image generation + analysis.
"""

from __future__ import annotations

import base64
from pathlib import Path

import requests

class GrokVisionClient:
    """Official GrokVision client for Grok Imagine (image gen) + vision analysis."""

    def __init__(self, api_key: str | None = None, base_url: str = "https://api.x.ai/v1"):
        self.api_key = api_key or "xai-placeholder-key-for-dev"  # overridden by CLI/env
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def generate(self, prompt: str, output_path: str = "vision-test/grok_imagine_output.png") -> str:
        """Generate image with Grok Imagine (real endpoint)."""
        url = f"{self.base_url}/images/generations"
        payload = {
            "model": "grok-imagine-image",
            "prompt": prompt,
            "n": 1,
            "response_format": "b64_json",
        }
        resp = requests.post(url, json=payload, headers=self.headers, timeout=90)
        resp.raise_for_status()
        data = resp.json()
        img_bytes = base64.b64decode(data["data"][0]["b64_json"])
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_bytes(img_bytes)
        return f"✅ Grok Imagine generated → {output_path} ({len(img_bytes):,} bytes)"

    def analyze(self, image_path: str, prompt: str = "Describe this image in extreme detail for the swarm.") -> str:
        """Image analysis via chat/completions (vision-enabled model)."""
        url = f"{self.base_url}/chat/completions"
        with open(image_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        payload = {
            "model": "grok-2-vision-latest",
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}}
                ]
            }]
        }
        resp = requests.post(url, json=payload, headers=self.headers, timeout=30)
        resp.raise_for_status()
        analysis = resp.json()["choices"][0]["message"]["content"]
        return f"🔍 Vision analysis:\n{analysis}"

# Singleton for swarm integration
vision_client = GrokVisionClient()
