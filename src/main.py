import typer
from rich.console import Console
from react.loop import run_autonomous_react_loop
from ui.rich_helpers import show_completion_message

console = Console()
app = typer.Typer(help="GrokForge — Autonomous Feature Shipping with ReAct 2.0")

@app.command()
def ship_feature(
    feature_description: str = typer.Argument(..., help="The feature to autonomously ship"),
    dry_run: bool = typer.Option(True, "--dry-run/--no-dry-run", help="Simulate only (recommended for safety)")
):
    """Autonomously ship a feature using ReAct 2.0."""
    console.print("[bold green]=== GROKFORGE DEBUG ===[/bold green]")
    console.print("DEBUG: main.py loaded successfully")
    console.print("DEBUG: ship_feature registered as root command")
   
    mode = "🧪 DRY-RUN (safe)" if dry_run else "🚀 LIVE"
    console.print(f"Mode: {mode}")
    run_autonomous_react_loop(feature_description, dry_run)
    if not dry_run:
        show_completion_message(feature_description)

# CLI entrypoint for console_scripts
def cli():
    """Entry point called by the installed grokforge command."""
    app()

if __name__ == "__main__":
    cli()
