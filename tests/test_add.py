import pytest
from src.math_operations import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_mixed():
    assert add(-2, 3) == 1
    assert add(2, -3) == -1

def test_add_large_numbers():
    assert add(10**6, 10**6) == 2*10**6
