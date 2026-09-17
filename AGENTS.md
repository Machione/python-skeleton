# Repository Guide

## Project Shape

- This is a template repository, not a finished application. Runtime functions
  are in `src/python_skeleton/main.py`; `src/python_skeleton/__init__.py` is empty.
- The installed command is configured as `python_skeleton:main`, but the callable
  currently lives at `python_skeleton.main:main`; align the entry point
  or re-export it before relying on the command.
- When instantiating the template, update the distribution name, script
  entry point, and package directory together. Distribution names may use
  dashes; the import package uses underscores.

## Tooling

- Python 3.14 is required by both `.python-version` and `pyproject.toml`.
- Use `uv`; create/update the environment with `uv sync --all-groups`.
  Keep `uv.lock` committed and use `uv add` or `uv add --dev` rather
  than editing dependency lists alone.
- Build distributions with `uv build`.

## Documentation

- Documentation uses ProperDocs with Shadcn, Mkdocstrings, and MkDocs AutoAPI. Preview
  with `uv run properdocs serve`; perform a finite verification build with `uv run
  properdocs build`.
- Keep `autoapi_dir: src` aligned with Mkdocstrings' `paths: [src]` in `properdocs.yml`.
- `shadcn_autoapi.py` is a compatibility hook for Shadcn 0.12.1: it skips Git
  timestamps only for AutoAPI-generated temporary pages. Remove it only
  after Shadcn handles MkDocs' `File.generated_by` marker upstream.

## Verification

- Lint: `uv run ruff check .`
- Format check: `uv run ruff format --check .`
- Typecheck: `uv run ty check`
- Tests: `uv run pytest`; focused test: `uv run pytest path/to/test_file.py::test_name`
- There are no repository-specific Ruff, ty, pytest, or coverage settings;
  these tools currently use their defaults.
