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


🎉 Congratulations! Wishing you every success as you begin your project journey 🚀

Saez-Rodriguez Group Team!

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Python-project template has a [BSD3](https://opensource.org/license/bsd-3-clause) license, as found in the [LICENSE](./LICENSE) file.
