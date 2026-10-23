import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(5, 0) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(10.0, 2.0) == 5.0
    with pytest.raises(ValueError):
        calc.divide(5.0, 0.0)
