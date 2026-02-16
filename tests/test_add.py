import pytest
from src.math_operations import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, -1, -2),
    (100, 200, 300),
    (-5, 5, 0),
    (1.5, 2.5, 4.0),
    (0, -2, -2)
])
def test_add_basic(a, b, expected):
    assert add(a, b) == expected

def test_add_typeerror():
    with pytest.raises(TypeError):
        add('1', 2)
    with pytest.raises(TypeError):
        add(1, None)
