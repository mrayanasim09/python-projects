# Development Guide

This document provides guidelines for developers contributing to the python-projects repository.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Development Setup](#development-setup)
4. [Code Style](#code-style)
5. [Testing](#testing)
6. [Pre-commit Hooks](#pre-commit-hooks)
7. [Building the Package](#building-the-package)
8. [Release Process](#release-process)

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mrayanasim09/python-projects.git
cd python-projects
```

### 2. Create a Virtual Environment

```bash
# On Linux/macOS
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install all dependencies including dev tools
pip install -e ".[dev]"

# Or install only test dependencies
pip install -e ".[test]"

# Or install from requirements.txt
pip install -r requirements.txt
```

## Development Setup

### Project Structure

```
python-projects/
├── Calculator/          # Calculator projects
├── Game/               # Game projects
├── GUI/                # GUI applications
├── Utilities/          # Utility scripts with tests
├── machine_learning/   # ML/AI projects
├── .github/workflows/  # CI/CD workflows
├── pyproject.toml      # Project configuration
├── setup.cfg           # Setup configuration
├── MANIFEST.in         # Package manifest
├── requirements.txt    # Dependencies
└── DEVELOPMENT.md      # This file
```

## Code Style

This project follows PEP 8 style guidelines with the following tools:

- **Black**: Code formatting
- **isort**: Import sorting
- **Flake8**: Linting
- **Mypy**: Type checking (optional)

### Formatting Code

```bash
# Format code with Black
black --line-length=100 .

# Sort imports with isort
isort --profile black .
```

### Linting

```bash
# Run Flake8
flake8 . --max-line-length=100 --statistics
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=Utilities --cov-report=term-missing

# Run specific test file
pytest Utilities/test_utilities.py -v

# Run tests with HTML coverage report
pytest --cov=Utilities --cov-report=html
```

### Writing Tests

Tests are located in the `Utilities/test_utilities.py` file. When adding new utilities, please add corresponding tests.

Example test structure:

```python
import pytest
from unittest.mock import patch, MagicMock

def test_example_function():
    """Test example function."""
    result = example_function(input_value)
    assert result == expected_value

@patch('module.external_dependency')
def test_with_mock(mock_dep):
    """Test with mocked dependency."""
    mock_dep.return_value = mocked_result
    result = function_using_dependency()
    assert result == expected_value
```

## Pre-commit Hooks

Pre-commit hooks help maintain code quality before commits.

### Installation

```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install
```

### Running Pre-commit

```bash
# Run on all files
pre-commit run --all-files

# Run on staged files only
pre-commit run
```

### Available Hooks

- Trailing whitespace removal
- End-of-file fixer
- YAML/JSON validation
- Black formatting
- isort import sorting
- Flake8 linting
- Bandit security scanning
- Pyupgrade (modern Python syntax)

## Building the Package

### Build Distribution Packages

```bash
# Install build tools
pip install build wheel

# Build source and wheel distributions
python -m build

# Or using setup.py
python setup.py sdist bdist_wheel
```

### Verify Package

```bash
# Check package metadata
twine check dist/*

# Install locally from built package
pip install dist/python_projects-1.0.0-py3-none-any.whl
```

## Release Process

1. **Update Version**
   - Update version in `pyproject.toml`
   - Update version in `setup.cfg`
   - Update `__version__` in module `__init__.py` files

2. **Update Changelog**
   - Add release notes to CHANGELOG.md (if exists)

3. **Run Tests**
   ```bash
   pytest --cov=Utilities
   ```

4. **Build Package**
   ```bash
   python -m build
   ```

5. **Create Git Tag**
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

6. **Publish to PyPI** (Optional)
   ```bash
   twine upload dist/*
   ```

## Continuous Integration

The repository uses GitHub Actions for CI/CD:

- **Test & Coverage**: Runs tests on Python 3.10, 3.11, 3.12
- **Lint**: Checks code formatting and style
- **Security**: Runs Bandit security scans

Workflows trigger on:
- Push to main/master branches
- Pull requests to main/master branches

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure you're in the virtual environment
   source venv/bin/activate
   
   # Reinstall package in editable mode
   pip install -e .
   ```

2. **Test Failures**
   ```bash
   # Clear pytest cache
   pytest --cache-clear
   
   # Run with verbose output
   pytest -vvv
   ```

3. **Pre-commit Hook Failures**
   ```bash
   # Update pre-commit hooks
   pre-commit autoupdate
   
   # Run hooks manually to see details
   pre-commit run --all-files --verbose
   ```

## Getting Help

- Open an issue on [GitHub](https://github.com/mrayanasim09/python-projects/issues)
- Join our [Discord](https://discord.gg/uRfXYjub)
- Check [FAQ.md](FAQ.md) for common questions

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.
