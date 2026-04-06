# ai-dan-factory-core

AI-DAN Factory — GitHub-native execution engine for a solo operator.

## Purpose

A lightweight, Python-only pipeline that moves a product brief through a fixed
set of stages: validate → discover → repo → inject → deploy → quality → monitor.

No frameworks. No containers. Just plain Python modules wired together by a
single orchestrator.

## Structure

```
contracts/          # Input/output data contracts (plain dataclasses)
stages/             # One function per pipeline stage
scripts/            # Utility scripts (empty placeholder)
orchestrator.py     # Runs all stages in sequence
.github/workflows/  # CI workflow that executes the orchestrator
```

## Usage

```bash
python orchestrator.py
```

## Rules

- No business logic yet — all stages return placeholder values
- No external dependencies
- Keep everything simple, modular, and Python-based
