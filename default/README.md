# Math Operations Python Module

## Overview
This repository provides simple math operations (addition and subtraction) with production-ready test coverage using `pytest`.

## Folder Structure
- `src/` : Source code for math operations
- `tests/` : Pytest-based test files
- `default/requirements.txt` : Python dependencies
- `default/README.md` : Project documentation
- `default/math.json` : CI/CD and metadata for workflow generation

## Usage
```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Running Tests
Install dependencies:
```bash
pip install -r default/requirements.txt
```
Run all tests:
```bash
pytest tests/
```

## Workflow
The repository is designed for CI/CD integration. See `default/math.json` for workflow metadata.
