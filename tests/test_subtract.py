import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6

def test_subtract_negative_numbers():
    assert subtract(-4, -2) == -2

def test_subtract_positive_and_negative():
    assert subtract(5, -2) == 7
    assert subtract(-2, 5) == -7

def test_subtract_zero():
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_large_numbers():
    assert subtract(3000000, 1000000) == 2000000

def test_subtract_float_numbers():
    assert subtract(5.7, 2.2) == pytest.approx(3.5)

def test_subtract_string_type_error():
    with pytest.raises(TypeError):
        subtract('2', 3)
