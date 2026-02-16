# Math Operations

This repository provides basic math operations (addition and subtraction) with comprehensive tests and CI-ready metadata.

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))       # 5
print(subtract(5, 3))  # 2
```

## Running Tests

Install dependencies:
```
pip install -r default/requirements.txt
```

Run tests:
```
pytest tests/
```

## CI/CD

This repo is CI-ready. See `default/math.json` for workflow metadata.
