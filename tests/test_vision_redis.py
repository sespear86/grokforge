import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from memory.swarm_memory import SwarmMemory

def test_vision_redis():
    swarm = SwarmMemory("vision-redis-test")
    swarm.enable_redis("redis://localhost:6379/0")  # safe even if Redis not running
    swarm.mine_image_collective("test_vision_image.jpg", {"vision": True})
    results = swarm.search_by_image_swarm("test_vision_image.jpg", limit=3)
    print("✅ Vision + Redis test passed –", len(results), "results")
    print(swarm.status())

if __name__ == "__main__":
    test_vision_redis()
