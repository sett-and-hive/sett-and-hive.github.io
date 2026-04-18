# ADR 0007: Use prek as the Hook Runner

## Status

Accepted

## Context

The repository uses a `.pre-commit-config.yaml`-style hook configuration, but
the desired local and CI runner is `prek` rather than upstream `pre-commit`.

According to the current official `prek` documentation, `prek` is designed as a
drop-in runner for existing pre-commit YAML configurations and supports the
commands this repository needs, including `prek run --all-files` and
`prek validate-config`.

## Decision

The repository standardizes on `prek` as the hook runner.

The repository will:

- keep `.pre-commit-config.yaml` as the configuration format
- replace command invocations of `pre-commit` with `prek`
- provide a `make prek` target that runs hooks over all files
- validate the hook configuration with `prek validate-config`

## Consequences

### Positive

- Preserves the familiar config format while using the preferred runner.
- Improves local and CI ergonomics with a faster Rust-native tool.
- Keeps migration cost low because the config format does not need to change.

### Negative

- Depends on a younger tool with evolving feature parity.
- Some ecosystem guidance still assumes upstream `pre-commit` command names.
