# Definition of Done

This is the governing Definition of Done for the repository. It is intentionally
strict. It must be updated as the repository's
engineering contract evolves, and the repository must follow the current version
of this document rather than a remembered summary of it.

## Purpose

The repository is only done when it is:

- releasable
- secure enough for its context
- understandable by a new maintainer
- reproducible
- covered by tests and contracts that would catch regressions

## Governing Rules

- Every significant architectural decision is recorded in an ADR as we go.
- Every phase starts with a design document in `docs/designs/`.
- The threat model is updated whenever assets, trust boundaries, or attack
  surfaces change.
- TCR is the working discipline: test, then commit or revert, then refactor.
- Python is written idiomatically and optimized for clarity.
- The repository remains a static site with no accidental backend dependency.
- `tech-radar.json` remains the source of truth until an ADR changes that rule.

## Done Checklist

Work is not done until every applicable item below is true.

### Scope and Design

- Acceptance criteria are explicit and satisfied.
- The relevant design document exists and reflects the current plan.
- Parallelizable tasks are identified in the design document before implementation.
- Any meaningful technical tradeoff or permanent architecture choice has an ADR.

### Code and Structure

- Code is minimal, coherent, and readable without hidden conventions.
- New files, modules, and commands fit the repository structure cleanly.
- Dead code, temporary compatibility shims, and stale comments are removed or justified.

### Tests and Verification

- Unit tests are written first or immediately to support TCR.
- Unit tests for touched Python modules achieve `100%` branch coverage.
- Contract tests cover the compatibility surface for generated artifacts and
  published behavior.
- Regression checks exist for file layout, page paths, and critical rendered output.
- Mutation testing is run with `cosmic-ray` for the PR scope, and surviving
  mutants are either fixed or explicitly justified.
- Local verification is green using the locked environment.

### Static Analysis and Formatting

- `ruff` passes.
- `ty` passes.
- Markdown formatting and linting pass with `rumdl`.
- `prek` passes locally with no skipped required hooks.
- The committed configuration itself is valid, including `prek`,
  `mkdocs`, and dependency-management files.
- Any `Makefile` targets remain a thin ergonomic layer over canonical commands,
  not a second build system.

### Security and Supply Chain

- Threat modeling is current for the change.
- `pip-audit` passes.
- `gitleaks` passes.
- `grype` is run when the change affects distributable artifacts, container-like
  surfaces, SBOM-relevant outputs, or otherwise increases artifact risk.
- Dependencies are reproducible and reviewable.
- Git-based integrations are pinned to commit SHAs.
- Index-based Python dependencies are locked in `uv.lock`.
- New dependencies are justified and removable.

### Dependency Governance

- Renovate is the dependency update system of record.
- Routine dependency updates soak for fourteen days.
- Security remediation is raised immediately and does not wait for the soak period.
- Patch updates are bundled to reduce noise.
- Minor updates are bundled to reduce noise.
- Major updates require explicit approval.
- Dependencies with serious incidents in the preceding year require explicit approval.
- Any change to this dependency-governance policy is captured in an ADR.

### CI/CD and Runner Security

- GitHub Actions workflows pin actions by commit SHA.
- Every workflow job starts with StepSecurity Harden-Runner.
- New or changed workflows start in Harden-Runner `audit` mode.
- After ten clean observed runs, the workflow is moved to egress blocking mode.
- Required runner permissions are minimal and explicit.

### Documentation

- `docs/definition-of-done.md` reflects actual practice and is maintained as the
  project evolves.
- ADRs reflect the architecture that is actually being built.
- The threat model reflects the current system.
- Build, test, publish, and operator instructions are current.
- Any security-sensitive or operationally subtle behavior is documented where a
  future maintainer would look first.

### Static Site Delivery

- The published radar remains available under `tech-radar/` unless an ADR changes it.
- Generated output is deterministic enough for regression testing.
- The site can be served as static content without extra runtime services.
- Asset paths, HTML structure, and critical interactions have stable contracts.

## Maintenance Rule

This document is not a one-time artifact. It must be updated as new obligations
become part of the repository's engineering contract.

## Failure Rule

If any applicable requirement in this document is unmet, the work is not done.
