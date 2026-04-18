# Phase 00 Design: Foundation

## Goal

Create the engineering and repository foundation required to migrate the radar
generator from JavaScript to Python without losing the current publish contract.

## Non-Goals

- complete Python reimplementation of the radar generator
- visual redesign of the radar
- removal of the current JavaScript output

## Deliverables

- Python project scaffold with `uv`
- lint, test, and coverage configuration
- `pre-commit` baseline
- Definition of Done
- threat model
- ADR foundation
- phase design documentation

## Constraints

- preserve the existing `tech-radar/` publish path
- keep `tech-radar.json` as the source of truth
- target Python `3.14`
- favor deterministic static generation

## Parallelizable Task Breakdown

### Track A: Governance

- finalize Definition of Done
- create and maintain threat model
- record migration foundation ADR

### Track B: Toolchain

- create `pyproject.toml`
- configure `uv`, `ruff`, `pytest`, coverage, and `rumdl`
- set up `pre-commit` with local and pinned hooks
- add a thin `Makefile` for common repeated local workflows

### Track C: Repository Layout

- add `src/` package layout
- add baseline tests
- add docs site configuration

### Track D: Security

- define expected local scanning commands
- wire `pip-audit` and `gitleaks` into developer workflow
- reserve `grype` for artifact and release scanning
- encode Renovate soak and approval policy
- add StepSecurity Harden-Runner to CI in audit mode

## Risks

- Python `3.14` tool compatibility may lag.
- Hook execution cost may conflict with strict TCR loops if not staged correctly.
- Mutation testing needs careful scoping to stay practical.

## Exit Criteria

- project metadata exists
- docs structure exists
- baseline tests exist
- lint, coverage, and hook policies are encoded in-repo
- the team can proceed into schema validation and generator implementation without
  reopening foundational tool decisions
