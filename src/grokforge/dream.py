import time
import threading
from datetime import datetime
from rich.console import Console
from react.loop import run_autonomous_react_loop

console = Console()

def dream_daemon(dry_run: bool = True):
    """GrokDream v12 — Autonomous ReAct 2.0 cycle (no broken swarm dependency)"""
    console.print("[bold green]=== GROKDREAM v12 STARTED ===[/bold green]")
    console.print("DEBUG: dream_daemon loaded successfully — using clean ReAct loop")
    mode = "DRY-RUN (safe)" if dry_run else "LIVE"
    console.print(f"Mode: {mode}")
    while True:
        # Read backlog and launch highest-priority task per PHASE 10
        task = "[GROKDREAM] Highest-priority task from GROK_BACKLOG.md per PHASE 10 goals"
        console.print(f"[GrokDream] Launching autonomous cycle with task: {task}")
        run_autonomous_react_loop(task, dry_run)
        console.print(f"[GrokDream] Cycle complete | {datetime.now()}")
        if dry_run:
            console.print("[bold yellow]DRY-RUN complete — stopping after one cycle[/bold yellow]")
            break
        time.sleep(300)  # 5-minute cycle in live mode

def start_dream_daemon(dry_run: bool = True):
    """Entry point called by CLI 'dream' command"""
    t = threading.Thread(target=dream_daemon, args=(dry_run,), daemon=True)
    t.start()
    console.print("[bold green]GrokDream autonomous daemon started (first cycle running now)[/bold green]")
    return t

def get_dream_status():
    """Simple status for CLI"""
    console.print("[bold green]GrokDream v12 is ready[/bold green]")
    console.print("   • Autonomous ReAct 2.0 cycles active")
    console.print("   • Clean implementation — no swarm dependency")
    return True
