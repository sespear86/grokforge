import argparse
import sys
from grokforge.api import GrokAPIClient  # Phase 1 stub

def main():
    parser = argparse.ArgumentParser(
        prog="grokforge",
        description="GrokForge - the Grok-native agentic coding harness (xAI first, per PROJECT-BIBLE.md sections 1-8)"
    )
    subparsers = parser.add_subparsers(dest="command", help="GrokForge Phase 1 commands")

    # init
    init_p = subparsers.add_parser("init", help="Initialize a new GrokForge project")
    init_p.add_argument("path", nargs="?", default=".", help="Project path")
    init_p.add_argument("--name", required=True, help="Project name")

    # run
    run_p = subparsers.add_parser("run", help="Run a natural-language task with full Grok tools")
    run_p.add_argument("task", help="Task description")

    # dream
    dream_p = subparsers.add_parser("dream", help="Launch GrokDream background daemon")
    dream_p.add_argument("--port", type=int, default=42069, help="Daemon port")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    client = GrokAPIClient()  # Phase 1 stub

    if args.command == "init":
        print(f"🚀 GrokForge init: Created project \"{args.name}\" at {args.path}")
    elif args.command == "run":
        print(f"🔥 GrokForge running task: {args.task}")
        print("✅ GrokAPI client stub ready | Tools: code_execution, web_search, x_keyword_search, x_semantic_search")
    elif args.command == "dream":
        print(f"🌌 GrokDream daemon starting on port {args.port} (Phase 2 daemon stub)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
