#!/usr/bin/env python3
"""Run tests across multiple Python versions using uv.

This script replaces tox for local multi-version testing. It creates isolated
virtual environments for each Python version, installs the package with test
dependencies, and runs pytest.

Usage:
    # Run tests on all Python versions this project supports
    python scripts/test-multi-py.py

    # Run tests on specific versions
    python scripts/test-multi-py.py 3.11 3.12

    # Run tests with additional pytest arguments
    python scripts/test-multi-py.py 3.12 -- -v --tb=short

    # Run tests in parallel (requires multiple Python versions installed)
    python scripts/test-multi-py.py --parallel

Requirements:
    - uv (https://docs.astral.sh/uv/)
    - Python versions you want to test must be installed or discoverable by uv
"""

import sys
import shutil
from pathlib import Path
import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

{% set _all = cookiecutter._python_versions %}
DEFAULT_VERSIONS = [
{%- for _v in _all[_all.index(cookiecutter.python_version):] %}
    '{{ _v }}',
{%- endfor %}
]
VENV_PREFIX = '.venv-test-'


def run_command(
    cmd: list[str],
    cwd: Path | None = None,
    capture: bool = False,
) -> subprocess.CompletedProcess:
    """Run a shell command and return the result."""
    return subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=capture,
        text=True,
        check=False,
    )


def check_uv() -> None:
    """Exit with an error message unless uv is installed."""
    if shutil.which('uv') is None:
        print('Error: uv is not installed.')
        print(
            'Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh',
        )
        sys.exit(1)


def check_python_version(version: str) -> bool:
    """Tell whether a Python version is available via uv."""
    result = run_command(
        ['uv', 'python', 'find', version],
        capture=True,
    )

    return result.returncode == 0


def run_tests_for_version(
    version: str,
    project_root: Path,
    pytest_args: list[str],
    verbose: bool = True,
) -> tuple[str, bool | None, str]:
    """Run tests for a specific Python version.

    Returns:
        The version, whether the tests passed (`None` if the version was not
        available) and the captured output.
    """
    venv_path = project_root / f'{VENV_PREFIX}{version}'

    if verbose:
        print(f'\n{"=" * 60}')
        print(f'Testing with Python {version}')
        print(f'{"=" * 60}')

    # Check if Python version is available
    if not check_python_version(version):
        msg = (
            f'Python {version} not found. '
            f'Install with: uv python install {version}'
        )

        if verbose:
            print(f'Warning: {msg}')

        return (version, None, msg)

    # Create virtual environment
    if verbose:
        print(f'Creating virtual environment at {venv_path}...')

    result = run_command(
        ['uv', 'venv', str(venv_path), '--python', version],
        cwd=project_root,
        capture=not verbose,
    )

    if result.returncode != 0:
        return (version, False, f'Failed to create venv: {result.stderr}')

    # Install package with test dependencies
    if verbose:
        print('Installing package with test dependencies...')

    python_path = venv_path / 'bin' / 'python'

    result = run_command(
        [
            'uv',
            'pip',
            'install',
            '-e',
            '.[tests]',
            '--python',
            str(python_path),
        ],
        cwd=project_root,
        capture=not verbose,
    )

    if result.returncode != 0:
        return (version, False, f'Failed to install: {result.stderr}')

    # Run pytest
    if verbose:
        print('Running tests...')

    result = run_command(
        [str(python_path), '-m', 'pytest', *pytest_args],
        cwd=project_root,
        capture=not verbose,
    )

    success = result.returncode == 0

    if verbose:
        print(f'\nPython {version}: {"PASSED" if success else "FAILED"}')

    return (version, success, '' if verbose else result.stdout)


def cleanup_venvs(project_root: Path) -> None:
    """Remove test virtual environments."""
    for venv_path in project_root.glob(f'{VENV_PREFIX}*'):
        if venv_path.is_dir():
            shutil.rmtree(venv_path)


def find_project_root() -> Path:
    """Return the closest parent directory containing a `pyproject.toml`."""
    project_root = Path.cwd()

    while project_root != project_root.parent:
        if (project_root / 'pyproject.toml').exists():
            return project_root

        project_root = project_root.parent

    print('Error: Could not find pyproject.toml')
    sys.exit(1)


def status_of(success: bool | None) -> str:
    """Render a per-version result as a word."""
    if success is None:
        return 'SKIPPED'

    return 'PASSED' if success else 'FAILED'


def build_parser() -> argparse.ArgumentParser:
    """Build the command line parser."""
    parser = argparse.ArgumentParser(
        description='Run tests across multiple Python versions using uv.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        'versions',
        nargs='*',
        default=DEFAULT_VERSIONS,
        help=(
            f'Python versions to test (default: {", ".join(DEFAULT_VERSIONS)})'
        ),
    )
    parser.add_argument(
        '--parallel',
        '-p',
        action='store_true',
        help='Run tests in parallel',
    )
    parser.add_argument(
        '--cleanup',
        '-c',
        action='store_true',
        help='Remove test virtual environments after running',
    )
    parser.add_argument(
        '--cleanup-only',
        action='store_true',
        help='Only remove test virtual environments, do not run tests',
    )

    return parser


def main() -> None:
    """Run the tests for every requested Python version."""
    # Handle -- separator for pytest args
    if '--' in sys.argv:
        idx = sys.argv.index('--')
        our_args = sys.argv[1:idx]
        pytest_args = sys.argv[idx + 1 :]
    else:
        our_args = sys.argv[1:]
        pytest_args = []

    args = build_parser().parse_args(our_args)
    project_root = find_project_root()

    check_uv()

    if args.cleanup_only:
        print('Cleaning up test virtual environments...')
        cleanup_venvs(project_root)
        print('Done.')

        return

    versions = args.versions

    print(f'Testing Python versions: {", ".join(versions)}')
    print(f'Project root: {project_root}')

    if pytest_args:
        print(f'Pytest args: {" ".join(pytest_args)}')

    results = {}

    if args.parallel:
        print('\nRunning tests in parallel...')

        with ThreadPoolExecutor(max_workers=len(versions)) as executor:
            futures = [
                executor.submit(
                    run_tests_for_version,
                    version,
                    project_root,
                    pytest_args,
                    verbose=False,
                )
                for version in versions
            ]

            for future in as_completed(futures):
                version, success, _ = future.result()
                results[version] = success
                print(f'Python {version}: {status_of(success)}')
    else:
        for version in versions:
            version, success, _ = run_tests_for_version(
                version,
                project_root,
                pytest_args,
                verbose=True,
            )
            results[version] = success

    # Summary
    print(f'\n{"=" * 60}')
    print('SUMMARY')
    print(f'{"=" * 60}')

    passed = sum(1 for s in results.values() if s is True)
    failed = sum(1 for s in results.values() if s is False)
    skipped = sum(1 for s in results.values() if s is None)

    for version in versions:
        print(f'  Python {version}: {status_of(results.get(version))}')

    print(f'\nTotal: {passed} passed, {failed} failed, {skipped} skipped')

    if args.cleanup:
        print('\nCleaning up test virtual environments...')
        cleanup_venvs(project_root)

    sys.exit(1 if failed > 0 else 0)


if __name__ == '__main__':
    main()
