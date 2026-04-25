#!/usr/bin/env python3
"""
Tier 9 — GrokDream Daemon v5.2 (Redis health + self-healing enhanced)
"""
import argparse
import os
import sys
import time
import signal
import redis
import json
sys.path.insert(0, os.getcwd())
from memory.swarm_react_engine import SwarmReActEngine

class GrokDreamDaemon:
    def __init__(self):
        self.engine = SwarmReActEngine(swarm_id="grokdream-daemon-v5.2")
        self.redis = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True, socket_connect_timeout=2)
        self.running = True
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        
        # Redis health check
        try:
            self.redis.ping()
            print("✅ GrokDream Daemon v5.2 initialized — Redis LIVE + Self-Healing + Vision ready")
        except:
            print("⚠️  Redis not connected (daemon still runs via --task mode)")

    def shutdown(self, *args):
        print("\n🛑 Graceful shutdown requested...")
        self.running = False

    def process_task_queue(self, provided_task: str = None):
        if provided_task:
            return {"task": provided_task, "requires_vision": False}
        try:
            task_json = self.redis.lpop("grokdream:tasks")
            if task_json:
                task = json.loads(task_json)
                print(f"📥 Pulled external task from Redis: {task['task'][:80]}...")
                return task
        except:
            pass
        return {"task": "Continue autonomous GrokForge city expansion with vision drawer and agent swarm", "requires_vision": False}

    def run_self_improvement(self):
        improvement = self.engine.bridge.rust_mine(
            "SELF-IMPROVEMENT: Review last GrokDream cycle and propose one refined task for next run",
            {"agent": "critic", "type": "self_improve", "swarm": "grokdream-daemon-v5.2"}
        )
        print(f"✅ Self-improvement mined: {improvement['status']}")

    def run(self, task: str = None, cycles: int = 2, continuous: bool = False, sleep: int = 30):
        print("🚀 GrokDream Daemon v5.2 starting (self-healing active)...")
        run_count = 0
        while self.running:
            run_count += 1
            try:
                current_task = self.process_task_queue(task if not continuous else None)
                print(f"\n=== Daemon Run #{run_count} | Task: {current_task['task'][:80]}... ===")
                
                if current_task.get("requires_vision"):
                    print("🖼️  Grok-2 Vision integration triggered — vision drawer engaged")
                
                self.engine.run_multi_agent_cycle(current_task["task"], max_cycles=cycles)
                self.run_self_improvement()
                
                print(f"✅ Daemon run #{run_count} complete — palace growing")
            except Exception as e:
                print(f"⚠️  Self-healing triggered — error in cycle: {e}")
                time.sleep(5)
            
            if not continuous:
                break
            print(f"⏳ Sleeping {sleep}s before next cycle...")
            time.sleep(sleep)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🚀 GrokDream Daemon v5.2")
    parser.add_argument("--task", type=str, default=None, help="Task for single-run mode")
    parser.add_argument("--cycles", type=int, default=2, help="Cycles per run")
    parser.add_argument("--continuous", action="store_true", help="Run forever with Redis queue")
    parser.add_argument("--sleep", type=int, default=30, help="Sleep seconds between runs")
    args = parser.parse_args()
   
    daemon = GrokDreamDaemon()
    daemon.run(task=args.task, cycles=args.cycles, continuous=args.continuous, sleep=args.sleep)
