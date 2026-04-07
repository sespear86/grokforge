import typer
import sys
from rich.console import Console

console = Console()

# === DEBUG SECTION ===
print("=== GROKFORGE DEBUG ===", file=sys.stderr)
print("DEBUG: main.py loaded as module", file=sys.stderr)
print(f"DEBUG: src in path? {any('src' in p for p in sys.path)}", file=sys.stderr)
# === END DEBUG ===

typer_app = typer.Typer(
    name="grokforge",
    help="GrokForge — Grok-native agentic coding harness (xAI first)",
    no_args_is_help=True,
)

@typer_app.command("ship")
def ship_feature(
    feature_description: str = typer.Argument(..., help="The feature to autonomously ship"),
    dry_run: bool = typer.Option(True, "--dry-run/--no-dry-run", help="Simulate only (recommended)")
):
    """Autonomously ship a feature using ReAct 2.0."""
    console.print(f"[bold]Mode:[/bold] {'🧪 DRY-RUN (safe)' if dry_run else '🚀 LIVE'}")
    from react.loop import run_autonomous_react_loop
    success = run_autonomous_react_loop(feature_description, dry_run=dry_run)
    if success:
        console.print("[bold magenta]🚀 GrokForge autonomous cycle complete![/bold magenta]")
    else:
        console.print("[bold red]Ship cycle ended with issues[/bold red]")

# === DEBUG SECTION (safe) ===
print("DEBUG: ship command successfully registered via decorator", file=sys.stderr)
print("DEBUG: cli() entrypoint defined", file=sys.stderr)
# === END DEBUG ===

def cli():
    """Main CLI entry point."""
    typer_app()

if __name__ == "__main__":
    cli()
