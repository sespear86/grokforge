from rich.console import Console
from rich.panel import Panel
console = Console()

def start_ship_feature(feature_description: str):
    """Rich banner when a new ship command starts."""
    console.print(Panel(
        f"[bold magenta]🚀 GROKFORGE AUTONOMOUS SHIP[/bold magenta]\n"
        f"Feature: [cyan]{feature_description}[/cyan]",
        title="GrokForge ReAct 2.0",
        subtitle="Phase 9 — Live Mode",
        border_style="bright_blue"
    ))

def dashboard_link():
    """Print live dashboard link (Phase 8 feature)."""
    console.print("[bold blue]📊 Live Dashboard → http://localhost:8080[/bold blue]")

def show_completion_message(feature_description: str):
    """Final celebratory message after LIVE ship completes."""
    console.print(Panel(
        f"[bold green]🎉 FEATURE SHIPPED SUCCESSFULLY![/bold green]\n"
        f"[white]✅ {feature_description}[/white]\n\n"
        "[italic]Auto-committed & pushed to phase9-autonomous-shipping[/italic]",
        title="GrokForge v0.1",
        border_style="green"
    ))
    console.print("[bold green]🚀 You are now running true autonomous feature shipping![/bold green]")
