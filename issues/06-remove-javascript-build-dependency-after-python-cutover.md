# Remove JavaScript build dependency after Python cutover

## Goal

Clean up the old JS build chain once the Python generator is stable.

## Scope

- Remove `package.json` and Yarn-based build commands when no longer needed.
- Delete any obsolete generator-specific dependencies.
- Keep the repo lean and focused on the Python path.

## Checklist

- [ ] Confirm the Python build fully replaces the JS build
- [ ] Remove the JS build dependency
- [ ] Remove obsolete build scripts and references
- [ ] Verify the repo still publishes correctly

## Acceptance

- The repo no longer depends on JavaScript tooling for radar generation.
- The Python workflow is the only supported build path.
