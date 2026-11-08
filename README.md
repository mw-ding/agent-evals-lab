# agent-evals-lab

A hands-on walk through Anthropic's agent-eval method. It builds one eval for a small coding agent ("fixer") that fixes real bugs taken from the [md-mt/termproof](https://github.com/md-mt/termproof) history, takes a baseline, then hill-climbs on it.

Plan and schedule: [PLAN.md](PLAN.md).

## Sources

- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), Anthropic Engineering, Jan 9 2026
- [`anthropics/skills` → claude-api evals guides](https://github.com/anthropics/skills/tree/main/skills/claude-api/shared/evals), vendored in [`vendor/anthropic-evals/`](vendor/anthropic-evals/) (Apache-2.0)
- [`anthropics/courses` → prompt_evaluations](https://github.com/anthropics/courses/tree/master/prompt_evaluations), for the optional Promptfoo lessons
- [`anthropics/agent-sdk-workshop`](https://github.com/anthropics/agent-sdk-workshop), for agent settings to climb on later

## Concept → file

| Concept (article) | Where it lives |
|---|---|
| Task | `tasks/<id>/task.json` |
| Reference solution | `hidden/<id>/reference.patch` |
| Grader (outcome) | `harness/grade.py`: held-back tests pass |
| Grader (trajectory) | `harness/grade.py`: no test edits, no network, turn/cost caps |
| Trial, transcript | `harness/run_eval.py` → `.claude/hillclimb/fixer/<round>/` |
| Agent harness (scaffold) | `agent/fixer.toml` + `claude -p` |
| Evaluation harness | `harness/` |
| pass@k, pass^k, noise | `harness/metrics.py` |
| Hill-climbing | `vendor/anthropic-evals/eval-hillclimb.md` |

## Commands

```
uv run python -m unittest discover -s tests -t .   # tests (also run in CI)
uv run scripts/mine_tasks.py --limit 15           # PRs → tasks/ + hidden/
uv run scripts/validate_tasks.py                  # reference passes, no-op fails
uv run harness/run_eval.py --round baseline --reps 2
```

Status: skeleton. Every module raises `NotImplementedError`; build them in the order in `PLAN.md`.
