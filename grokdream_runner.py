#!/usr/bin/env python3
"""
Tier 7 — Persistent GrokDream Runner v1
Main entrypoint for continuous autonomous operation.
Run with: python grokdream_runner.py --task "your task here" --cycles 5 --continuous
Fully copy-paste ready. One-liner explanations included.
"""
import argparse
import os
import sys
import time
sys.path.insert(0, os.getcwd())

from memory.swarm_react_engine import SwarmReActEngine

def main():
    parser = argparse.ArgumentParser(description="🚀 GrokDream v4.1 Persistent Runner")
    parser.add_argument("--task", type=str, default="Design and visualize the next major GrokForge city expansion with autonomous agent swarm",
                        help="Task for the swarm to execute")
    parser.add_argument("--cycles", type=int, default=3, help="Cycles per run")
    parser.add_argument("--continuous", action="store_true", help="Run in infinite loop (24/7 mode)")
    parser.add_argument("--sleep", type=int, default=60, help="Seconds between continuous runs")
    args = parser.parse_args()

    print("🚀 GrokDream Persistent Runner v1 starting...")
    engine = SwarmReActEngine(swarm_id="grokdream-persistent")

    if args.continuous:
        print(f"🔄 Continuous 24/7 mode enabled — sleeping {args.sleep}s between runs")
        run_count = 0
        while True:
            run_count += 1
            print(f"\n=== Continuous Run #{run_count} ===")
            engine.run_multi_agent_cycle(args.task, max_cycles=args.cycles)
            print(f"✅ Run #{run_count} complete — sleeping {args.sleep} seconds...")
            time.sleep(args.sleep)
    else:
        engine.run_multi_agent_cycle(args.task, max_cycles=args.cycles)
        print("✅ Single-run GrokDream complete — runner ready for daemon mode")

if __name__ == "__main__":
    main()
