"""Post-generation hook for cookiecutter template."""

import os
import shutil


# The cookiecutter answers this hook branches on.
project_profile = '{{ cookiecutter.project_profile }}'
include_security_workflow = '{{ cookiecutter.include_security_workflow }}'
include_multiversion_testing = '{{ cookiecutter.include_multiversion_testing }}'

# Files and directories to remove for the selected options. Everything the
# template can generate is written out first and pruned here; Jinja
# conditionals are used only *inside* files, never to skip whole paths.
REMOVE_PATHS = []

# The only documentation page the `workflow` profile keeps: no mkdocs site,
# no API reference, no community tree, just a quickstart next to the README.
WORKFLOW_KEEP_DOCS = frozenset({'quickstart.md'})

if include_security_workflow == 'no':
    REMOVE_PATHS.append('.github/workflows/security.yaml')

if include_multiversion_testing == 'no':
    REMOVE_PATHS.append('scripts')

if project_profile != 'package':
    # No documentation site and no version bumping outside the `package`
    # profile; see the `project_profile` prompt in `cookiecutter.json`.
    REMOVE_PATHS += [
        '.bumpversion.cfg',
        'mkdocs.yml',
        '.github/workflows/docs.yaml',
    ]

if project_profile == 'tiny':
    # `pyproject.toml` + ruff + pre-commit + a single test, nothing else.
    REMOVE_PATHS += [
        '.github',
        '.codecov.yaml',
        '.coveragerc',
        'docs',
        'scripts',
    ]


def remove_path(path):
    """Remove a file or directory if it exists."""
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def prune_docs():
    """Reduce `docs/` to the pages the `workflow` profile keeps."""
    if not os.path.isdir('docs'):
        return

    for entry in os.listdir('docs'):
        if entry not in WORKFLOW_KEEP_DOCS:
            remove_path(os.path.join('docs', entry))


def main():
    """Post-generation processing."""
    # Remove optional files based on configuration
    for path in REMOVE_PATHS:
        remove_path(path)

    if project_profile == 'workflow':
        prune_docs()


if __name__ == '__main__':
    main()
