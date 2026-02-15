import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-3, -7) == -10

def test_add_mixed_sign_numbers():
    assert add(10, -3) == 7
    assert add(-4, 9) == 5

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 7) == 7
    assert add(5, 0) == 5

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)
    assert add(-1.1, 1.1) == pytest.approx(0.0)

def test_add_large_numbers():
    assert add(1_000_000_000, 2_000_000_000) == 3_000_000_000
