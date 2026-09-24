# python-skeleton

Template repository for new Python projects.

## Features

TODO: Add stuff here!

## Getting started

### Creating a copy

When creating a new repository on GitHub, select `python-skeleton` as the
template to follow.

Once you have created your own repository based off this template, then edit
the `name`, `description` and `[project.scripts]` part of
[pyproject.toml](./pyproject.toml) and rename the folder
[src/python_skeleton](./src//python_skeleton), to match the name and
description of the repository you have created. Note that the `name` in
[pyproject.toml](./pyproject.toml) can contain dashes (`-`), and your
repository name can match that, but the folder
[src/python_skeleton](./src//python_skeleton) translates dashes to underscores
(`_`). You should follow that example.

Over time, you will want to replace this README with your own.

### Virtual environment

Use [`uv`](https://docs.astral.sh/uv/). Make sure that it is installed.

This project will have minimal dependencies installed by default, so you can
add more as you are developing your code using `uv add something`. If you want
to add dependencies that are required for development but not for the use of
the package, add them to the dev group with `uv add --dev something`.

To create a virtual environment to start working on this project use
`uv sync --all-groups`.

### Repository settings

#### General

Features:

- Turn off Wikis
- Turn on Sponsorships
- Turn off Projects

Pull Requests:

- Turn off "Allow merge commits"
- Turn off "Allow rebase merging"
- Turn on "Always suggest updating pull request branches"
- Turn on "Allow auto-merge"
- Turn on "Automatically delete head branches"

#### Rulesets

Create a new branch ruleset. Give it a name like "Protect main". Include the
default branch as a target. Set the enforcement status to "Active".

Branch rules:

- Turn on "Require linear history"
- Turn on "Require a pull request before merging"
  - Turn on "Dismiss stale pull request approvals when new commits are pushed"
  - Turn on "Require conversation resolution before merging"
  - Change allowed merge methods to "Squash" only
- Turn on "Require status checks to pass" FIXME: need to define the checks here!!
- Turn on "Require code scanning results"
- Turn on "Require code quality results"
- Turn on "Restrict code coverage"
  - Set "Minimum line coverage percentage" to 100
  - Set "Maximum line coverage drop" to 0

#### Release automation

Releases are automated with
[release-please](https://github.com/googleapis/release-please). Pull request
titles must follow [Conventional Commits](https://www.conventionalcommits.org)
because they become the squash-merge commit message: `feat:` triggers a minor
release, `fix:` a patch release, and a `!` suffix a major release. Prefixes
such as `docs:`, `ci:` and `chore:` never trigger a release. Release PRs merge
automatically once checks pass, after which the tag, GitHub release, and built
distributions are published automatically. Define the ruleset's required
status checks so that auto-merged release PRs wait for CI.

One-time setup:

1. Create a GitHub App (Settings > Developer settings > GitHub Apps) with
   repository permissions Contents (read/write), Pull requests (read/write),
   and Issues (read/write). Disable the app's webhook.
2. Install the app on this repository.
3. Add an Actions variable `RELEASE_APP_CLIENT_ID` containing the app's Client
   ID, and an Actions secret `RELEASE_APP_PRIVATE_KEY` containing its private
   key.

### Recommended VS Code extensions

- `tamasfe.even-better-toml`
TODO: Add stuff here! E.g. RUFF, ty, etc.
