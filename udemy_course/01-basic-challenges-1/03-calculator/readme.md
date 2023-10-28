# Challenge: Calculator

## Instructions

Write a function called `calculator` that takes in 2 numbers and an operator and returns the result of the calculation.

### Function Signature

```python
def calculator(num1: float, num2: float, operator: str) -> float:
    """
    Returns the result of a calculation.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operator (str): The operator to use in the calculation.

    Returns:
    - float: The result of the calculation.
    """
```

### Examples

```python
calculator(1, 2, '+') # 3
calculator(10, 5, '-') # 5
calculator(2, 2, '*') # 4
calculator(10, 5, '/') # 2
```

### Constraints

- The function must return a number
- The function must throw or log an error if an invalid operator is given

### Hints

- You can use `if` statements or `switch` statements to determine which operator was given.

## Solutions

<details>
 <summary>Click For Solution 1</summary>

#### Using an if statement:

```python
def calculate(num1, num2, operator):
    # Declare a variable to store the result
    result = None

    # Use if/elif/else statements to determine which operation to perform
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        # If the operator is not one of the above, raise an error
        raise ValueError('Invalid operator')

    return result
```

### Explanation

- Create a function called `calculate` that takes in three arguments: `num1`, `num2`, and `operator`.
- Create a variable called `result` to store the result of the calculation.
- Use an `if` statement to determine which operator was given. If it was +, -, \* or /, we did the calculation. If the operator is anything else, we throw an error.

 </details>

### Test Cases

```python
import calculator
import pytest

def test_perform_calculator_operations():
    num1 = 5
    num2 = 7

    assert calculator.calculate(num1, num2, '+') == 12
    assert calculator.calculate(num1, num2, '-') == -2
    assert calculator.calculate(num1, num2, '*') == 35
    assert calculator.calculate(num1, num2, '/') == 0.7142857142857143
```
