# Python project template (Saez-Rodriguez Group)

## Description

This is a Cookiecutter template to create Python projects. It has been tailored by the [Saez-Rodriguez Group](https://saezlab.org/) at Universität Heidelberg.

This template provides tools to streamline setup and maintenance, letting you focus on your project instead of getting bogged down by technical details. It includes:

- Documentation
  - [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/): A sleek, responsive theme for MkDocs documentation sites.

- Code Quality/Automation
  - [Ruff](https://docs.astral.sh/ruff/): The single linter and formatter, run on every commit through [pre-commit](https://pre-commit.com/) and kept up to date by [pre-commit.ci](https://pre-commit.ci/).
  - [mypy](https://mypy.readthedocs.io/): Static type checking, configured strictly and run as its own CI job.
  - [zizmor](https://docs.zizmor.sh/): Static analysis of the GitHub Actions workflows themselves, run both as a pre-commit hook and in CI.

- Release Management
  - [Bump2version](https://github.com/c4urself/bump2version):  A tool to automate version number management in your project.
  - [Cruft](https://cruft.github.io/cruft/): Keeps the project in sync with this template; the generated `template-update.yaml` workflow opens the update pull requests for you.

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

  The first structural question is `project_profile`, which decides how much
  scaffolding you get — see [Project profiles](#project-profiles) below.

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
  uv pip install ".[dev,tests,docs]"   # drop `docs` outside the `package` profile
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

## Project profiles

`project_profile` decides how much scaffolding is generated. Everything a
profile does not include is simply absent — there is nothing to delete
afterwards.

| | `package` (default) | `workflow` | `tiny` |
| --- | --- | --- | --- |
| Intended for | a distributed library | an analysis or pipeline repository | a scratch or single-purpose repository |
| `pyproject.toml`, ruff, pre-commit | yes | yes | yes |
| `tests/` and pytest | yes | yes | yes |
| Documentation | full mkdocs site | `README.md` + `docs/quickstart.md` | `README.md` |
| CI test matrix | every supported Python | oldest and newest supported Python | none |
| `build.yaml`, `release.yaml`, `template-update.yaml` | yes | yes | no |
| `docs.yaml` (GitHub Pages) | yes | no | no |
| `.bumpversion.cfg` | yes | no | no |
| Coverage config | yes | yes | no |

The CI matrix follows the `python_version` answer rather than a fixed list: a
project that requires 3.12 is tested on 3.12 and 3.13, never on the versions it
declares it does not support.

`include_security_workflow` (a `bandit` scan) and `include_multiversion_testing`
(a local multi-version test helper script) stay as separate answers, so they can
be switched on for any profile that has a `.github` directory.

## Keeping a project in sync with the template

Projects created with `cruft create` record the template commit in
`.cruft.json`. The generated `template-update.yaml` workflow runs `cruft update`
monthly and opens a pull request with whatever changed here. The paths a project
owns rather than inherits — its README, its source, its tests, its documentation
pages — are listed under `[tool.cruft] skip` in the generated `pyproject.toml`
and are never overwritten.

For the workflow to be able to open that pull request, enable *Allow GitHub
Actions to create and approve pull requests* under Settings → Actions → General.

## Code quality

The generated `.pre-commit-config.yaml` uses **ruff** as the only Python linter
and the only Python formatter. The hooks that ruff supersedes — `isort`,
`black`, `blacken-docs`, `check-ast`, the `pretty-format-*` formatters — are
deliberately not there; `ruff format` covers the code blocks in docstrings via
`docstring-code-format`. What remains next to it are the five checks ruff does
not do: `check-merge-conflict`, `detect-private-key`, `check-yaml`,
`end-of-file-fixer` and `mixed-line-ending`.

The config carries a `ci:` block, so enabling the repository on
[pre-commit.ci](https://results.pre-commit.ci) is enough to get monthly hook
updates and autofix commits pushed to your pull requests.

**Type checking** is [mypy](https://mypy.readthedocs.io/) in `strict` mode,
configured under `[tool.mypy]` in the generated `pyproject.toml` and installed
by the `typing` extra. It is deliberately *not* a pre-commit hook: a hook runs
in its own isolated environment, without the project's dependencies, and
reports import errors that are not real. It runs instead as the `typecheck` job
of `test.yaml`, which installs the project first. Strict from the first commit
is the cheap moment to start; the ruff configuration already requires
annotations everywhere (`ANN`), so there is nothing extra to write. A
third-party package that ships no types is exempted case by case through a
`[[tool.mypy.overrides]]` block — there is a commented-out example in the
generated `pyproject.toml`. Generated packages carry a
[PEP 561](https://peps.python.org/pep-0561/) `py.typed` marker, so the
annotations are visible to whoever depends on them.

**Workflow linting** is [zizmor](https://docs.zizmor.sh/), which audits the
GitHub Actions workflows for the things that go wrong in CI rather than in
Python: credential persistence, shell injection through `${{ ... }}`
expansion, over-broad `permissions`, unpinned actions. It runs as a pre-commit
hook and in the `lint` job of `test.yaml`, where a token is available so the
audits that need the GitHub API also run. Its configuration is
`.github/zizmor.yml`: actions from the publishers this template already depends
on may be pinned to a release tag, and **every other action has to be pinned to
a commit hash**. Hash pinning everything without something like Dependabot to
move the hashes forward only trades a supply-chain risk for a staleness one,
which is why the split is there rather than a blanket exemption.

## Continuous integration

The generated project comes with the following GitHub Actions workflows in
`.github/workflows`:

| Workflow | Trigger | What it does |
| --- | --- | --- |
| `test.yaml` | push and pull request on `main`/`master`, twice a month, manual | Runs the unit tests with coverage on every supported Python, the ruff lint and format checks, `zizmor` over the workflows, `mypy` over the package, and (in the `package` profile) a strict mkdocs build. The `check` job at the end aggregates all of them. |
| `build.yaml` | push and pull request on `main`/`master` | Builds the sdist and the wheel with `uv build` and validates the distribution metadata with `twine check --strict`. |
| `docs.yaml` | push on `main`/`master`, manual | Publishes the mkdocs site to GitHub Pages with `mkdocs gh-deploy`. |
| `release.yaml` | GitHub release published | Builds and uploads the distribution to PyPI. |
| `security.yaml` | push and pull request on `main`/`master` | Runs `bandit`. Generated only when `include_security_workflow` is `yes`. |
| `template-update.yaml` | monthly, manual | Runs `cruft update` and opens a pull request with the changes made to this template. |

The `tiny` profile generates no workflows at all, and the `workflow` profile
generates everything except `docs.yaml`.

All workflows declare a least-privilege `permissions` block and a
`concurrency` group, so that a new push cancels the superseded runs. They are
checked out without persisted credentials wherever the job does not need to
push, and `zizmor` keeps them that way; the two places that do need the
credentials — the GitHub Pages deployment and the template-update pull
request — carry an inline `# zizmor: ignore[artipacked]` saying why.

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
