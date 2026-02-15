# Math Operations Module

This repository contains Python functions for basic math operations (addition and subtraction) and corresponding pytest-based unit tests.

## Folder Structure
- `src/`: Production Python code
- `tests/`: Pytest test files
- `default/`: Metadata, requirements, and documentation

## Usage

Import math_operations:

```python
from src.math_operations import add, subtract

print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run tests:

```bash
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow

CI is triggered on push to Feature3 and pull requests to main. Test results are uploaded to S3 and stored in `reports/`.

See `default/math.json` for workflow metadata.
