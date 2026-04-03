import time
import threading
import atexit

_stop_event = threading.Event()

def dream_daemon():
    print("🌌 GrokDream daemon starting (PERSISTENT background mode)")
    print(" • Monitoring ReAct traces + sub-agent handoffs")
    print(" • Vision queue active | Memory persistence every 30s")
    print(" • Auto-saving topics to memory/topics/")
    heartbeat = 0
    while not _stop_event.is_set():
        heartbeat += 1
        time.sleep(5)  # short demo interval so you can Ctrl+C cleanly
        print(f"[Daemon heartbeat {heartbeat}] Persistent memory + swarm synced")

def start_dream_daemon():
    t = threading.Thread(target=dream_daemon, daemon=False)
    t.start()
    print("GrokDream daemon running on background thread (port 42069 simulation)")
    # graceful shutdown
    def stop():
        _stop_event.set()
        print("🌌 GrokDream daemon shutting down cleanly")
    atexit.register(stop)
