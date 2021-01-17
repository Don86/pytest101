# Sauce: https://www.youtube.com/watch?v=etosV2IWBF0
import pytest
from calc import Calculator, CalculatorError


def my_first_test_function():
    # This will automatically pass, 
    # because this asserts that True == True
    assert True


def test_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5


def test_add_weird_stuff():
    # Exceptions
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add("two", 3)


def test_add_weirder_stuff():
    # Exceptions
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add("two", "three")


def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 1) == 4
    assert calculator.subtract(1, 1) == 0
    assert calculator.subtract(0, 2) == -2


def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(5, 1) == 5
    assert calculator.multiply(1, -3) == -3
    assert calculator.multiply(0, 2) == 0


def test_divide():
    calculator = Calculator()
    assert calculator.divide(5, 1) == 5
    assert calculator.divide(9, 3) == 3
    assert calculator.divide(9, -3) == -3
