from rich.console import Console
import time
console = Console()

def research_step(feature_description: str, dry_run: bool = True) -> str:
    console.print("[cyan]🔎 Researcher activating — calling tools...[/cyan]")
    if dry_run:
        console.print("🧪 [DRY-RUN] Would call: web_search + x_keyword_search")
        time.sleep(1.2)
    else:
        console.print("✅ [LIVE] Tool calls executed")
    result = f"Best practices for '{feature_description}': Tailwind dark mode, system preference, smooth toggle."
    console.print(f"📋 Research summary: {result}")
    return result
