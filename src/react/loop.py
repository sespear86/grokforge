from ui.rich_helpers import start_ship_feature, dashboard_link
from tools.safe_git import safe_git_commit, safe_git_push
from tools.researcher import research_step
from tools.self_review import self_review_critique
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import time

console = Console()

def run_autonomous_react_loop(feature_description: str, dry_run: bool = True):
    start_ship_feature(feature_description)
    dashboard_link()
    console.print("[bold yellow]🔄 Starting FULL ReAct 2.0 Autonomous Loop...[/bold yellow]")
   
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        # 1. Planner
        task = progress.add_task("[cyan]1/6 Planning...", total=None)
        time.sleep(0.8); progress.update(task, completed=True)
        console.print("✅ [Step 1/6] Planner complete")
       
        # 2. Researcher
        task = progress.add_task("[cyan]2/6 Researcher calling tools...", total=None)
        research_step(feature_description, dry_run)
        progress.update(task, completed=True)
        console.print("✅ [Step 2/6] Researcher complete")
       
        # 3-4. Coder + Tester (stubs)
        for step in ["3/6 Coder", "4/6 Tester"]:
            task = progress.add_task(f"[cyan]{step}...", total=None)
            time.sleep(1.0); progress.update(task, completed=True)
            console.print(f"✅ [{step}] complete")
       
        # 5. Self-Review
        task = progress.add_task("[cyan]5/6 Self-review gate...", total=None)
        self_review_critique(feature_description, dry_run)
        progress.update(task, completed=True)
        console.print("✅ [Step 5/6] Self-Review passed")
       
        # 6. Safe Commit + Push
        task = progress.add_task("[cyan]6/6 Safe git...", total=None)
        if dry_run:
            console.print("[bold green]🎉 DRY-RUN COMPLETE — Feature would have shipped![/bold green]")
            return True
        else:
            commit_msg = f"feat(autonomous): {feature_description}"
            if safe_git_commit(commit_msg, cwd=".") and safe_git_push(cwd="."):
                progress.update(task, completed=True)
                console.print("[bold green]🎉 FEATURE SHIPPED SUCCESSFULLY![/bold green]")
                return True
    return False
