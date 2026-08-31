# Python project template (Saez-Rodriguez Group)

## Description

This is a Cookiecutter template to create Python projects. It has been tailored by the [Saez-Rodriguez Group](https://saezlab.org/) at Universität Heidelberg.

This template provides tools to streamline setup and maintenance, letting you focus on your project instead of getting bogged down by technical details. It includes:

- Documentation
  - [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/): A sleek, responsive theme for MkDocs documentation sites.

- Code Quality/Automation
  - [Pre-commit hooks](https://pre-commit.com/): A framework for managing and running code quality hooks before commits.

- Release Management
  - [Bump2version](https://github.com/c4urself/bump2version):  A tool to automate version number management in your project.

- Testing
  - [Pytest](https://docs.pytest.org/en/stable/):  A powerful testing framework for writing and running Python tests.

- Continuous integration
  - [GitHub Actions](https://docs.github.com/en/actions) workflows for tests, linting, documentation and releases, described in [Continuous integration](#continuous-integration) below.


## Pre-requisites
> **Note:**   We strongly recommend you have the following pre-requisites before using this template.

| Pre-requisite                                                 | Description                                                                      |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | A high-performance tool for managing Python packages and virtual environments.   |
| [Cruft](https://cruft.github.io/cruft/#installation)          | A CLI tool to scaffold new projects using customizable templates.                |
| [GitHub CLI](https://github.com/cli/cli#installation)         | A command-lIne tool to interact with GitHub repositories, issues, and workflows. |

## How-to use this template?

In six easy steps you will have a ready to use Python project with batteries included.

**1.  Generate Your Project from the Template**

  Run the following command and follow the prompts in your terminal:
  ```bash
  cruft create https://github.com/saezlab/python-project.git --checkout master
  ```

**2. Navigate to Your New Project Directory**
```bash
cd <my-project> # replace with the name of your project
```

**3. Set Up and Activate a Virtual Environment using `uv`**
```bash
uv venv .venv
source .venv/bin/activate
```
> This creates and activates a lightweight virtual environment in `.venv`.

**4. Install Project Dependencies listed in the `pyproject.toml` file**

  Install all required and optional dependencies (development, testing, docs):
  ```bash
  uv pip install ".[dev,tests,docs]"
  ```

**5. Install and update pre-commit hooks**
```bash
git init
pre-commit install
pre-commit autoupdate
```

**6. Initialize Git and Push to GitHub**
```bash

git add .
git commit -m "Initial commit"
gh repo create <GitHub-organization>/<my-project>  --public --source=. --push
```

**7. Link to the template**
```bash
cruft link
https://github.com/saezlab/python-project
```

This links your project to the template so you can later do:

```bash
cruft update
```

---

🎉 Congratulations! Wishing you every success as you begin your project journey 🚀

Saez-Rodriguez Group Team!

## Continuous integration

The generated project comes with the following GitHub Actions workflows in
`.github/workflows`:

| Workflow | Trigger | What it does |
| --- | --- | --- |
| `test.yaml` | push and pull request on `main`/`master`, twice a month, manual | Runs the unit tests with coverage on Python 3.10–3.13, the ruff lint and format checks, and a strict mkdocs build. The `check` job at the end aggregates all of them. |
| `build.yaml` | push and pull request on `main`/`master` | Builds the sdist and the wheel with `uv build` and validates the distribution metadata with `twine check --strict`. |
| `docs.yaml` | push on `main`/`master`, manual | Publishes the mkdocs site to GitHub Pages with `mkdocs gh-deploy`. |
| `release.yaml` | GitHub release published | Builds and uploads the distribution to PyPI. |
| `security.yaml` | push and pull request on `main`/`master` | Runs `bandit`. Generated only when `include_security_workflow` is `yes`. |

All workflows declare a least-privilege `permissions` block and a
`concurrency` group, so that a new push cancels the superseded runs.

**Branch protection**: require the single `All checks passed` check from
`test.yaml` instead of the individual jobs. It is an
[`alls-green`](https://github.com/re-actors/alls-green#why) gate over the whole
matrix, so the protection rule does not have to be edited whenever a Python
version is added or removed.

**Releasing to PyPI**: `release.yaml` uses
[trusted publishing](https://docs.pypi.org/trusted-publishers/), so no API
token is stored in the repository. Register the repository and the `release`
workflow as a trusted publisher on PyPI, and create a GitHub environment named
`pypi` in the repository settings. Until that is done the workflow fails at the
upload step; everything else keeps working.

**Coverage**: `test.yaml` uploads the coverage report to Codecov over OIDC,
without a token. The upload is not allowed to fail the run, so a project that
is not registered with Codecov still gets a green build.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Python-project template has a [BSD3](https://opensource.org/license/bsd-3-clause) license, as found in the [LICENSE](./LICENSE) file.
