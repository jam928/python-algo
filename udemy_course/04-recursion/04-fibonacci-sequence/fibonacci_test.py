from fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(0) == 0  # The 0th Fibonacci number is 0
    assert fibonacci(1) == 1  # The 1st Fibonacci number is 1
    assert fibonacci(2) == 1  # The 2nd Fibonacci number is 1 (0 + 1)
    assert fibonacci(3) == 2  # The 3rd Fibonacci number is 2 (1 + 1)
    assert fibonacci(4) == 3  # The 4th Fibonacci number is 3 (1 + 2)
    assert fibonacci(5) == 5  # The 5th Fibonacci number is 5 (2 + 3)
    assert fibonacci(6) == 8  # The 6th Fibonacci number is 8 (3 + 5)
    assert fibonacci(7) == 13  # The 7th Fibonacci number is 13 (5 + 8)
