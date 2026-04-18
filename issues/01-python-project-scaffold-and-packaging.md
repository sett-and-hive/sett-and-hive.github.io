# Add Python project scaffold and packaging

## Goal

Create the Python foundation for the migration.

## Scope

- Add `pyproject.toml`.
- Choose a modern dependency and task manager such as `uv` or `poetry`.
- Add a CLI entry point for the build.
- Add formatting, linting, and test tooling.

## Checklist

- [ ] Add Python packaging metadata
- [ ] Add a build CLI entry point
- [ ] Add lint and format configuration
- [ ] Add a test runner setup
- [ ] Document the new local build commands

## Acceptance

- Running the Python build entry point works without Node or Yarn.
- The project structure is ready for the rest of the migration.
