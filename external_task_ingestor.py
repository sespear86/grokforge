#!/usr/bin/env python3
"""
Tier 9 — External Task Ingestor
Simple, fast way to feed tasks into the GrokDream daemon from anywhere (CLI, scripts, future webhooks).
"""
import argparse
import json
import time
import redis
import sys

def main():
    parser = argparse.ArgumentParser(description="🚀 External Task Ingestor for GrokDream Daemon")
    parser.add_argument("--task", type=str, required=True, help="Task description to inject")
    parser.add_argument("--source", type=str, default="external-cli", help="Source label (for tracking)")
    parser.add_argument("--vision", action="store_true", help="Flag if this task needs Grok-2 Vision processing")
    args = parser.parse_args()

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
