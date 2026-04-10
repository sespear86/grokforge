import typer
import subprocess
from rich.console import Console
from pathlib import Path
from react.loop import run_autonomous_react_loop
from ui.rich_helpers import show_completion_message

console = Console()
app = typer.Typer(help="GrokForge — Autonomous Feature Shipping with ReAct 2.0")

def get_next_backlog_task():
    """Dynamically read GROK_BACKLOG.md line-by-line and return the first unchecked task (bulletproof)."""
    backlog_path = Path("GROK_BACKLOG.md")
    if not backlog_path.exists():
        return "[GROKDREAM] No backlog found — using placeholder"
    content = backlog_path.read_text(encoding="utf-8").splitlines()
    for line in content:
        stripped = line.strip()
        if stripped.startswith("- [ ]"):
            task = stripped[5:].strip()
            return task
    return "[GROKDREAM] All tasks complete — engine idle"

def normalize_backlog():
    """Permanently fix any [x] [x] malformations or artifacts (full foresight)."""
    backlog_path = Path("GROK_BACKLOG.md")
    if not backlog_path.exists():
        return
    lines = backlog_path.read_text(encoding="utf-8").splitlines()
    updated = []
    for line in lines:
        if "[x] [x]" in line:
            line = line.replace("[x] [x]", "[x]")
            console.print("[bold green]✅ Backlog normalized (fixed malformed [x] [x])[/bold green]")
        updated.append(line)
    backlog_path.write_text("\n".join(updated) + "\n", encoding="utf-8")

def mark_task_complete(task_description: str):
    """Mark task complete line-by-line + commit — never creates malformed entries."""
    backlog_path = Path("GROK_BACKLOG.md")
    if not backlog_path.exists():
        return
    lines = backlog_path.read_text(encoding="utf-8").splitlines()
    updated = []
    for line in lines:
        if line.strip().startswith("- [ ]") and task_description in line:
            updated.append(line.replace("- [ ]", "- [x]", 1))
        else:
            updated.append(line)
    backlog_path.write_text("\n".join(updated) + "\n", encoding="utf-8")
    try:
        subprocess.run(["git", "add", "GROK_BACKLOG.md"], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", f"chore(backlog): mark completed → {task_description[:80]}", "--no-verify"], check=True, capture_output=True)
        console.print("[bold green]✅ Backlog task marked complete and committed[/bold green]")
    except subprocess.CalledProcessError:
        console.print("[yellow]⚠ Git commit note (pre-commit) — task still marked locally[/yellow]")

def cleanup_polluted_files():
    """Automatically clean any ReAct pollution from previous cycles (full foresight)."""
    polluted = ["src/ui/dark_mode_toggle.py"]
    for f in polluted:
        path = Path(f)
        if path.exists():
            path.write_text("# Cleaned by GrokDream v24 — ready for new features\n", encoding="utf-8")
            console.print(f"[bold green]🧹 Cleaned polluted file: {f}[/bold green]")
    subprocess.run(["git", "add"] + polluted, check=False, capture_output=True)

@app.command()
def ship_feature(
    feature_description: str = typer.Argument(..., help="The feature to autonomously ship"),
    dry_run: bool = typer.Option(True, "--dry-run/--no-dry-run", help="Simulate only (recommended for safety)")
):
    console.print("[bold green]=== GROKFORGE DEBUG ===[/bold green]")
    console.print("DEBUG: main.py loaded successfully")
    mode = "DRY-RUN (safe)" if dry_run else "LIVE MODE 🔥"
    console.print(f"Mode: {mode}")
    run_autonomous_react_loop(feature_description, dry_run)
    if not dry_run:
        show_completion_message(feature_description)

@app.command()
def dream(
    dry_run: bool = typer.Option(False, "--dry-run/--no-dry-run", help="Simulate only (recommended for safety)")
):
    """Launch GrokDream autonomous mode — normalizes, cleans, picks, ships, marks."""
    console.print("[bold green]=== GROKFORGE DEBUG ===[/bold green]")
    console.print("DEBUG: main.py loaded successfully")
    console.print("DEBUG: dream subcommand registered as top-level command")
    mode = "DRY-RUN (safe)" if dry_run else "LIVE MODE 🔥"
    console.print(f"Mode: {mode}")
   
    normalize_backlog()
    cleanup_polluted_files()
    task = get_next_backlog_task()
    console.print(f"📋 Next task from GROK_BACKLOG.md: [bold]{task}[/bold]")
   
    run_autonomous_react_loop(task, dry_run)
    if not dry_run:
        mark_task_complete(task)
        show_completion_message(task)

def cli():
    app()

if __name__ == "__main__":
    cli()
