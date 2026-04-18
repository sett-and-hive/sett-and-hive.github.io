# ADR 0003: Renovate Dependency Governance

## Status

Accepted

## Context

This repository needs automated dependency maintenance, but recent software
supply chain attacks make naive "update immediately" automation unacceptable.
We want dependency updates to flow without turning pull requests into noise or
blindly trusting fresh upstream releases.

## Decision

Renovate is the dependency update system of record for this repository.

The repository will use the following Renovate policy:

- routine dependency updates soak for fourteen days
- security remediation bypasses the soak period and is raised immediately
- patch updates are bundled to reduce noise
- minor updates are bundled to reduce noise
- major updates require explicit approval
- dependencies with serious incidents in the preceding year require explicit approval

## Consequences

### Positive

- Reduces exposure to newly published malicious or unstable releases.
- Keeps routine maintenance noise under control.
- Makes review friction explicit where risk is highest.

### Negative

- Slows normal dependency adoption by design.
- Requires curating the high-risk dependency approval list over time.
