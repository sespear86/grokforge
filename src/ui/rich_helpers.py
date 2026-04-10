from rich.console import Console
console = Console()
def show_completion_message(task: str):
    console.print(f"╭───────────────────────────────────── GrokForge v0.1 ─────────────────────────────────────╮")
    console.print(f"│ 🎉 FEATURE SHIPPED SUCCESSFULLY! │")
    console.print(f"│ ✅ {task} │")
    console.print("╰──────────────────────────────────────────────────────────────────────────────────────────╯")
    console.print("🚀 You are now running true autonomous feature shipping!")
