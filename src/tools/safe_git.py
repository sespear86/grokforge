import subprocess
import os
from rich.console import Console
console = Console()

def _has_uncommitted_changes(cwd: str = ".") -> bool:
    """Return True if there are any changes to commit."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=cwd, capture_output=True, text=True, check=False
        )
        return bool(result.stdout.strip())
    except Exception:
        return True  # assume changes if we can't check

def safe_git_commit(commit_msg: str, cwd: str = ".", dry_run: bool = True) -> bool:
    if dry_run:
        console.print("[bold yellow]DRY-RUN: Would commit with message:[/bold yellow]")
        console.print(f" git commit -m \"{commit_msg}\"")
        return True

    try:
        if not _has_uncommitted_changes(cwd):
            console.print("[bold yellow]ℹ️ No changes to commit — feature already up-to-date[/bold yellow]")
            return True

        console.print("[bold blue]→ Staging all changes...[/bold blue]")
        subprocess.run(["git", "add", "."], cwd=cwd, check=True, capture_output=True)

        console.print(f"[bold blue]→ Committing: {commit_msg}[/bold blue]")
        result = subprocess.run(
            ["git", "commit", "--no-verify", "-m", commit_msg],
            cwd=cwd, check=True, capture_output=True
        )
        console.print(f"[bold green]✅ Committed:[/bold green] {commit_msg}")
        return True
    except subprocess.CalledProcessError as e:
        err = e.stderr.decode().strip() if e.stderr else str(e)
        if "nothing to commit" in err.lower():
            console.print("[bold yellow]ℹ️ No changes to commit — feature already up-to-date[/bold yellow]")
            return True
        console.print(f"[bold red]⚠ Git commit failed:[/bold red] {err}")
        return False

def safe_git_push(cwd: str = ".", dry_run: bool = True) -> bool:
    if dry_run:
        console.print("[bold yellow]DRY-RUN: Would push to origin[/bold yellow]")
        return True
    try:
        console.print("[bold blue]→ Pushing to origin/phase9-autonomous-shipping...[/bold blue]")
        result = subprocess.run(
            ["git", "push", "origin", "phase9-autonomous-shipping"],
            cwd=cwd, check=True, capture_output=True
        )
        console.print("[bold green]✅ Pushed to origin/phase9-autonomous-shipping[/bold green]")
        return True
    except subprocess.CalledProcessError as e:
        err = e.stderr.decode().strip() if e.stderr else str(e)
        console.print(f"[bold red]⚠ Git push failed:[/bold red] {err}")
        return False
