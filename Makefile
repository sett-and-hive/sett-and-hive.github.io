.PHONY: help lock sync fmt lint markdown-lint typecheck test docs serve-docs audit prek check

help:
	@printf '%s\n' \
		'Available targets:' \
		'  make lock        Refresh uv.lock' \
		'  make sync        Sync the locked development environment' \
		'  make fmt         Format Python and Markdown content' \
		'  make lint        Run Ruff checks' \
		'  make markdown-lint Run Markdown lint checks with rumdl' \
		'  make typecheck   Run ty type checking' \
		'  make test        Run pytest with coverage gates' \
		'  make mutation-test Run mutation testing with cosmic-ray' \
		'  make docs        Build the docs site in strict mode' \
		'  make serve-docs  Serve the docs site locally' \
		'  make audit       Run pip-audit against the locked environment' \
		'  make prek        Run all configured prek hooks over all files' \
		'  make check       Run the standard local verification suite'

lock:
	uv lock

sync:
	uv sync --locked --group dev

fmt:
	uv run --locked ruff format .
	uv run --locked rumdl fmt docs README.md BUILD-RADAR.md issues

lint:
	uv run --locked ruff check .

markdown-lint:
	uv run --locked rumdl check docs README.md BUILD-RADAR.md issues

typecheck:
	uv run --locked ty check

test:
	uv run --locked pytest

mutation-test:
	uv run --locked python scripts/mutation_test.py --base origin/main

docs:
	uv run --locked mkdocs build --strict

serve-docs:
	uv run --locked mkdocs serve

audit:
	uv run --locked pip-audit

prek:
	uv run --locked prek run --all-files --show-diff-on-failure
	uv run --locked prek run --all-files --show-diff-on-failure --hook-stage pre-push

check:
	uv run --locked ruff check .
	uv run --locked ty check
	uv run --locked pytest
	uv run --locked rumdl check docs README.md BUILD-RADAR.md issues
	uv run --locked mkdocs build --strict
	uv run --locked pip-audit
