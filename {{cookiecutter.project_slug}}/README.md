{% if cookiecutter.project_profile == 'package' -%}
![project-banner](./docs/assets/project-banner-readme.png)

{% endif -%}
# {{ cookiecutter.project_name }}

{% if cookiecutter.project_profile != 'tiny' -%}
[![Tests](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}/test.yaml?branch=main&label=tests)](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yaml)
[![Codecov](https://img.shields.io/codecov/c/github/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }})](https://codecov.io/gh/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }})
{% if cookiecutter.project_profile == 'package' -%}
[![Docs](https://img.shields.io/badge/docs-MkDocs-blue)](https://{{ cookiecutter.github_organization }}.github.io/{{ cookiecutter.project_slug }}/)
{% endif -%}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }})](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
{% endif -%}
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![License](https://img.shields.io/badge/license-{{ cookiecutter._license[cookiecutter.license].license_short|replace('-', '--') }}-blue)

## Description

{{ cookiecutter.readme }}

- [ ] TODO: replace this with a paragraph that says what the project does and who it is for.

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

- [ ] TODO: keep this only once the project is on PyPI; until then point at the repository.

## Usage

- [ ] TODO: Add usage instructions for your project.

```python
import {{ cookiecutter.package_name }}

print({{ cookiecutter.package_name }}.__version__)
```
{% if cookiecutter.project_profile == 'package' %}
## Documentation

The full documentation is at
<https://{{ cookiecutter.github_organization }}.github.io/{{ cookiecutter.project_slug }}/>.
It is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
from the `docs/` directory:

```bash
mkdocs serve
```
{% elif cookiecutter.project_profile == 'workflow' %}
## Documentation

See [docs/quickstart.md](docs/quickstart.md).
{% endif %}
## Development

```bash
uv venv --python {{ cookiecutter.python_version }}
uv pip install -e '.[dev,tests{% if cookiecutter.project_profile == 'package' %},docs{% endif %}]'
pre-commit install
```

[ruff](https://docs.astral.sh/ruff/) is the only linter and formatter; it runs
on every commit through pre-commit. Tests are run with
[pytest](https://docs.pytest.org/):

```bash
pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an
[issue]({{ cookiecutter.project_repo }}/issues) first to discuss what you would
like to change.{% if cookiecutter.project_profile == 'package' %} The contribution guide is at
[docs/contributing.md](docs/contributing.md).{% endif %}

Please make sure to update tests as appropriate.

## License

{{ cookiecutter.license }} — see the [LICENSE](./LICENSE) file.
