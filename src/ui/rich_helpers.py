from rich.console import Console
console = Console()

def start_ship_feature(feature_description: str):
    console.print(f"[bold green]🚀 SHIPPING FEATURE:[/bold green] {feature_description}")

def dashboard_link():
    console.print("[bold blue]📊 Live Dashboard → http://localhost:8080[/bold blue]")
