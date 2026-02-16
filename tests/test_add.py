import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-2, -4) == -6

def test_add_positive_and_negative():
    assert add(7, -3) == 4

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_float_numbers():
    assert add(2.5, 3.2) == pytest.approx(5.7)

def test_add_string_type_error():
    with pytest.raises(TypeError):
        add('2', 3)
