# ai-dan-factory-core

AI-DAN Factory — GitHub-native execution engine for a solo operator.

## Purpose

A lightweight, Python-only pipeline that moves a product brief through a fixed
set of stages: validate → discovery → repo → inject → deploy → quality → monitor.

No frameworks. No containers. Just plain Python modules wired together by a
single orchestrator.

## Structure

```
contracts/          # Input/output data contracts (plain dataclasses)
  build_brief.py    # BuildBrief — input contract for a factory run
  factory_result.py # FactoryResult — output contract for a completed run
stages/             # One function per pipeline stage
  validate.py       # Validate the build brief
  discovery.py      # Discover context and resources
  repo.py           # Set up the target repository
  inject.py         # Inject code or assets
  deploy.py         # Deploy the project
  quality.py        # Run quality checks
  monitor.py        # Monitor deployment health
scripts/            # Utility scripts (placeholder)
orchestrator.py     # run_factory() — runs all stages in sequence
.github/workflows/  # CI workflow that executes the orchestrator
```

## Contracts

**BuildBrief** — input to every factory run:
- `version`, `project_id`, `project_name`
- `problem`, `solution`, `target_user`, `monetization`
- `target_repo`, `constraints`

**FactoryResult** — output of every factory run:
- `version`, `project_id`, `run_id`, `status`, `stage`
- `repo_url`, `deployment_url`, `health_status`
- `quality_score`, `monitor_signal`, `recommended_action`
- `last_checked_at`, `error_message`

## Stage Output Format

Every stage function returns a dict with exactly three keys:

```json
{"stage": "<name>", "status": "ok", "summary": "<message>"}
```

## Usage

```bash
python orchestrator.py
```

## Rules

- No business logic yet — all stages return placeholder values
- No external dependencies — Python standard library only
- This repo is execution only: no strategy, no decision engine, no budget logic
- Keep everything simple, modular, and Python-based
