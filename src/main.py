import typer
import subprocess
from rich.console import Console
from pathlib import Path
from react.loop import run_autonomous_react_loop
from ui.rich_helpers import show_completion_message

console = Console()
app = typer.Typer(help="GrokForge — Autonomous Feature Shipping with ReAct 2.0")

def get_next_backlog_task():
    """Dynamically read GROK_BACKLOG.md and return the first unchecked task."""
    backlog_path = Path("GROK_BACKLOG.md")
    if not backlog_path.exists():
        return "[GROKDREAM] No backlog found — using placeholder"
    content = backlog_path.read_text()
    for line in content.splitlines():
        if line.strip().startswith("- [ ]"):
            task = line.strip()[5:].strip()
            return task
    return "[GROKDREAM] All tasks complete — engine idle"

def mark_task_complete(task_description: str):
    """Mark the shipped task as [x] in GROK_BACKLOG.md and commit it."""
    backlog_path = Path("GROK_BACKLOG.md")
    if not backlog_path.exists():
        return
    content = backlog_path.read_text()
    updated = content.replace(f"- [ ] {task_description}", f"- [x] {task_description}")
    backlog_path.write_text(updated)
    # Commit the backlog update
    subprocess.run(["git", "add", "GROK_BACKLOG.md"], check=True)
    subprocess.run(["git", "commit", "-m", f"chore(backlog): mark completed → {task_description[:80]}"], check=True)

@app.command()
def ship_feature(
    feature_description: str = typer.Argument(..., help="The feature to autonomously ship"),
    dry_run: bool = typer.Option(True, "--dry-run/--no-dry-run", help="Simulate only (recommended for safety)")
):
    """Autonomously ship a feature using ReAct 2.0."""
    console.print("[bold green]=== GROKFORGE DEBUG ===[/bold green]")
    console.print("DEBUG: main.py loaded successfully")
    console.print("DEBUG: ship_feature registered as root command")
    mode = "DRY-RUN (safe)" if dry_run else "LIVE MODE 🔥"
    console.print(f"Mode: {mode}")
    run_autonomous_react_loop(feature_description, dry_run)
    if not dry_run:
        show_completion_message(feature_description)

@app.command()
def dream(
    dry_run: bool = typer.Option(False, "--dry-run/--no-dry-run", help="Simulate only (recommended for safety)")
):
    """Launch GrokDream autonomous mode — dynamically picks next task from GROK_BACKLOG.md."""
    console.print("[bold green]=== GROKFORGE DEBUG ===[/bold green]")
    console.print("DEBUG: main.py loaded successfully")
    console.print("DEBUG: dream subcommand registered as top-level command")
    mode = "DRY-RUN (safe)" if dry_run else "LIVE MODE 🔥"
    console.print(f"Mode: {mode}")
    
    # Dynamic task selection (this is the permanent unlock)
    task = get_next_backlog_task()
    console.print(f"📋 Next task from GROK_BACKLOG.md: [bold]{task}[/bold]")
    
    run_autonomous_react_loop(task, dry_run)
    if not dry_run:
        mark_task_complete(task)
        show_completion_message(task)

# CLI entrypoint for console_scripts
def cli():
    """Entry point called by the installed grokforge command."""
    app()

if __name__ == "__main__":
    cli()
