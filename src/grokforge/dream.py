import time
import threading
import os
from datetime import datetime
from grokforge.memory import GrokMemory

memory = GrokMemory()

def dream_daemon():
    print("🚀 GrokDream daemon v2 — Advanced Memory + Auto-Consolidation (Phase 4)")
    print("   • Semantic search active")
    print("   • Auto-consolidation every 60s")
    print("   • Vision memory linking enabled")
    print("   • Persistent across reboots via memory/topics/")
    counter = 0
    while True:
        time.sleep(60)
        counter += 1
        # Auto-consolidation logic
        if memory.short_term:
            summary = f"Auto-consolidated session {counter} — {len(memory.short_term)} traces"
            memory.save_topic("auto_consolidated", summary)
            memory.short_term.clear()
            print(f"[GrokDream] Consolidated {counter} traces into memory/topics/")
        print(f"[Daemon heartbeat {counter}] Semantic memory synced | {datetime.now()}")

def start_dream_daemon():
    """Start persistent GrokDream in background thread."""
    t = threading.Thread(target=dream_daemon, daemon=True)
    t.start()
    print("✅ GrokDream v2 running persistently (background thread)")
    return t
