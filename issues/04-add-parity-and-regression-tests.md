# Add parity and regression tests

## Goal

Protect the migration with tests that catch output drift and broken builds.

## Scope

- Add validation tests for the radar schema.
- Add output checks for the generated site.
- Add a smoke test for the full build flow.
- Use golden files or snapshots where appropriate.

## Checklist

- [ ] Add schema validation tests
- [ ] Add generated output regression tests
- [ ] Add a build smoke test
- [ ] Capture the expected file layout in tests

## Acceptance

- The build fails when the generator output drifts unexpectedly.
- The project has a reliable automated check before publishing.
