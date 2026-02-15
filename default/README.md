# Math Operations Project

## Overview
This project provides basic math operations (addition and subtraction) implemented in Python, with comprehensive pytest-based tests and CI/CD integration instructions.

## Source Code
- **src/math_operations.py**: Contains `add` and `subtract` functions.

## Tests
- **tests/test_add.py**: Pytest cases for addition.
- **tests/test_subtract.py**: Pytest cases for subtraction.

## Requirements
Install dependencies:
```
pip install -r default/requirements.txt
```

## Running Tests
Run all tests and generate reports:
```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD Workflow
- Workflow file: `.github/workflows/ci.yml`
- Default branch: `main`
- Feature branch: `Feature3`

## Metadata
See `default/math.json` for workflow and test metadata.
