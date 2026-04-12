import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from memory.swarm_memory import SwarmMemory

def test_rust_multimodal():
    swarm = SwarmMemory("rust-test-swarm")
    swarm.register_agent("agent-beta")
    swarm.mine_multi_modal_collective("Imagine a futuristic GrokForge city", "image", {"vision": True})
    swarm.mine_multi_modal_agent("agent-beta", "Rust hot-paths are 100x faster", "text")
    results = swarm.rust_search_swarm("GrokForge", limit=5)
    print("✅ Rust + Multi-modal test passed –", len(results), "results")
    print(swarm.status())

if __name__ == "__main__":
    test_rust_multimodal()
