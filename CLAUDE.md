# Building this repo

You are the builder. The owner is learning the eval method and has about 2 hours. Follow `PLAN.md` step by step and keep it moving: write the code, run it, and show results. The owner reads, decides, and reads the failure transcripts.

## Rules

- Read `vendor/anthropic-evals/build-eval.md`, `eval-audit.md` and `eval-hillclimb.md` before building. Follow their file layout and field names: `results.jsonl`, `summary.json`, `_state.json`, `traces/<id>_rep<k>.json`. Vendored files are read-only.
- Python 3.12+ with `uv`. Use only the standard library unless a dependency clearly saves time.
- Write small unit tests for `grade.py`, `metrics.py` and `sandbox.py`. Use `unittest`.
- Commit at each step in `PLAN.md`, in small commits. This repo is **public**: never commit secrets, personal facts or raw transcripts (`traces/` is gitignored).

## Agent under test

Headless Claude Code, run once per trial in its own temp sandbox:

```
claude -p "<task prompt>" --output-format stream-json --verbose \
  --model <model> --max-turns <n> --permission-mode acceptEdits \
  --allowedTools "Read,Edit,Write,Glob,Grep,Bash" \
  --disallowedTools "WebFetch,WebSearch" \
  --append-system-prompt-file agent/<variant>.md
```

- Run from inside the sandbox dir. Settings levers live in `agent/fixer.toml`.
- Take `model` and `usage` from the stream's result/assistant events, never from config.
- Check whether `--max-budget-usd` applies under a subscription login before relying on it.
- Run 4 trials concurrently, with a timeout per trial. Resume must be idempotent per (case, rep).

## Tasks and isolation

- Source repo: `md-mt/termproof`, `python/` only. Clone it to `work/termproof`.
- Mine merged PRs whose diff touches both `python/termproof/**` and `python/tests/**`.
  - Prompt = the PR title and body, with diff hunks and test names removed.
  - Split the diff into `hidden/<id>/test.patch` and `hidden/<id>/reference.patch`.
- Sandbox = `git archive <parent sha> python/` extracted into a temp dir: no `.git`, no future history, nothing from `hidden/`.
- Grade by applying `test.patch` to the agent's final tree, then running only the touched test files: `uv run python -m unittest <modules>`. The full suite takes about 2.5 min, so don't run it.
- Validate every task before use: reference + tests must pass and no-op + tests must fail. Drop tasks that don't.
- Trajectory checks:
  - no edits to `tests/`
  - no web or `gh` or `git clone` calls in the transcript
  - turn count
- Flag any pass that fetched termproof or this repo.

## Checkpoints: stop and show the owner

1. After validation: list the tasks, which ones were dropped and why.
2. After the smoke trial: the transcript path, model, tokens and time.
3. After the baseline:
   - pass rate with a 95% confidence interval, pass@2 and pass^2
   - the noise floor
   - the 3 lowest cases, each sorted into agent / task / grader / environment
4. Before round 1: the one lever to change and why. Get a yes.
