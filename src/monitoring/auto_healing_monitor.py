# src/monitoring/auto_healing_monitor.py
# Phase 8 — Auto-Healing Monitor (Option 3)
import asyncio
import subprocess
from datetime import datetime
from src.self_improvement_loop import run_self_improvement_cycle

async def check_service_health(service: str) -> bool:
    """Check if a user systemd service is active."""
    try:
        result = subprocess.run(
            ["systemctl", "--user", "is-active", service],
            capture_output=True, text=True
        )
        return result.stdout.strip() == "active"
    except:
        return False

async def run_auto_healing_cycle():
    """Phase 8 auto-healing loop."""
    print(f"🛡️ [{datetime.now()}] Starting Auto-Healing Cycle (Phase 8)")
    swarm_healthy = await check_service_health("grokforge-swarm.service")
    dream_healthy = await check_service_health("grok-dream.service")

    if not swarm_healthy or not dream_healthy:
        print("⚠️  Service unhealthy — triggering self-improvement + restart")
        await run_self_improvement_cycle()
        subprocess.run(["systemctl", "--user", "restart", "grokforge-swarm.service"])
        subprocess.run(["systemctl", "--user", "restart", "grok-dream.service"])
    else:
        print("✅ All services healthy")
    return "auto_heal_complete"

if __name__ == "__main__":
    asyncio.run(run_auto_healing_cycle())
