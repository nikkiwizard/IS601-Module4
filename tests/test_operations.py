# tests/test_operations.py

"""
Unit tests for the operations module using pytest.

This test suite covers both positive and negative scenarios for the Operation
class's static methods. It ensures that arithmetic operations perform correctly
and handle edge cases appropriately.

Tests are organized following the AAA (Arrange, Act, Assert) pattern and adhere
to PEP8 standards for code style and formatting.
"""

import pytest
from app.operation import Operation


# -----------------------------------------------------------------------------------
# Test Addition Method
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("a,b,expected", [
    (10.0, 5.0, 15.0),
    (-10.0, -5.0, -15.0),
    (10.0, -5.0, 5.0),
    (10.0, 0.0, 10.0),
])
def test_addition(a, b, expected):
    result = Operation.addition(a, b)
    assert result == expected, f"Expected {a} + {b} to be {expected}, got {result}"


# -----------------------------------------------------------------------------------
# Test Subtraction Method
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("a,b,expected", [
    (10.0, 5.0, 5.0),
    (-10.0, -5.0, -5.0),
    (10.0, -5.0, 15.0),
    (10.0, 0.0, 10.0),
])
def test_subtraction(a, b, expected):
    result = Operation.subtraction(a, b)
    assert result == expected, f"Expected {a} - {b} to be {expected}, got {result}"


# -----------------------------------------------------------------------------------
# Test Multiplication Method
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("a,b,expected", [
    (10.0, 5.0, 50.0),
    (-10.0, -5.0, 50.0),
    (10.0, -5.0, -50.0),
    (10.0, 0.0, 0.0),
])
def test_multiplication(a, b, expected):
    result = Operation.multiplication(a, b)
    assert result == expected, f"Expected {a} * {b} to be {expected}, got {result}"


# -----------------------------------------------------------------------------------
# Test Division Method
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("a,b,expected", [
    (10.0, 5.0, 2.0),
    (-10.0, -5.0, 2.0),
    (10.0, -5.0, -2.0),
    (0.0, 5.0, 0.0),
])
def test_division(a, b, expected):
    result = Operation.division(a, b)
    assert result == expected, f"Expected {a} / {b} to be {expected}, got {result}"


# -----------------------------------------------------------------------------------
# Test Power Method
# -----------------------------------------------------------------------------------


@pytest.mark.parametrize("a,b,expected", [
    (2.0, 3.0, 8.0),
    (5.0, 0.0, 1.0),
    (2.0, -1.0, 0.5),
    (-2.0, 3.0, -8.0),
    (0.0, 5.0, 0.0),
])
def test_power(a, b, expected):
    result = Operation.power(a, b)
    assert result == expected, f"Expected {a} ** {b} to be {expected}, got {result}"


def test_division_with_zero_divisor():
    """Verify dividing by zero raises the expected ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Operation.division(10.0, 0.0)
    assert str(exc_info.value) == "Division by zero is not allowed."


# -----------------------------------------------------------------------------------
# Test Invalid Input Types (Negative Testing)
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("calc_method, a, b, expected_exception", [
    (Operation.addition, '10', 5.0, TypeError),
    (Operation.subtraction, 10.0, '5', TypeError),
    (Operation.multiplication, '10', '5', TypeError),
    (Operation.division, 10.0, '5', TypeError),
    (Operation.power, 2.0, '3', TypeError),
])
def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    """
    Test that arithmetic methods raise TypeError when provided with invalid input types.
    
    This test verifies that providing non-float inputs to the arithmetic methods raises
    a TypeError, as the operations are intended for floating-point numbers.
    """
    # Arrange
    # No setup needed as the invalid inputs are provided directly

    # Act & Assert
    with pytest.raises(expected_exception):
        calc_method(a, b)

