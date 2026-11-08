"""Turn merged PRs that touch python/termproof/** and python/tests/** into tasks.

Writes tasks/<id>/task.json (agent-visible) and hidden/<id>/{test.patch,reference.patch} (grader-only).
"""
import argparse


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", default="md-mt/termproof")
    p.add_argument("--clone", default="work/termproof")
    p.add_argument("--limit", type=int, default=15)
    p.parse_args(argv)
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
