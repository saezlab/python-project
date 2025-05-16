# Python project template

> **Note**
> This document is best viewed in its [rendered Sphinx version](https://saezlab.github.io/python-project/).

Create your new Python project by forking this repo. It sets up several helpful development tools for you:

* [Poetry build system](https://python-poetry.org/)
* [Tox testing](https://tox.wiki/en/latest/)
* [Pre-commit hooks](https://pre-commit.com/) for formatting and linting (Python, YAML, rST)
* [Pytest](https://docs.pytest.org/) for testing
* [Bump2version](https://github.com/c4urself/bump2version) for versioning
* [Sphinx documentation](https://www.sphinx-doc.org/en/master/)

This repo supports improved development practices. See [Efficient Development Guide](https://github.com/saezlab/HowTo/blob/master/HowTo_efficient_development.md), [tools spreadsheet](https://docs.google.com/spreadsheets/d/1by744ceMxt57egyq8Q4SZUfzLRhNG6BtlpoD3ljgp90/edit#gid=0), or the [Saezbook](https://saezbook.omnipathdb.org/Help/HowTo/efficient_development.html) for more info.

## Setup

This template uses [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) to create projects.

```bash
# Clone the template
git clone https://github.com/saezlab/python-project

# Edit metadata
$EDITOR python-project/cookiecutter.json

# Generate your project
cookiecutter python-project
```

Or use the shortcut:

```bash
cookiecutter gh:saezlab/python-project
```

## Manual setup

While cookiecutter automates this, here are the manual steps:

### Project name

Use `new_project` as a placeholder.

### Install tools

```bash
curl -sSL https://install.python-poetry.org | python3 -
pip install --user tox pre-commit
```

### Copy the template

```bash
git clone https://github.com/saezlab/python-project new_project
cd new_project
```

### Set remote origin

```bash
git remote set-url origin git@github.com:saezlab/new_project
```

### Rename placeholder names

```bash
find . -depth -type f ! -path '*/.git/*' -exec sed -i '' 's/project_name/new_project/g' {} +
git mv project_name new_project
git add -u
git commit -m 'set project name'
```

### Set author name and email

```bash
find . -depth -type f ! -path '*/.git/*' -exec sed -i '' 's/Denes Turei/Your Name/g' {} +
find . -depth -type f ! -path '*/.git/*' -exec sed -i '' 's/turei\.denes@gmail\.com/your@email/g' {} +
git add -u
git commit -m 'set author'
```

### Edit project metadata

Edit `pyproject.toml` fields: `description`, `repository`, and `bug_tracker`.

### License

If using MIT:

```bash
find . -depth -type f ! -path '*/.git/*' -exec sed -i '' 's/GPLv3/MIT/g' {} +
sed -i '' 's/GPL-3\.0-only/MIT/g' pyproject.toml
git add LICENSE
git add pyproject.toml
git commit -m 'set license to MIT'
```

### Initialize tools

```bash
poetry update
poetry install
tox
git add -u
git commit -m 'updated poetry lock'
```

Edit the README file. If using markdown, update the `readme` field in `pyproject.toml`.

### Set up pre-commit

```bash
pre-commit install
```

> **Note**
> If you fix pre-commit issues, remember to `git add` again.

> **Warning**
> Don't interrupt pre-commit if it stashes changes.

### Choose code formatter

Uncomment one formatter in `.pre-commit-config.yaml`. To run it manually:

```bash
pre-commit run yapf --hook-stage manual
```

Avoid enabling multiple formatters.

### Configure linter

Add ignore rules in `pyproject.toml` under `tool.flake8`. Use `# noqa:` in code for specific cases.

### Rewrite README

Delete this template content and write about your project.

### Sphinx Docs

Edit `docs/src/index.rst`. You may keep or replace the existing content.

## Usage

### Skip pre-commit hooks

```bash
git commit -nm 'commit message'
```

### Run tests

```bash
tox
# Or:
poetry run pytest -v
```

### Add dependency

```bash
# Edit pyproject.toml
poetry update
poetry install
git add -u
git commit -m 'new dependency: some-package'
```

### Build package

```bash
poetry build
```

To publish:

```bash
poetry config pypi-token.pypi my-token
poetry publish
```

### Build docs

```bash
poetry run make html --directory docs/
```

### Why use `poetry run`?

This runs code inside the project's virtual environment.

```bash
poetry run python
```

This ensures dependencies match what’s locked in `poetry.lock`.
