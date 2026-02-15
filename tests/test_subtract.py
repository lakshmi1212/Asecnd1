import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(8, 5) == 3

def test_subtract_negative_numbers():
    assert subtract(-3, -7) == 4

def test_subtract_mixed_sign_numbers():
    assert subtract(10, -3) == 13
    assert subtract(-4, 9) == -13

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 7) == -7
    assert subtract(5, 0) == 5

def test_subtract_floats():
    assert subtract(2.5, 3.1) == pytest.approx(-0.6)
    assert subtract(-1.1, 1.1) == pytest.approx(-2.2)

def test_subtract_large_numbers():
    assert subtract(2_000_000_000, 1_000_000_000) == 1_000_000_000
