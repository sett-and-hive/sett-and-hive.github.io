# Contributing to Sett and Hive Radar

This project is migrating to a Python-based toolchain using `uv`, `ruff`, `ty`, and `pytest`.

## Local Development Setup

### Prerequisites

- **Python 3.14**: This project requires Python 3.14.
- **uv**: We use [uv](https://github.com/astral-sh/uv) for dependency management.
- **prek**: Install `prek` locally to run pre-commit hooks.
- **gitleaks**: Install `gitleaks` locally for secret scanning.

### Getting Started

1. **Clone the repository**:

    ```bash
    git clone https://github.com/sett-and-hive/sett-and-hive.github.io.git
    cd sett-and-hive.github.io
    ```

2. **Sync the environment**:

    ```bash
    make sync
    ```

3. **Install pre-commit hooks**:
    We use `prek` as our hook runner. Ensure it is installed and configured:

    ```bash
    uv run --locked prek install
    ```

## Important Make Targets

Use `make` to run common development tasks:

- `make sync`: Sync the locked development environment and install dependencies.
- `make fmt`: Format Python and Markdown content.
- `make lint`: Run Ruff checks for Python linting.
- `make typecheck`: Run `ty` for type checking.
- `make test`: Run `pytest` with coverage requirements.
- `make mutation-test`: Run mutation testing with `cosmic-ray`.
- `make prek`: Run all configured pre-commit and pre-push hooks over all files.
- `make check`: Run the full verification suite (lint, typecheck, tests, docs, audit).
- `make serve-docs`: Serve the documentation site locally.

## Development Workflow

1. **Run hooks often**: Before pushing, ensure all hooks pass by running `make prek`.
2. **Verify changes**: Run `make check` to ensure your changes meet the project's quality standards.
3. **Type Safety**: We use `ty` for type checking. Ensure all new code is properly typed.
4. **Testing**: All new features and bug fixes must be accompanied by tests. We aim for 100% coverage.
5. **Mutation Testing**: We use `cosmic-ray` for mutation testing. Per the
   [Definition of Done](docs/definition-of-done.md) and
   [ADR 0009](docs/adrs/0009-use-cosmic-ray-for-mutation-testing.md), you must run mutation testing
   for your changes and ensure no mutants survive without justification.

    ```bash
    make mutation-test
    ```
