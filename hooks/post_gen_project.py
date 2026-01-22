"""Post-generation hook for cookiecutter template."""

import os
import shutil

# Get the cookiecutter variables
include_security_workflow = '{{ cookiecutter.include_security_workflow }}'
include_multiversion_testing = '{{ cookiecutter.include_multiversion_testing }}'

# Files/directories to remove based on options
REMOVE_PATHS = []

if include_security_workflow == 'no':
    REMOVE_PATHS.append('.github/workflows/ci-security.yml')

if include_multiversion_testing == 'no':
    REMOVE_PATHS.append('scripts')


def remove_path(path):
    """Remove a file or directory if it exists."""
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def main():
    """Remove optional files based on cookiecutter configuration."""
    for path in REMOVE_PATHS:
        remove_path(path)


if __name__ == '__main__':
    main()
