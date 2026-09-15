# Repository Guide

## Project Shape

- This is a template repository, not a finished application. Runtime code currently consists only of `src/python_skeleton/__init__.py`.
- The installed command `python-skeleton` calls `python_skeleton:main`, as configured in `[project.scripts]` in `pyproject.toml`.
- When instantiating the template, update the distribution name, script entry point, and package directory together. Distribution names may use dashes; the import package uses underscores.

## Tooling

- Python 3.14 is required by both `.python-version` and `pyproject.toml`.
- Use `uv`; create/update the environment with `uv sync --all-groups`. Keep `uv.lock` committed and use `uv add` or `uv add --dev` rather than editing dependency lists alone.
- Run the current entry point with `uv run python-skeleton` and build distributions with `uv build`.

## Verification

- Lint: `uv run ruff check .`
- Format check: `uv run ruff format --check .`
- Typecheck: `uv run ty check`
- Tests: `uv run pytest`; focused test: `uv run pytest path/to/test_file.py::test_name`
- No tests are currently committed, so `uv run pytest` reports zero collected tests and exits with pytest's no-tests status. Do not present it as a passing suite until tests exist.
- There are no repository-specific Ruff, ty, pytest, or coverage settings and no CI workflows; these tools currently use their defaults.
