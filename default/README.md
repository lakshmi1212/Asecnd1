# Math Operations Module

This repository provides basic math operations (addition, subtraction) with automated tests and CI integration.

## Structure

- `src/math_operations.py`: Core math logic (add, subtract)
- `tests/test_add.py`: Tests for addition
- `tests/test_subtract.py`: Tests for subtraction
- `default/requirements.txt`: Python dependencies
- `default/math.json`: Metadata for workflow automation

## Usage

```python
from src.math_operations import add, subtract
print(add(2, 3))       # 5
print(subtract(5, 2))  # 3
```

## Running Tests

Install dependencies:
```bash
pip install -r default/requirements.txt
```

Run tests:
```bash
pytest tests/
```

## CI/CD Workflow

Refer to `.github/workflows/ci.yml` for pipeline details. Workflow metadata is provided in `default/math.json` for automation agents.
