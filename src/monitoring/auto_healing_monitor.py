# src/monitoring/auto_healing_monitor.py — Auto-Healing Monitor (Phase 8)
import asyncio
import subprocess
import json
from datetime import datetime
import os

class AutoHealingMonitor:
    def __init__(self):
        self.services = ["grokforge-swarm", "grok-dream"]
        self.log_file = os.path.expanduser("~/GrokForge/healing.log")
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    async def _run_cmd(self, cmd: list) -> str:
        """Run shell command asynchronously — ALWAYS return output (even if returncode != 0)."""
        proc = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        output = (stdout.decode() + "\n" + stderr.decode()).strip()
        if not output:
            output = f"ERROR (returncode={proc.returncode}): no output"
        return output

    async def get_service_status(self, service: str) -> dict:
        """Get live systemctl status for a user service."""
        output = await self._run_cmd(["systemctl", "--user", "status", f"{service}.service", "--no-pager"])
        active = "active (running)" in output
        return {
            "service": service,
            "active": active,
            "status": "healthy" if active else "unhealthy",
            "last_check": datetime.now().isoformat(),
            "raw": output[:600] + "..." if len(output) > 600 else output
        }

    async def get_live_status(self) -> dict:
        """Return live status for all monitored services."""
        tasks = [self.get_service_status(svc) for svc in self.services]
        results = await asyncio.gather(*tasks)
        return {
            "timestamp": datetime.now().isoformat(),
            "services": {r["service"]: r for r in results},
            "overall_health": "healthy" if all(r["active"] for r in results) else "needs_attention"
        }

    async def heal_service(self, service: str) -> bool:
        """Attempt to heal a service (restart + grace period) and log the action."""
        if service not in self.services:
            return False

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "service": service,
            "action": "heal_attempted",
            "result": None
        }

        # Restart
        await self._run_cmd(["systemctl", "--user", "restart", f"{service}.service"])
        await asyncio.sleep(10)  # increased grace period for full restart

        status = await self.get_service_status(service)
        success = status["active"]

        log_entry["result"] = "success" if success else "failed"
        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

        return success
