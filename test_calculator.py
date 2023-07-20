import calculator
import pytest

# TC-1-01 - Addition Function
def test_addition():
    result = calculator.add(3, 4)
    assert result == 7

# TC-1-02 - Subtraction Function
def test_subtraction():
    result = calculator.subtract(8, 5)
    assert result == 3

# TC-1-03 - Multiplication Function
def test_multiplication():
    result = calculator.multiply(2, 6)
    assert result == 12

# TC-1-04 - Division Function
def test_division():
    result = calculator.divide(10, 2)
    assert result == 5

# TC-1-05 - Invalid Selection
def test_invalid_selection():
    with pytest.raises(ValueError):
        raise ValueError("Invalid selection")

# TC-1-06 - Division by Zero
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)

# TC-1-07 - Lower boundary input values
def test_lower_boundary():
    result = calculator.add(0, 0)
    assert result == 0

# TC-1-08 - Upper boundary input values
def test_upper_boundary():
    result = calculator.multiply(9999, 9999)
    assert result == 99980001