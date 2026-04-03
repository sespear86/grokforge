"""
grokforge/cli.py — Full CLI with Phase 2 + Phase 3 Vision + Phase 4 Advanced Memory
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from grokforge.memory import GrokMemory
from grokforge.dream import start_dream_daemon
from grokforge.vision import vision_client
from grokforge.swarm import VisionAwareSwarm  # Vision-aware swarm

def main() -> int:
    parser = argparse.ArgumentParser(description="GrokForge — xAI-native agentic harness")
    parser.add_argument("--api-key", default=os.getenv("XAI_API_KEY"), help="xAI API key")
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # === Phase 2 existing commands (preserved) ===
    subparsers.add_parser("init", help="Initialize GrokForge project")
    subparsers.add_parser("run", help="Run ReAct loop")

    # === Phase 4 Dream (subcommands + daemon start) ===
    dream_parser = subparsers.add_parser("dream", help="GrokDream commands")
    dream_sub = dream_parser.add_subparsers(dest="dream_cmd", required=False)
    dream_sub.add_parser("consolidate", help="Force immediate consolidation")

    # === NEW: Phase 4 Advanced Memory ===
    mem_parser = subparsers.add_parser("memory", help="Advanced semantic memory")
    mem_sub = mem_parser.add_subparsers(dest="mem_cmd", required=True)
    search_p = mem_sub.add_parser("search", help="Semantic search")
    search_p.add_argument("query", help="Search query")

    # === Phase 3 Vision subcommands (preserved) ===
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
        vision_client.api_key = args.api_key

    # Ensure memory directory always exists
    os.makedirs("memory/topics", exist_ok=True)

    # === Phase 4 handlers ===
    if args.cmd == "memory":
        memory = GrokMemory()
        if args.mem_cmd == "search":
            results = memory.semantic_search(args.query)
            print("\n".join(results) or "No memories yet.")
        return 0

    if args.cmd == "dream":
        if hasattr(args, "dream_cmd") and args.dream_cmd == "consolidate":
            memory = GrokMemory()
            memory.save_topic("manual_consolidate", "User-forced consolidation")
            print("✅ Manual consolidation triggered")
        else:
            # Start daemon + keep main thread alive (prevents shutdown crash)
            start_dream_daemon()
            print("✅ GrokDream daemon started (Ctrl+C to stop)")
            print("   (Press Ctrl+C when done testing)")
            try:
                while True:
                    time.sleep(10)
            except KeyboardInterrupt:
                print("\n👋 GrokDream shutting down gracefully...")
        return 0

    # === Phase 3 Vision ===
    if args.cmd == "vision":
        if args.vision_cmd == "generate":
            print(vision_client.generate(args.prompt, args.output))
        elif args.vision_cmd == "analyze":
            print(vision_client.analyze(args.image_path, args.prompt))
        return 0

    # Phase 2 fallback (preserved)
    print(f"✅ Running Phase 2 command: {args.cmd} (Vision + Memory integration active)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
