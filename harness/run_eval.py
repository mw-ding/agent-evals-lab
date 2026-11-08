"""Run every (task, rep) once through `claude -p` and grade it.

Writes .claude/hillclimb/fixer/<round>/results.jsonl, summary.json and traces/<id>_rep<k>.json
in the schema of vendor/anthropic-evals/eval-hillclimb.md. Resume is idempotent per (task, rep).
"""
import argparse


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--round", default="baseline", help="output dir name: baseline, v1, v2, ...")
    p.add_argument("--reps", type=int, default=2)
    p.add_argument("--concurrency", type=int, default=4)
    p.add_argument("--config", default="agent/fixer.toml")
    p.add_argument("--ids", nargs="*", help="limit to these task ids")
    p.parse_args(argv)
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
