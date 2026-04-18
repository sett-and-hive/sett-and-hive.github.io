# ADR 0005: Harden-Runner Rollout

## Status

Accepted

## Context

GitHub Actions runners are a sensitive supply chain execution environment.
Because this repository intends to pin actions by commit SHA and treat CI as a
security boundary, runtime egress monitoring and control need to be part of the
default workflow design.

## Decision

Every GitHub Actions job in this repository starts with StepSecurity
Harden-Runner.

The rollout policy is:

- pin the Harden-Runner action by commit SHA
- begin each new or materially changed workflow in `audit` mode
- observe ten clean runs
- switch the workflow to egress blocking mode after those ten clean runs
- use the stronger container-aware sudo hardening option where supported

## Consequences

### Positive

- Treats CI runners as a defended runtime, not just an execution convenience.
- Creates an operational path from observation to enforcement.
- Reduces the blast radius of compromised actions and dependency execution.

### Negative

- Requires deliberate rollout management.
- Can block legitimate network calls if the transition to blocking mode is rushed.
