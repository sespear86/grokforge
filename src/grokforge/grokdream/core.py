# Phase 6 integration — Multi-Agent Swarm + ReAct 2.0 + VisionAwareSwarm
from grokforge.core.react_v2 import ReAct2
from grokforge.swarm import AgentSwarm
from grokforge.vision import VisionAwareSwarm  # now present

class GrokDreamV3:
    def __init__(self):
        self.vision_swarm = VisionAwareSwarm()
        self.swarm = AgentSwarm()

    async def immediate_cycle(self, task: str):
        """Full autonomous cycle: ReAct 2.0 → Multi-Agent Swarm → Dream synthesis"""
        react = ReAct2(vision_swarm=self.vision_swarm)
        result = await react.run(task)
        await self.swarm.log_cycle(result)
        return result
