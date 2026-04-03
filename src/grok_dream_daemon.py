# src/grok_dream_daemon.py — Phase 7.3 GrokDreamV3 Daemon
import asyncio
from datetime import datetime
from src.self_improvement_loop import run_self_improvement_cycle

async def main():
    print(f"🌙 [{datetime.now()}] GrokDreamV3 Vision-Aware Daemon started (Phase 7.3)")
    while True:
        await asyncio.sleep(3600)  # hourly cycle
        print("🔄 Running scheduled self-improvement...")
        await run_self_improvement_cycle()

if __name__ == "__main__":
    asyncio.run(main())
