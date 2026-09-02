# Installation

## From PyPI

```bash
pip install {{ cookiecutter.project_slug }}
```

## From source

```bash
git clone {{ cookiecutter.project_repo }}
cd {{ cookiecutter.project_slug }}
pip install -e .
```

## For development

The project is developed with [uv](https://docs.astral.sh/uv/). To get an
environment with the test, documentation and development dependencies:

```bash
uv venv --python {{ cookiecutter.python_version }}
uv pip install -e '.[dev,tests{% if cookiecutter.project_profile == 'package' %},docs{% endif %}]'
pre-commit install
```

## Requirements

{{ cookiecutter.project_name }} requires Python {{ cookiecutter.python_version }} or newer.
