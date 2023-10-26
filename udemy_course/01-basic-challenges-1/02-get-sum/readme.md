# Challenge: Get Sum

This is another very basic practice challenge just to get you into the hang of things.

## Instructions

Write a function called `calculate_sum` that takes in two numbers and returns the sum of those two numbers.

### Function Signature

```python
def get_sum(a: int, b: int) -> int:
    """
    Returns the sum of two numbers.

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    - int: The sum of the two numbers.
    """
```

### Examples

```python
calculate_sum(1, 2) # 3
calculate_sum(10, 5) # 15
calculate_sum(2, 2) # 4
calculate_sum(10, 5) # 15
```

### Constraints

- The function must return a number

### Hints

- You can use the `+` operator to add two numbers together.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def calculate_sum(a, b):
    return a + b
```

### Explanation

This is a pretty simple challenge. We created a function that takes in two values and we added those two values together. We then returned the sum of those two values.

</details>

### Test Cases

```python
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
```
