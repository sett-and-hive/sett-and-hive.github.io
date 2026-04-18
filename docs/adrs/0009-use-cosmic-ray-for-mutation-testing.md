# ADR 0009: Use Cosmic Ray for mutation testing

## Status

Accepted

## Context

We have a strict quality policy, including 100% branch coverage for Python code.
However, high coverage does not guarantee that tests are effective at catching
regressions or that the assertions are meaningful. Mutation testing provides a
way to verify the quality of the tests themselves by introducing small changes
(mutations) to the source code and ensuring that at least one test fails.

## Decision

We will use `cosmic-ray` for mutation testing of the Python radar toolchain.

Mutation testing will be part of the "Definition of Done" for any pull request
affecting Python source code.

## Consequences

- Developers must run `cosmic-ray` for their changes.
- Surviving mutants must be addressed by improving tests or explicitly
  justified if they represent unreachable or irrelevant code.
- Mutation testing can be slow, so it is recommended to run it on a scoped
  basis (e.g., against specific modules) during development.
- `cosmic-ray` configuration is maintained in `pyproject.toml`.
