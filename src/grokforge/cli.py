import argparse
from rich.console import Console
from grokforge.dream import start_dream_daemon, get_dream_status
from react.loop import run_autonomous_react_loop

console = Console()

def main():
    """Main CLI entrypoint (called by __main__.py)"""
    parser = argparse.ArgumentParser(
        description="GrokForge — Autonomous Feature Shipping with ReAct 2.0",
        prog="grokforge"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ship_feature command
    ship_parser = subparsers.add_parser("ship_feature", help="Autonomously ship a feature using ReAct 2.0")
    ship_parser.add_argument("feature_description", help="The feature to autonomously ship")
    ship_parser.add_argument("--dry-run", action="store_true", default=True, help="Simulate only (recommended for safety)")

    # dream command
    dream_parser = subparsers.add_parser("dream", help="Launch GrokDream autonomous mode")
    dream_parser.add_argument("--dry-run", action="store_true", default=True, help="Simulate only (recommended for safety)")

    args = parser.parse_args()

    console.print("[bold green]=== GROKFORGE DEBUG ===[/bold green]")
    console.print("DEBUG: cli.py loaded successfully")

    if args.command == "ship_feature":
        console.print("DEBUG: ship_feature registered")
        mode = "DRY-RUN (safe)" if args.dry_run else "LIVE"
        console.print(f"Mode: {mode}")
        run_autonomous_react_loop(args.feature_description, args.dry_run)

    elif args.command == "dream":
        console.print("DEBUG: dream command registered as top-level subcommand")
        mode = "DRY-RUN (safe)" if args.dry_run else "LIVE"
        console.print(f"Mode: {mode}")
        start_dream_daemon(args.dry_run)
        if args.dry_run:
            get_dream_status()

if __name__ == "__main__":
    main()
