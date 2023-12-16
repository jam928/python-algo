# Power

## Instructions

Write a function called `power` that takes in a `base` and an `exponent` and returns the result of raising the `base` to the power of the `exponent`. Use recursion to solve this problem.

### Function Signature

```python
def power(base: float, exponent: float) -> float:
    """
    Returns the result of raising the base to the power of the exponent.
    
    Parameters:
        base (float): The base number.
        exponent (float): The exponent.
        
    Returns:
        float: The result of the calculation.
    """
```

### Examples

```python
power(2, 3) # 8 (2^3 = 2 * 2 * 2 = 8)
power(5, 2) # 25 (5^2 = 5 * 5 = 25)
power(3, 4) # 81 (3^4 = 3 * 3 * 3 * 3 = 81)
```

### Constraints

- The base and exponent will always be positive integers

### Hints

- Remember that any number raised to the power of 0 is 1. This should give you the base case
- Think about how you can break down the problem into smaller parts using recursion

## Solutions

<details>
  <summary>Click For Solution</summary>

```js
def power(base: float, exponent: float) -> float:
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)
```

### Explanation

- The base case of the recursion is when the exponent is 0. In this case, we return 1 because any number raised to the power of 0 is 1.
- For any other value of exponent, we break down the problem into smaller parts. To raise the base to the power of exponent, we can start by multiplying the base by the result of the function called with the same base and the exponent decremented by 1. This recursive step forms the essence of the algorithm, as it continually reduces the problem until it reaches the base case.

Let's us `power(2, 5)` and look at the exact steps including reaching the base case and unwinding and cycling through the returns:

```js
base = 2
exponent = 5
exponent !== 0 so base case is skipped
return 2 * power(2, 4)
exponent = 4
return 2 * power(2, 3)
exponent = 3
return 2 * power(2, 2)
exponent = 2
return 2 * power(2, 1)
exponent = 1
return 2 * power(2, 0)
exponent = 0
return 1
```

Now we start unwinding:

```js
return 1 * 2 = 2
return 2 * 2 = 4
return 4 * 2 = 8
return 8 * 2 = 16
return 16 * 2 = 32
```

</details>

### Test Cases

```python
from power import power


def test_calculate_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(3, 4) == 81

```
