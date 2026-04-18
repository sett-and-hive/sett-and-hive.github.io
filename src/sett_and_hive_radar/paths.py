"""Shared repository paths used by the Python radar toolchain."""

from pathlib import Path


def project_root() -> Path:
    """Return the repository root from the installed package location."""
    return Path(__file__).resolve().parents[2]
