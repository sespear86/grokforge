# src/main_swarm.py — Phase 7.3 Production Entry Point
# Wires native Grok tool calling + ReAct + self-improvement

import asyncio
from src.react_loop import execute_react_step_with_grok_tools
from src.self_improvement_loop import run_self_improvement_cycle
from src.tool_registry.grok_native_tools import registry

async def main():
    print("🚀 Starting GrokForge Swarm (Phase 7.3 — Real LLM Tool Calling)")
    # Register example tool for demo
    registry.register_tool(
        name="self_improve",
        description="Trigger autonomous self-improvement cycle",
        parameters={"reason": {"type": "string"}}
    )
    print(f"Loaded {len(registry.tool_definitions)} native Grok tools")

    # Demo ReAct step with native calling
    result = await execute_react_step_with_grok_tools("Start self-improvement cycle", [])
    print(result)

    # Run one self-improvement cycle
    await run_self_improvement_cycle()
    print("✅ GrokForge Swarm ready for systemd launch")

if __name__ == "__main__":
    asyncio.run(main())
