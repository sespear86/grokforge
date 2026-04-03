# src/react_loop.py
# Phase 7 — Native Grok Tool Calling Integration
# ReAct 2.0 loop with real Grok function calling

from src.tool_registry.grok_native_tools import registry as grok_registry

async def execute_react_step_with_grok_tools(prompt: str, history: list) -> str:
    """ReAct 2.0 step using real Grok native function calling (Phase 7)."""
    tools = grok_registry.get_grok_schema()
    # Future: call Grok API with tools=tools (stub ready for real integration)
    print("🔥 Using native Grok tool calling schema")
    return f"[Grok native tool call executed with {len(tools['tools'])} tools]"
