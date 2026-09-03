# Contributing

Contributions are welcome — bug reports, documentation fixes and pull requests
alike. Small fixes can go straight to a pull request; for anything larger,
please open an [issue]({{ cookiecutter.project_repo }}/issues) first so the
approach can be agreed on before the work is done.

## Development environment

```bash
git clone {{ cookiecutter.project_repo }}
cd {{ cookiecutter.project_slug }}
uv venv --python {{ cookiecutter.python_version }}
uv pip install -e '.[dev,tests,typing{% if cookiecutter.project_profile == 'package' %},docs{% endif %}]'
pre-commit install
```

## Code style

[ruff](https://docs.astral.sh/ruff/) is both the linter and the formatter; its
configuration lives in `pyproject.toml`, and `.pre-commit-config.yaml` runs it
on every commit. Nothing else formats Python in this project.

```bash
ruff check --fix .
ruff format .
```

Configuring your editor to run ruff on save is the least painful way to work:
in VS Code or Cursor, add to `.vscode/settings.json`

```json
{
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll.ruff": "explicit",
        "source.organizeImports.ruff": "explicit"
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
}
```

The pre-commit hooks also run
[zizmor](https://docs.zizmor.sh/) over `.github/`, which audits the GitHub
Actions workflows for credential persistence, shell injection through
`${{ '{{' }} ... {{ '}}' }}` expansion and unpinned actions. Its configuration,
including which action publishers may be pinned to a tag rather than a commit
hash, is `.github/zizmor.yml`.

To check everything the CI checks before pushing:

```bash
pre-commit run --all-files
```

## Type checking

[mypy](https://mypy.readthedocs.io/) runs in `strict` mode over
`{{ cookiecutter.package_name }}/`; the settings are in `pyproject.toml`.

```bash
mypy
```

It is not a pre-commit hook, because a hook would run in its own environment
without this project's dependencies and report import errors that do not
exist. It runs in CI instead, in a job that installs the project first, so run
it locally in your development environment before pushing.

When a dependency ships no type information, mypy fails with `import-untyped`.
Exempt that one package with a `[[tool.mypy.overrides]]` block in
`pyproject.toml` — there is a commented-out example there — rather than
turning `ignore_missing_imports` on globally.

## Tests

The project uses [pytest](https://docs.pytest.org/), and is developed
test-first: write the failing test, then the code that makes it pass.

```bash
pytest
pytest --cov={{ cookiecutter.package_name }} --cov-report=term-missing
```

## Documentation

```bash
mkdocs serve      # live preview on http://127.0.0.1:8000
mkdocs build --strict
```

The API reference is generated from the docstrings by
[mkdocstrings](https://mkdocstrings.github.io/), so documenting a public
function is a matter of writing its Google-style docstring. `--strict` turns
warnings into errors and is what the CI runs; a build that is clean locally is
clean there too.

## Releases

Versions follow [semantic versioning](https://semver.org/). A release is cut by
bumping the version and pushing the tag:

```bash
bump2version patch   # or minor / major
git push --follow-tags
```

Publishing the GitHub release then triggers the `release` workflow, which
builds the distribution and uploads it to PyPI.
