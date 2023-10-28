import calculator
import pytest


def test_perform_calculator_operations():
    num1 = 5
    num2 = 7

    assert calculator.calculate(num1, num2, '+') == 12
    assert calculator.calculate(num1, num2, '-') == -2
    assert calculator.calculate(num1, num2, '*') == 35
    assert calculator.calculate(num1, num2, '/') == 0.7142857142857143