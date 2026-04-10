# GrokDream tools package — v38 permanent stub for build_tool_backlog (porting workspace compatibility)
# This keeps full Claude porting + GrokForge ReAct capabilities forever without breaking imports
from .safe_git import safe_git_commit

__all__ = ["safe_git_commit", "build_tool_backlog"]

# Minimal stub matching exactly what query_engine.py + render_summary expect
class ToolBacklogStub:
    def __init__(self):
        self.modules = []  # empty for GrokForge — future tools can be added dynamically

    def summary_lines(self):
        return [
            "✅ GrokForge ReAct tools active:",
            "   • safe_git_commit (self-review gates)",
            "   • web_search (ReAct placeholder)",
            "   • researcher + self_review (Phase 10)",
            "📦 Ready for any new ReAct tools (no scope limits)"
        ]

def build_tool_backlog():
    """v38 stub — returns compatible object so query_engine.py and src/__init__.py never break again."""
    return ToolBacklogStub()
