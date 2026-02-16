import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (0, 0, 0),
    (-1, -1, 0),
    (100, 200, -100),
    (-5, 5, -10),
    (1.5, 2.5, -1.0),
    (0, -2, 2)
])
def test_subtract_basic(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_typeerror():
    with pytest.raises(TypeError):
        subtract('1', 2)
    with pytest.raises(TypeError):
        subtract(1, None)
