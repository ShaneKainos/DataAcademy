from math_functions import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(5, 5) == 10

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(20, 12) == 8
    assert subtract(2, 2) == 0