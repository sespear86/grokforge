import time
import threading
import os
from datetime import datetime
from grokforge.memory import GrokMemory
from grokforge.swarm import VisionAwareSwarm

memory = GrokMemory()
swarm = VisionAwareSwarm()

def dream_daemon():
    print("🚀 GrokDream v3 — Autonomous Swarm + ReAct 2.0 (Phase 5 LOCKED)")
    print("   • Runs first cycle immediately")
    print("   • Then every 300s (5 min) forever")
    print("   • Semantic memory + vision + swarm self-improvement")
    print("   • Ready for systemd persistence")
    counter = 0
    while True:
        counter += 1
        # Autonomous cycle (ReAct 2.0 stub ready for full tool calling)
        if memory.short_term:
            summary = f"Autonomous consolidation {counter} — {len(memory.short_term)} traces"
            memory.save_topic("auto_consolidated", summary)
            memory.short_term.clear()
        latest_topics = memory.list_topics()[:5]
        swarm_task = f"Review recent memory topics: {latest_topics}. Suggest ONE concrete improvement task for GrokForge using full xAI tools."
        swarm_result = swarm.run(swarm_task)  # VisionAwareSwarm now carries ReAct 2.0 context
        memory.save_topic("swarm_insight", f"Swarm cycle {counter}", swarm_result)
        print(f"[GrokDream] Cycle {counter} complete | Swarm insight saved | {datetime.now()}")
        time.sleep(300)  # sleep AFTER first cycle

def start_dream_daemon():
    t = threading.Thread(target=dream_daemon, daemon=True)
    t.start()
    print("✅ GrokDream v3 autonomous daemon started (first cycle running now)")
    return t

def get_dream_status():
    """Simple status for CLI"""
    print("✅ GrokDream v3 is running (background thread)")
    print("   • Autonomous cycles with VisionAwareSwarm active")
    print("   • Semantic memory + ReAct 2.0 ready")
    print(f"   • Latest topics: {len(memory.list_topics())} in memory/topics/")
    return True
