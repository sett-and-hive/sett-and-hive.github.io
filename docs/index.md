# Engineering Docs

This repository is migrating the Sett and Hive technology radar build pipeline
from a third-party JavaScript generator to a Python-first static site toolchain.

The governing documents live here:

- [Definition of Done](definition-of-done.md)
- [Threat Model](threat-model.md)
- [ADR 0001: Python migration foundation](adrs/0001-python-radar-migration-foundation.md)
- [ADR 0002: Dependency update and runner security](adrs/0002-dependency-update-and-runner-hardening.md)
- [ADR 0003: Renovate dependency governance](adrs/0003-renovate-dependency-governance.md)
- [ADR 0004: Pre-commit enforcement](adrs/0004-pre-commit-enforcement.md)
- [ADR 0005: Harden-Runner rollout](adrs/0005-harden-runner-rollout.md)
- [ADR 0006: Thin Makefile command surface](adrs/0006-thin-makefile-command-surface.md)
- [ADR 0007: Use prek as the hook runner](adrs/0007-use-prek-as-hook-runner.md)
- [ADR 0008: Use Astral ty for type checking](adrs/0008-use-astral-ty-for-type-checking.md)
- [Phase 00 design](designs/phase-00-foundation.md)

The current delivery strategy is:

- preserve the published `tech-radar/` path during the migration
- build the replacement with Python, `uv`, `ruff`, `ty`, `pytest`, and `prek`
- document every significant architectural decision in an ADR
- design each phase before implementation and decompose it into parallelizable work
