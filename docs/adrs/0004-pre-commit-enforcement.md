# ADR 0004: Pre-commit-Style Hook Enforcement

## Status

Accepted

## Context

The repository uses TCR, strict quality gates, and multiple static checks. The
fastest way to keep those checks close to the point of change is to enforce them
through a pre-commit-style hook runner and a shared repository configuration.

## Decision

The repository will use a pre-commit-style enforcement layer for repository
hygiene and developer workflow checks.

The repository will:

- use the common baseline hooks for text, file, YAML, JSON, TOML, merge, and key safety
- use `ruff` for Python linting and formatting
- use `rumdl` for Markdown formatting
- validate the hook-runner configuration itself
- keep heavier checks such as `pytest`, `pip-audit`, and `gitleaks` at
  `pre-push` or manual stages where appropriate

The specific runner implementation may evolve and is captured in later ADRs.

## Consequences

### Positive

- Catches common quality failures before they reach CI.
- Keeps repository conventions consistent across contributors.
- Supports TCR by shortening the feedback loop.

### Negative

- Adds local workflow overhead.
- Requires ongoing maintenance of hook pinning and compatibility.
