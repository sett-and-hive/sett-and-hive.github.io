# Threat Model

## Scope

This document covers the migration from a JavaScript-based generated radar site
to a Python-generated static site published through GitHub Pages.

## Security Objectives

- Preserve the integrity of published radar content.
- Prevent supply chain compromise in the local build and publish flow.
- Prevent accidental disclosure of secrets in the repository history.
- Keep the generated static site free of avoidable injection risks.
- Make regressions in security posture visible before merge.

## Assets

- `tech-radar.json` content
- generated `tech-radar/` site artifacts
- build configuration, lockfiles, and hook configuration
- ADRs, design docs, and repository workflow documentation
- Git history and release provenance

## Actors

- maintainers working locally
- GitHub Pages and repository automation
- end users viewing the published static site
- dependency publishers and transitive tool authors
- attackers attempting repo compromise, content tampering, or secret exfiltration

## Trust Boundaries

- maintainer workstation to repository
- repository to GitHub Pages publication
- local dependency resolution to external package indexes
- generated static HTML/JS to the end-user browser

## Primary Threats

### Supply chain compromise

- Malicious or compromised build dependencies.
- Dependency drift that silently changes generated output.
- Unreviewed tool upgrades.

Mitigations:

- `uv.lock` committed and reviewed.
- `pip-audit` required.
- Renovate applies a fourteen-day minimum release age to routine updates.
- Security updates bypass the soak period and are raised immediately.
- Major and high-risk dependency updates require explicit approval.
- SHAs for git-based hooks and automation references.
- ADR review for meaningful toolchain changes.

### Secret leakage

- Tokens committed to the repository.
- Secrets embedded into generated site artifacts.

Mitigations:

- `gitleaks` in the local and CI workflow.
- no secrets in static-site configuration
- review generated artifacts as publishable public content

### Content tampering or invalid output

- Invalid `tech-radar.json` data.
- Unsafe HTML in blip descriptions.
- Accidental drift between source data and published output.

Mitigations:

- typed validation for source content
- contract tests for rendered output
- regression tests for expected file layout and key page contracts

### Dependency and artifact vulnerability exposure

- Vulnerable Python packages.
- Vulnerable bundled assets or generated artifacts.

Mitigations:

- `pip-audit` for Python dependencies
- `grype` when distributable artifacts or SBOM-oriented review is warranted
- StepSecurity Harden-Runner on GitHub Actions jobs, starting in audit mode and
  moving to egress blocking after ten observed clean runs

## Static Site Abuse Cases

- inject unsafe markup into `tech-radar.json`
- ship stale generated assets that no longer match reviewed content
- break content security expectations with unnecessary runtime dependencies

## Required Controls

- typed schema validation
- output contract tests
- reproducible lockfile
- secret scanning
- vulnerability scanning
- ADR and design review for architecture changes

## Residual Risk

- The site is intentionally public and static, so content integrity is more
  important than confidentiality.
- Third-party ecosystem risk cannot be eliminated; it must be constrained,
  documented, and continuously scanned.

## Review Cadence

- Update this document at the start and end of each major phase.
- Update immediately when assets, trust boundaries, or publication flow change.
