# src/tool_registry/grok_native_tools.py
# Phase 7 — Native Grok LLM Tool-Calling Integration
# Adds strict JSON schema support for real Grok/xAI function calling

from typing import Dict, Any, List

class GrokNativeToolRegistry:
    """Native Grok function-calling schema generator and validator (Phase 7)."""

    def __init__(self):
        self.tool_definitions: List[Dict[str, Any]] = []

    def register_tool(self, name: str, description: str, parameters: Dict[str, Any]):
        """Register a tool using exact Grok/xAI JSON schema format."""
        tool_schema = {
            "type": "function",
            "function": {
                "name": name,
                "description": description,
                "parameters": {
                    "type": "object",
                    "properties": parameters,
                    "required": list(parameters.keys()),
                    "additionalProperties": False
                }
            }
        }
        self.tool_definitions.append(tool_schema)
        print(f"✅ Registered native Grok tool: {name}")

    def get_grok_schema(self) -> Dict[str, Any]:
        """Return full schema ready for Grok API tool_calls parameter."""
        return {"tools": self.tool_definitions}

    def validate_tool_call(self, tool_call: Dict[str, Any]) -> bool:
        """Basic validation for incoming Grok tool calls."""
        return (
            "function" in tool_call
            and "name" in tool_call["function"]
            and "arguments" in tool_call["function"]
        )

# Auto-register core tools on import (Phase 7 style)
registry = GrokNativeToolRegistry()
# Example registrations will be expanded in next blocks
print("🚀 GrokNativeToolRegistry initialized for Phase 7")
