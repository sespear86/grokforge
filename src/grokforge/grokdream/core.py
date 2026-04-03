# Phase 6 integration — Multi-Agent Swarm + ReAct 2.0
from grokforge.core.react_v2 import ReAct2
from grokforge.swarm import AgentSwarm

class GrokDreamV3:
    async def immediate_cycle(self, task):
        react = ReAct2(vision_swarm=self.vision_swarm)
        result = await react.run(task)
        await self.swarm.log_cycle(result)  # persistent swarm history
        return result
