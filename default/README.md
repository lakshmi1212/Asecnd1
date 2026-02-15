# Math Operations Project

This repository implements basic math operations and automated testing using pytest.

## Source Code
- `src/math_operations.py`: Contains `add` and `subtract` functions.

## Tests
- `tests/test_add.py`: Tests for the `add` function.
- `tests/test_subtract.py`: Tests for the `subtract` function.

## Requirements
Install dependencies:

```bash
pip install -r default/requirements.txt
```

## Running Tests
Execute all tests and generate reports:

```bash
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD Workflow
The workflow is defined in `.github/workflows/ci.yml` and runs tests on push or pull request.

## Branches
- Default branch: `main`
- Feature branch: `Feature3`
