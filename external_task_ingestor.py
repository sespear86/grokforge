#!/usr/bin/env python3
"""
Tier 9 — External Task Ingestor (FULLY RESILIENT)
Now calls the new bootstrap automatically.
"""
import argparse
import json
import time
import redis
import sys
import subprocess

def ensure_redis_running():
    try:
        r = redis.Redis(host='localhost', port=6379, db=1, socket_connect_timeout=1)
        r.ping()
        return True
    except:
        print("⚡ Redis not responding — running full bootstrap...")
        try:
            subprocess.run(["./bootstrap_redis.sh"], check=True)
            time.sleep(2)
            return True
        except:
            print("❌ Bootstrap failed. Please run: ./bootstrap_redis.sh")
            return False

def main():
    parser = argparse.ArgumentParser(description="🚀 External Task Ingestor for GrokDream Daemon")
    parser.add_argument("--task", type=str, required=True, help="Task description to inject")
    parser.add_argument("--source", type=str, default="external-cli", help="Source label")
    parser.add_argument("--vision", action="store_true", help="Flag for Grok-2 Vision")
    args = parser.parse_args()

    if not ensure_redis_running():
        print("⚠️  Falling back to console-only (daemon can still use --task)")
        print(f"   Task was: {args.task}")
        return

    r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)
    
    task_payload = {
        "task": args.task,
        "source": args.source,
        "timestamp": time.time(),
        "requires_vision": args.vision
    }
    
    r.rpush("grokdream:tasks", json.dumps(task_payload))
    print(f"✅ Task ingested to Redis queue: {args.task[:80]}...")
    print(f"   Vision flag: {args.vision} | Source: {args.source}")
    print("   Daemon will pick it up on next cycle!")

if __name__ == "__main__":
    main()
