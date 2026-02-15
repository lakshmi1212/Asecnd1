import pytest
from src.math_operations import subtract

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 0),
        (0, 0, 0),
        (-1, 1, -2),
        (100, 200, -100),
        (-5, -7, 2),
        (5.5, 2.5, 3.0),
        (1e10, 1e9, 9e9)
    ]
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

