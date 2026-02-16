# Math Operations Project

## Overview
This project implements basic math operations (addition and subtraction) in Python and provides comprehensive pytest-based unit tests. CI/CD workflow is integrated for automated testing and reporting.

## Folder Structure
- `src/`: Contains production Python code for math operations.
- `tests/`: Contains pytest unit tests for addition and subtraction.
- `default/`: Contains CI metadata, requirements, and documentation.

## Usage
### Math Operations
```
from src.math_operations import add, subtract

result_add = add(2, 3)      # 5
result_subtract = subtract(5, 2)  # 3
```

### Running Tests
Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests with reporting:
```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow
Automated tests are triggered on push to `Feature3` and pull requests to `main` branch. Artifacts are uploaded to S3.

## Requirements
See `default/requirements.txt` for dependencies.
