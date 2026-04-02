import os
from datetime import datetime

class GrokMemory:
    def __init__(self):
        self.short_term = []  # ReAct trace
        self.topics_dir = "memory/topics"
        os.makedirs(self.topics_dir, exist_ok=True)

    def add_to_trace(self, entry: str):
        timestamp = datetime.now().isoformat()
        self.short_term.append(f"[{timestamp}] {entry}")
        print(f"🧠 Memory trace: {entry[:80]}...")

    def save_topic(self, topic: str, content: str):
        path = f"{self.topics_dir}/{topic.replace(' ', '_')}.md"
        with open(path, "a") as f:
            f.write(f"\n### {datetime.now().isoformat()}\n{content}\n")
        print(f"📁 Saved topic: {topic}")
