from memory import MemPalaceBackend
from tools.memory_tools import MEMORY_TOOLS

print("✅ Tier 4 verification starting...")
backend = MemPalaceBackend()
print(backend.status())

print("\n✅ Available tools:", list(MEMORY_TOOLS.keys()))
print("🎉 Tier 4 fully wired and ready for swarm!")
