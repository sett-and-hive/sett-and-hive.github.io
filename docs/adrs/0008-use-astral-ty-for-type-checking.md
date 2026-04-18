# ADR 0008: Use Astral ty for Type Checking

## Status

Accepted

## Context

The repository needs a fast, modern type checker that fits the Astral-oriented
toolchain already in use for `uv` and `ruff`.

According to the current official Astral documentation, `ty` is Astral's type
checker and language server, with project configuration in `pyproject.toml`
under `[tool.ty]` and a standard `ty check` command for project checking.

## Decision

The repository standardizes on Astral `ty` for Python type checking.

The repository will:

- configure `ty` in `pyproject.toml`
- run `ty check` as part of local verification
- expose type checking via the Makefile
- run `ty` in CI and through the hook runner for appropriate stages

## Consequences

### Positive

- Keeps the Python quality toolchain aligned around Astral tools.
- Adds fast type checking to the repository's standard verification flow.
- Reduces friction for both local development and CI execution.

### Negative

- Adds another still-evolving tool to the repository contract.
- Type-checking behavior and configuration practices may change as `ty` matures.
