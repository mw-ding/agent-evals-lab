# Agent Evals Lab — plan

**Last updated:** 2026-11-08

Goal, in about 2 hours: learn Anthropic's agent-eval method by building one working eval on a real GitHub project, taking a baseline, and running one hill-climb round. A coding agent writes the code; The owner reads, decides, and inspects the failures.

## Sources (checked on GitHub / anthropic.com today)

| Source | Use it for | License |
|---|---|---|
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (Jan 9 2026) | Vocabulary, capability vs regression suites, pass@k / pass^k | link only |
| `anthropics/skills` → `skills/claude-api/shared/evals/` | `build-eval.md`, `eval-audit.md`, `eval-hillclimb.md`, report builder, `SCHEMA.md` | Apache-2.0: vendor with LICENSE and pinned commit |
| `anthropics/courses` → `prompt_evaluations/` | Promptfoo lessons 05–09 (optional, later) | no license stated: link only, don't copy |
| `anthropics/agent-sdk-workshop` | Agent settings to climb on later | link only |

## Design

**Agent under test ("fixer").** Headless `claude -p` given a task prompt and a repo snapshot. Levers: appended system prompt, allowed tools, max turns, model.

**Tasks from md-mt/termproof history (SWE-bench style).** 12–15 merged PRs touching `python/` source plus tests (92 of the last 141 merged PRs change tests).
- Each task: a snapshot of the parent commit, the PR description as the prompt, and the PR's test changes held back.
- The merged PR must pass the grader, which proves the task is solvable.
- A no-op patch must fail the grader, which proves the grader can tell the difference.
- Grading runs only the PR's own test files: seconds per trial. The full suite takes 2m25s and isn't needed.

**Graders.**
- Outcome (headline, binary): the held-back tests pass.
- Trajectory checks: no edits to test files, no network fetches, turn and cost caps.

**Contamination.**
- termproof and this lab repo are both public, so hidden tests and reference patches are reachable on the web.
- Defense: the agent gets no web tools, works in a `git archive` snapshot with no history, and hidden files are never copied into its sandbox.
- Screen passing transcripts for fetches.

**Harness.**
- Fresh temp directory per trial.
- 4 trials run concurrently.
- Output uses the hill-climb guide's `results.jsonl` and `traces/` schema, so Anthropic's report builder works unchanged.
- Each row records the model taken from the response, usage, and the grade.
- Reported metrics: pass rate with a 95% confidence interval, pass@k, pass^k, cost, latency.

**Public-repo hygiene.** Commit task definitions, harness, and reports. Keep raw transcripts gitignored by default, and never commit owner/personal facts.

## Repo: `mw-ding/agent-evals-lab` (public), `~/src/agent-evals-lab`

```
README.md                 concept → file map
vendor/anthropic-evals/   claude-api evals guides + report builder, LICENSE, commit pin
tasks/<id>/task.json      prompt, base_sha, tags (agent-visible)
hidden/<id>/              test patch, reference patch (grader-only)
agent/fixer.toml          levers: prompt, tools, max_turns, model
harness/{sandbox,run_eval,grade,metrics}.py
scripts/{mine_tasks,validate_tasks}.py
.claude/hillclimb/fixer/  _state.json, baseline/, v1/
```

## About 2 hours

| Time | Step | What you learn |
|---|---|---|
| 0:00–0:15 | Create repo, `uv` env, vendor the guides; you skim the article | Vocabulary |
| 0:15–0:40 | Mine 12–15 tasks; validate (reference passes, no-op fails) | Tasks, reference solutions, isolation |
| 0:40–1:00 | Harness and fixer; one smoke trial; check the model from the response | Harness, transcripts |
| 1:00–1:30 | Baseline 15 × 2 reps in the background; you read the guide's Step 0.5 meanwhile | Trials, noise |
| 1:30–2:00 | Audit; you read failed transcripts and sort each into agent / task / grader / environment; one hill-climb round | Reading transcripts, hill-climbing |

Cut from the first version: Promptfoo warm-up, model judge, held-out validation slice, GEPA. All of these are follow-ups.

Caveats:
- 15 tasks × 2 reps gives a margin of about ±18 points, so the round-1 result is directional, not proof. Raise reps or tasks next session.
- Trials use your Claude subscription quota.
- If trials run long (more than 5 min each), the baseline slips past 1:30.

## Decisions (2026-11-08)

1. Agent runtime: headless `claude -p` with your Claude login.
2. Built by a fresh Claude Code session in this repo, following `CLAUDE.md`.
