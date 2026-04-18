# ADR 0006: Thin Makefile Command Surface

## Status

Accepted

## Context

The repository now has several frequently repeated commands for local work:

- lock and sync the development environment
- run tests
- run lint and formatting
- build documentation
- run local verification suites

Those commands are already owned by `uv`, `pytest`, `ruff`, `rumdl`,
`pre-commit`, and `mkdocs`. A `Makefile` can improve ergonomics for both humans
and agents, but it becomes harmful if it turns into a second build system with
its own logic and hidden state.

## Decision

The repository will use a deliberately thin `Makefile` as an ergonomic command
surface only.

The `Makefile` will:

- expose short targets for common repeated workflows
- delegate directly to the canonical underlying commands
- avoid owning dependency resolution logic beyond calling `uv`
- avoid hiding side effects or introducing separate state

The `Makefile` will not become the source of truth for build behavior. The
source of truth remains the underlying commands, configuration, and tests.

## Consequences

### Positive

- Gives humans and agents a stable command vocabulary.
- Reduces repetition for common local tasks.
- Keeps the developer experience simple without changing the architecture.

### Negative

- Adds another file that must stay aligned with the canonical commands.
- Can drift into a second build system if not actively constrained.
