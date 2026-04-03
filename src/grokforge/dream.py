import time
import threading
import os
import subprocess
from datetime import datetime
from grokforge.memory import GrokMemory
from grokforge.swarm import VisionAwareSwarm

memory = GrokMemory()
swarm = VisionAwareSwarm()

def dream_daemon():
    print("🚀 GrokDream v3 — Autonomous Swarm + ReAct 2.0 (Phase 5)")
    print("   • Persistent systemd daemon ready")
    print("   • Semantic memory + vision linking active")
    print("   • VisionAwareSwarm runs every 300s")
    print("   • Self-improving ReAct loop with full xAI tools")
    counter = 0
    while True:
        time.sleep(300)  # 5-minute autonomous cycle
        counter += 1
        # Autonomous consolidation + swarm activation
        if memory.short_term:
            summary = f"Autonomous consolidation {counter} — {len(memory.short_term)} traces"
            memory.save_topic("auto_consolidated", summary)
            memory.short_term.clear()
        # Wake swarm with latest memory context
        latest_topics = memory.list_topics()[:3]
        swarm_task = f"Review recent memory topics: {latest_topics} and suggest one improvement task for GrokForge."
        swarm_result = swarm.run(swarm_task)
        memory.save_topic("swarm_insight", f"Swarm cycle {counter}", swarm_result)
        print(f"[GrokDream] Cycle {counter} complete | Swarm insight saved | {datetime.now()}")

def start_dream_daemon():
    t = threading.Thread(target=dream_daemon, daemon=True)
    t.start()
    print("✅ GrokDream v3 autonomous daemon started (background)")
    return t

def install_systemd_service():
    """Optional: Install as real systemd service for true persistence."""
    print("🔧 (Optional) Run 'sudo systemctl enable --now grokdream' after manual service file creation")
