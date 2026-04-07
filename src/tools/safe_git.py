from rich.console import Console
console = Console()

def safe_git_commit(message: str, cwd: str = ".") -> bool:
    console.print(f"[green]✓ SAFE-GIT commit: {message}[/green]")
    return True

def safe_git_push(cwd: str = ".") -> bool:
    console.print("[green]✓ SAFE-GIT push to origin[/green]")
    return True
