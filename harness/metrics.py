"""Aggregate metrics, recomputed from results.jsonl rows."""


def pass_at_k(n: int, c: int, k: int) -> float:
    """Chance at least one of k trials passes, given c passes out of n trials."""
    raise NotImplementedError


def pass_hat_k(n: int, c: int, k: int) -> float:
    """Chance all k trials pass (pass^k), given c passes out of n trials."""
    raise NotImplementedError


def ci_halfwidth(p: float, n: int, z: float = 1.96) -> float:
    """95% CI half-width for a pass rate p over n trials."""
    raise NotImplementedError
