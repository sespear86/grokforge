# tests/test_phase7_toolcalling.py
# Phase 7 smoke test for native Grok tool calling
import pytest
from src.tool_registry.grok_native_tools import registry

def test_grok_native_registry_initialization():
    assert len(registry.tool_definitions) == 0
    print("✅ Phase 7 native tool registry smoke test passed")
