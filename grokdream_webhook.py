#!/usr/bin/env python3
"""
Tier 10 — GrokDream Webhook/API Server
Send tasks instantly from anywhere: curl, browser, scripts, other machines.
"""
from flask import Flask, request, jsonify
import json
import redis
import time
import threading
import sys
sys.path.insert(0, ".")

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.get_json()
    if not data or not data.get("task"):
        return jsonify({"error": "Missing task"}), 400
    
    task_payload = {
        "task": data["task"],
        "source": data.get("source", "webhook"),
        "timestamp": time.time(),
        "requires_vision": data.get("requires_vision", False),
        "image_url": data.get("image_url")  # Grok-2 Vision image upload ready
    }
    
    r.rpush("grokdream:tasks", json.dumps(task_payload))
    print(f"📥 Webhook received task: {data['task'][:80]}... (vision: {data.get('requires_vision')})")
    return jsonify({"status": "task ingested", "task": data["task"]}), 200

def run_webhook():
    print("🌐 GrokDream Webhook/API running on http://localhost:5000/ingest")
    print("   Example: curl -X POST -H 'Content-Type: application/json' -d '{\"task\": \"Build the next city block\", \"requires_vision\": true}' http://localhost:5000/ingest")
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    run_webhook()
