"""Per-trial sandbox: a history-free snapshot of the source repo at a commit."""
from pathlib import Path


def make_sandbox(repo_dir: Path, base_sha: str, subdir: str = "python") -> Path:
    """`git archive base_sha subdir` into a fresh temp dir; return the project root inside it.

    No .git, no future history, nothing from hidden/.
    """
    raise NotImplementedError


def remove_sandbox(path: Path) -> None:
    raise NotImplementedError
