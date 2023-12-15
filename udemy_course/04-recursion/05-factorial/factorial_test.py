from factorial import factorial


def test_factorial_of_0_should_be_1():
    assert factorial(0) == 1


def test_factorial_of_5_should_be_120():
    assert factorial(5) == 120


def test_factorial_of_10_should_be_3628800():
    assert factorial(10) == 3628800
