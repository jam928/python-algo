# The function to be tested
def add(a, b):
    return a + b

# The corresponding pytest test case
import pytest

def test_add():
    assert add(2, 3) == 5  # Test the sum of 2 and 3
    assert add(-1, 1) == 0  # Test the sum of -1 and 1
    assert add(0, 0) == 0  # Test the sum of 0 and 0
    assert add(10, -5) == 5  # Test the sum of 10 and -5

if __name__ == "__main__":
    pytest.main()
