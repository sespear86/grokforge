from memory.swarm_memory import SwarmMemory

def test_swarm():
    swarm = SwarmMemory("test-swarm")
    swarm.register_agent("agent-alpha")
    swarm.mine_collective("GrokForge is building the ultimate agentic harness", {"phase": "tier4"})
    swarm.mine_agent("agent-alpha", "Rust hot-paths incoming", {"priority": "high"})
    results = swarm.search_swarm("GrokForge", limit=5)
    print("✅ Swarm test passed –", len(results), "results found")
    print(swarm.status())

if __name__ == "__main__":
    test_swarm()
