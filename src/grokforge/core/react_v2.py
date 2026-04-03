# GrokForge — Phase 6: Full ReAct 2.0 Tool-Calling Engine
import json
from typing import Dict, List, Any
from grokforge.tools import ToolRegistry  # existing registry
from grokforge.swarm import AgentSwarm  # new swarm layer

class ReAct2:
    def __init__(self, vision_swarm=None, max_cycles=20):
        self.tool_registry = ToolRegistry()
        self.swarm = AgentSwarm()  # Multi-Agent Swarm Collaboration
        self.vision_swarm = vision_swarm  # VisionAwareSwarm link
        self.max_cycles = max_cycles
        self.memory = []  # stateful memory

    async def run(self, task: str, tools: List[str] = None) -> Dict:
        """Full ReAct 2.0 loop with parallel tool calling + swarm delegation"""
        self.memory.append({"role": "user", "content": task})
        cycle = 0
        
        while cycle < self.max_cycles:
            # 1. Thought (ReAct)
            thought = await self._generate_thought()
            self.memory.append({"role": "assistant", "content": thought})
            
            # 2. Action — parallel tool calling
            actions = await self._parse_actions(thought)
            if not actions:
                break  # final answer reached
            
            # 3. Parallel execution via ToolRegistry + Swarm delegation
            results = await self.tool_registry.execute_parallel(actions, swarm=self.swarm)
            
            # 4. Observation + VisionAwareSwarm enrichment if needed
            obs = {"observations": results}
            if self.vision_swarm:
                obs["vision"] = await self.vision_swarm.analyze(results)
            self.memory.append({"role": "observation", "content": json.dumps(obs)})
            
            cycle += 1
        
        # Final synthesis by DreamIntegrator agent
        final = await self.swarm.dream_integrate(self.memory)
        return {"final_answer": final, "cycles": cycle, "memory": self.memory}
