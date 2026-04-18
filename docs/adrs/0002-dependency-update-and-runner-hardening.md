# ADR 0002: Dependency Update and Runner Hardening Policy

## Status

Accepted

## Context

The repository is moving onto a Python-first toolchain at a time when software
supply chain attacks against packages, actions, and CI runners are common and
well-documented.

Routine dependency updates still need to flow, but they should do so with
deliberate friction:

- new releases need time to soak
- security fixes need to bypass that soak
- breaking changes need explicit review
- CI runners need runtime egress controls and tamper monitoring

## Decision

We will adopt the following repository-wide policy:

- Renovate is the dependency update system of record.
- Routine dependency updates soak for fourteen days via Renovate minimum release age.
- Security-driven updates bypass the soak period and are raised immediately.
- Patch updates are bundled together to reduce PR noise.
- Minor updates are bundled together to reduce PR noise.
- Major updates always require explicit approval.
- Dependencies with serious incidents in the preceding year require explicit approval.
- GitHub Actions workflows pin actions by commit SHA.
- Every GitHub Actions job starts with StepSecurity Harden-Runner.
- New workflows begin with Harden-Runner in `audit` mode for ten observed clean
  runs before switching to egress blocking mode.

## Consequences

### Positive

- Reduces exposure to fresh malicious releases.
- Makes security exception paths explicit.
- Treats the CI runner as a sensitive execution environment rather than a blind spot.

### Negative

- Dependency updates arrive more slowly by default.
- Maintaining the high-risk dependency approval list is an ongoing governance task.
- Audit-to-block rollout requires operational discipline.
