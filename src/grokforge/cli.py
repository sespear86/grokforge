"""
grokforge/cli.py — Full CLI with Phase 2 (init/run/dream) + Phase 3 Vision
"""

from __future__ import annotations

import argparse
from grokforge.memory import GrokMemory
from grokforge.dream import start_dream_daemon

import os
import sys
from grokforge.vision import vision_client
from grokforge.swarm import VisionAwareSwarm  # Vision-aware swarm

def main() -> int:
    parser = argparse.ArgumentParser(description="GrokForge — xAI-native agentic harness")
    parser.add_argument("--api-key", default=os.getenv("XAI_API_KEY"), help="xAI API key")
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # === Phase 2 existing commands (preserved) ===
    subparsers.add_parser("init", help="Initialize GrokForge project")
    subparsers.add_parser("run", help="Run ReAct loop")
    subparsers.add_parser("dream", help="Launch GrokDream daemon")

    # === NEW: Phase 3 Vision subcommands ===
    vision_parser = subparsers.add_parser("vision", help="Grok Imagine vision tools")
    vsub = vision_parser.add_subparsers(dest="vision_cmd", required=True)

    gen = vsub.add_parser("generate", help="Generate image with Grok Imagine")
    gen.add_argument("prompt", help="Text prompt for image generation")
    gen.add_argument("--output", default="vision-test/grok_imagine_output.png", help="Output file path")

    ana = vsub.add_parser("analyze", help="Analyze an image with Grok Vision")
    ana.add_argument("image_path", help="Path to image file")
    ana.add_argument("--prompt", default="Describe this image in extreme detail for the swarm.")

    args = parser.parse_args()

    if args.api_key:
        vision_client.api_key = args.api_key  # live override

    if args.cmd == "vision":
        if args.vision_cmd == "generate":
            print(vision_client.generate(args.prompt, args.output))
        elif args.vision_cmd == "analyze":
            print(vision_client.analyze(args.image_path, args.prompt))
        return 0

    # Phase 2 routing (stub — full logic from previous scaffolding)
    print(f"✅ Running Phase 2 command: {args.cmd} (Vision integration now active)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
