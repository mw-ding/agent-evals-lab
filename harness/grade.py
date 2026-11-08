"""Graders. Outcome is the headline; trajectory checks are guardrails."""
from pathlib import Path


def grade_outcome(project_root: Path, test_patch: Path, test_modules: list[str]) -> dict:
    """Apply the held-back test patch, run only `test_modules`, return {"pass": 0|1, "detail": str}."""
    raise NotImplementedError


def grade_trajectory(trace: list[dict], max_turns: int) -> dict:
    """From a trace (turns of role/content), return {"no_test_edits": 0|1, "no_network": 0|1, "turns": int}."""
    raise NotImplementedError
