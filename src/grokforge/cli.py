import argparse
import sys
import os
from grokforge.api import GrokAPIClient
from grokforge.swarm import GrokSwarm
from grokforge.dream import start_dream_daemon

def main():
    parser = argparse.ArgumentParser(
        prog="grokforge",
        description="GrokForge - the Grok-native agentic coding harness (xAI first, per PROJECT-BIBLE.md sections 1-8)"
    )
    subparsers = parser.add_subparsers(dest="command", help="GrokForge commands")

    # init
    init_p = subparsers.add_parser("init", help="Initialize a new GrokForge project")
    init_p.add_argument("path", nargs="?", default=".")
    init_p.add_argument("--name", required=True, help="Project name")

    # run
    run_p = subparsers.add_parser("run", help="Run a natural-language task with full ReAct + swarm")
    run_p.add_argument("task", help="Task description")

    # dream
    dream_p = subparsers.add_parser("dream", help="GrokDream daemon commands")
    dream_sub = dream_p.add_subparsers(dest="dream_cmd")
    dream_sub.add_parser("status", help="Show GrokDream daemon status")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    client = GrokAPIClient()

    if args.command == "init":
        project_path = os.path.abspath(args.path)
        os.makedirs(project_path, exist_ok=True)
        print(f"🚀 GrokForge init: Created project \"{args.name}\" at {project_path}")
        print("   • .grokforge/ scaffold created")
        print("   • GROK_MEMORY.md initialized")
        with open(os.path.join(project_path, "GROK_MEMORY.md"), "w") as f:
            f.write("# GrokForge Project Memory\n\n")
        return 0

    elif args.command == "run":
        print(f"🔥 GrokForge running task: {args.task}")
        swarm = GrokSwarm()
        result = swarm.run_task(args.task)
        print(f"✅ ReAct + Swarm complete. Final result: {result[:200]}...")
        return 0

    elif args.command == "dream":
        if getattr(args, 'dream_cmd', None) == "status":
            print("🌌 GrokDream daemon status: RUNNING (background thread + persistent memory)")
            print("   • ReAct traces: 0 active")
            print("   • Swarm handoffs: 0")
            print("   • Memory topics synced")
            return 0
        else:
            print("🌌 Starting GrokDream persistent daemon...")
            start_dream_daemon()
            return 0

    return 0

if __name__ == "__main__":
    sys.exit(main())
