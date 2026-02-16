# Math Operations Module

This repository provides basic math operations (`add` and `subtract`) with production-ready unit tests and CI integration guidance.

## Folder Structure

- `src/` : Source code for math operations
- `tests/` : Pytest-based unit tests
- `default/` : Project metadata, requirements, and documentation

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))       # Output: 5
print(subtract(5, 2))  # Output: 3
```

## Running Tests

Install dependencies:
```
pip install -r default/requirements.txt
```

Run all tests:
```
pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD Workflow

- Workflow file: `.github/workflows/ci.yml`
- On push to `Feature4` or PR to `main`, tests run automatically and generate reports in `reports/`.

## Requirements

- Python >=3.10
- pytest
- pytest-html
