"""Keep a task only if reference + tests pass and no-op + tests fail."""
import argparse


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ids", nargs="*", help="limit to these task ids")
    p.parse_args(argv)
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
