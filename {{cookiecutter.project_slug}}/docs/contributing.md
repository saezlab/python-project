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
uv pip install -e '.[dev,tests{% if cookiecutter.project_profile == 'package' %},docs{% endif %}]'
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

To check everything the CI checks before pushing:

```bash
pre-commit run --all-files
```

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
