from calculator import Calculator, CalculatorError
import pytest

# Arrange - setting up anything you need before the action happens
# Act - core thing
# Assert - What is you asserting? Where  you get that is from your action.


def test_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5


def test_add_with_weird_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError): # raises an error and the user should decide to handle that
        result = calculator.add("two", 3)

def test_add_with_weirder_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError): 
        result = calculator.add("two", "three")


def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(9, 3)
    assert result == 6


def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(9, 3)
    assert result == 27


def test_divide():
    calculator = Calculator()
    result = calculator.divide(9, 3)
    assert result == 3

def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 0)
    
