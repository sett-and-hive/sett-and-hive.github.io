# Migrate tech-radar build pipeline from JavaScript to Python

## Goal

Replace the current JavaScript-based radar generation flow with a modern Python
implementation while keeping the published GitHub Pages output stable.

## Scope

- Keep `tech-radar.json` as the source of truth.
- Replace `package.json` and Yarn-based build steps with a Python CLI.
- Preserve the generated static site layout so GitHub Pages continues to work.
- Add validation and tests before removing the old JS path.

## Checklist

- [ ] Define the target Python toolchain and repo structure
- [ ] Add schema validation for `tech-radar.json`
- [ ] Reimplement static site generation in Python
- [ ] Preserve output parity with the current radar site
- [ ] Add build and validation tests
- [ ] Update documentation and GitHub Pages instructions
- [ ] Remove unused JavaScript build dependency and cleanup

## Child issues

- [Python project scaffold](./01-python-project-scaffold-and-packaging.md)
- [Radar schema validation](./02-validate-tech-radar-json-with-typed-models.md)
- [Python site generation](./03-implement-python-radar-site-generation.md)
- [Parity and regression tests](./04-add-parity-and-regression-tests.md)
- [Docs and workflow update](./05-update-build-docs-and-repository-workflow.md)
- [Remove JS build dependency](./06-remove-javascript-build-dependency-after-python-cutover.md)

## Done when

- The repo builds the radar site with Python only.
- The published output remains compatible with the existing GitHub Pages path.
- The build is covered by validation and regression tests.
