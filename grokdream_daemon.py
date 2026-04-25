#!/usr/bin/env python3
"""
Tier 8 — Persistent GrokDream Daemon v5 (FIXED)
Supports single-run testing (--task + --cycles) AND continuous Redis-queue mode.
Fully copy-paste ready. One-liner explanations included.
"""
import argparse
import os
import sys
import time
import signal
import redis
sys.path.insert(0, os.getcwd())

from memory.swarm_react_engine import SwarmReActEngine

class GrokDreamDaemon:
    def __init__(self):
        self.engine = SwarmReActEngine(swarm_id="grokdream-daemon-v5")
        self.redis = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)
        self.running = True
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        print("✅ GrokDream Daemon v5 initialized — Redis task queue + self-improvement active")

    def shutdown(self, *args):
        print("\n🛑 Graceful shutdown requested...")
        self.running = False

    def process_task_queue(self, provided_task: str = None):
        """Pull from Redis queue or use provided task (for single-run testing)."""
        if provided_task:
            return provided_task
        task = self.redis.lpop("grokdream:tasks")
        if task:
            print(f"📥 Pulled task from Redis queue: {task}")
            return task
        return "Continue autonomous GrokForge city expansion with vision drawer and agent swarm"

    def run_self_improvement(self):
        """Critic-driven self-improvement loop."""
        improvement = self.engine.bridge.rust_mine(
            "SELF-IMPROVEMENT: Review last GrokDream cycle and propose one refined task for next run",
            {"agent": "critic", "type": "self_improve", "swarm": "grokdream-daemon-v5"}
        )
        print(f"✅ Self-improvement mined: {improvement['status']}")

    def run(self, task: str = None, cycles: int = 2, continuous: bool = False, sleep: int = 30):
        print("🚀 GrokDream Daemon v5 starting...")
        run_count = 0
        while self.running:
            run_count += 1
            current_task = self.process_task_queue(task if not continuous else None)
            print(f"\n=== Daemon Run #{run_count} | Task: {current_task[:80]}... ===")
            
            self.engine.run_multi_agent_cycle(current_task, max_cycles=cycles)
            self.run_self_improvement()
            
            print(f"✅ Daemon run #{run_count} complete — palace growing")
            if not continuous:
                break
            print(f"⏳ Sleeping {sleep}s before next cycle...")
            time.sleep(sleep)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🚀 GrokDream Daemon v5")
    parser.add_argument("--task", type=str, default=None, help="Task for single-run mode")
    parser.add_argument("--cycles", type=int, default=2, help="Cycles per run (single-run mode)")
    parser.add_argument("--continuous", action="store_true", help="Run forever with Redis queue")
    parser.add_argument("--sleep", type=int, default=30, help="Sleep seconds between continuous runs")
    args = parser.parse_args()
    
    daemon = GrokDreamDaemon()
    daemon.run(task=args.task, cycles=args.cycles, continuous=args.continuous, sleep=args.sleep)
