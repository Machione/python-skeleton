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

## Releasing

- Releases are automated with release-please. Config is in
  `release-please-config.json`; the last released version is recorded in
  `.release-please-manifest.json`.
- Commits must follow Conventional Commits. Squash merging uses the PR title,
  which the `Lint PR` workflow enforces. Only `feat:` (minor) and `fix:`
  (patch) trigger a release; a `!` suffix triggers a major bump. `docs:`,
  `ci:`, `chore:` and similar prefixes never release.
- On each push to `main`, the Release workflow opens or updates a release PR
  and enables auto-merge on it. Once checks pass it merges; release-please
  then tags `vX.Y.Z`, creates the GitHub release, and the `build_release` job
  attaches the `dist/` artifacts. The version comes from `pyproject.toml` in
  the release commit — never bump it by hand. To force a version, put
  `Release-As: x.y.z` in a commit body on `main`.
- `uv.lock` is bumped in the release PR via an `extra-files` workaround
  (googleapis/release-please#2561); its `jsonpath` references the package
  name, so update it together with `project.name` when instantiating the
  template.
- The workflow authenticates with a GitHub App: Actions variable
  `RELEASE_APP_CLIENT_ID` and secret `RELEASE_APP_PRIVATE_KEY`. Plain
  `GITHUB_TOKEN` cannot be used because its PRs do not trigger CI.

## Verification

- Lint: `uv run ruff check .`
- Format check: `uv run ruff format --check .`
- Typecheck: `uv run ty check`
- Tests: `uv run pytest`; focused test: `uv run pytest path/to/test_file.py::test_name`
- There are no repository-specific Ruff, ty, pytest, or coverage settings;
  these tools currently use their defaults.
