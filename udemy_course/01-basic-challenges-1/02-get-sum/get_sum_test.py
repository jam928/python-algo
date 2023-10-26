import get_sum  # Assuming you have a 'get_sum.py' module
import pytest

def test_calculate_sum():
    # Test case inputs
    num1 = 5
    num2 = 7

    # Call the function
    result = get_sum.calculate_sum(num1, num2)

    # Check if the result is equal to the expected sum
    assert result == 12