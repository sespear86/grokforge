#!/usr/bin/env python3
"""
MemPalace Bridge for GrokForge
==============================
Pluggable Python interface to the side MemPalace v3.1.0 instance.
Designed as the first step toward abstract MemoryBackend (Tier 4 spatial long-term).
Fully compatible with PROJECT-BIBLE.md modular design and future Rust port.

This file was generated while the side palace was actively assisting (it just mined
this entire conversation for us).

Usage:
    from memory.mempalace_bridge import MemPalaceBridge
    bridge = MemPalaceBridge()
    print(bridge.wake_up(wing="sean_grok_chats"))   # use correct wing
    results = bridge.search("Phase 10 memory architecture")
"""

import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Any

class MemPalaceBridge:
    """
    Bridge to side MemPalace. Future versions will inherit from abstract MemoryBackend.
    """

    def __init__(self, palace_path: Optional[str] = None):
        self.palace_path = palace_path
        self._mempalace_bin = "mempalace"  # must be in PATH (activate mempalace-venv)

    def _run(self, args: List[str]) -> Dict[str, Any]:
        """Internal runner — handles plain-text output from v3.1.0 CLI."""
        cmd = [self._mempalace_bin] + args
        if self.palace_path:
            cmd.extend(["--palace", self.palace_path])

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=60
            )
            output = result.stdout.strip()
            # CLI returns plain text (not JSON), so we always return raw output
            return {
                "success": True,
                "raw_output": output,
                "command": " ".join(cmd)
            }
        except subprocess.CalledProcessError as e:
            return {
                "error": str(e),
                "stderr": e.stderr.strip() if e.stderr else "",
                "command": " ".join(cmd)
            }
        except FileNotFoundError:
            return {
                "error": f"{self._mempalace_bin} not found in PATH. Activate the mempalace-venv first."
            }

    def mine(self, path: str, mode: str = "convos") -> Dict[str, Any]:
        """Mine files/conversations into the palace."""
        args = ["mine", str(path)]
        if mode:
            args.extend(["--mode", mode])
        return self._run(args)

    def search(self, query: str, wing: Optional[str] = None) -> Dict[str, Any]:
        """Search the palace (replaces old query)."""
        args = ["search", query]
        if wing:
            args.extend(["--wing", wing])
        return self._run(args)

    def wake_up(self, wing: Optional[str] = None) -> Dict[str, Any]:
        """Get L0 + L1 wake-up context for continuity."""
        args = ["wake-up"]
        if wing:
            args.extend(["--wing", wing])
        return self._run(args)

    def status(self) -> Dict[str, Any]:
        """Show palace status."""
        return self._run(["status"])

    def compress(self) -> Dict[str, Any]:
        """Compress drawers."""
        return self._run(["compress"])

    # Convenience method for GrokForge continuity
    def grokforge_wake_up(self) -> Dict[str, Any]:
        """Wake-up optimized for our project (tries common wings)."""
        for wing in ["sean_grok_chats", "Project-Build-Sessions", "GrokForge"]:
            result = self.wake_up(wing=wing)
            if "success" in result and result.get("raw_output"):
                return result
        return self.wake_up()


# Simple CLI entry point (for direct use from terminal)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="GrokForge MemPalace Bridge")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # mine
    p = subparsers.add_parser("mine", help="Mine path")
    p.add_argument("path")
    p.add_argument("--mode", default="convos", choices=["convos", "project"])

    # search
    p = subparsers.add_parser("search", help="Search palace")
    p.add_argument("query")
    p.add_argument("--wing", default=None)

    # wake-up
    p = subparsers.add_parser("wake-up", help="Wake-up continuity")
    p.add_argument("--wing", default=None)

    args = parser.parse_args()
    bridge = MemPalaceBridge()

    if args.command == "mine":
        print(bridge.mine(args.path, getattr(args, "mode", "convos")))
    elif args.command == "search":
        print(bridge.search(args.query, getattr(args, "wing", None)))
    elif args.command == "wake-up":
        print(bridge.wake_up(getattr(args, "wing", None)))
    else:
        print(bridge.grokforge_wake_up())

    status_parser = subparsers.add_parser("status", help="Show palace status")
    status_parser.set_defaults(func=lambda args: print("Status via bridge"))


    # Add status subparser (was missing from previous patch)
    status_parser = subparsers.add_parser("status", help="Show palace status")
    status_parser.set_defaults(func=lambda args: print(bridge.status()))
