# src/main_swarm.py — Phase 7.3 Production Entry Point (now daemonized for Phase 8)
# Wires native Grok tool calling + ReAct + self-improvement + keep-alive

import asyncio
from react_loop import execute_react_step_with_grok_tools
from self_improvement_loop import run_self_improvement_cycle
from tool_registry.grok_native_tools import registry

async def main():
    print("🚀 GrokForge Swarm (Phase 7.3 — Real LLM Tool Calling + Phase 8 Daemon)")
    # Register example tool for demo
    registry.register_tool(
        name="self_improve",
        description="Trigger autonomous self-improvement cycle",
        parameters={"reason": {"type": "string"}}
    )
    print(f"Loaded {len(registry.tool_definitions)} native Grok tools")

    # Demo ReAct step
    result = await execute_react_step_with_grok_tools("Start self-improvement cycle", [])
    print(result)

    # Run one self-improvement cycle on startup
    await run_self_improvement_cycle()
    print("✅ GrokForge Swarm ready for systemd launch — entering daemon mode")

    # === PHASE 8 KEEP-ALIVE LOOP ===
    print("🔄 Swarm daemon loop started (will self-improve every 60 min)")
    while True:
        try:
            await asyncio.sleep(3600)  # 1 hour — adjust as needed
            print("🔄 [Daemon tick] Running scheduled self-improvement...")
            await run_self_improvement_cycle()
        except Exception as e:
            print(f"⚠ Daemon loop error (continuing): {e}")
            await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
