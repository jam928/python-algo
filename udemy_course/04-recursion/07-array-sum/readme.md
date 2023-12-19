# Challenge: Array Sum Using Recursion

## Description

Let's practice using recursion by creating a function that calculates the sum of an array of numbers. Write a function called `array_sum` that takes in an array of numbers and returns their sum using recursion.

## Instructions

Write a function called `array_sum` that takes in an array of numbers and returns their sum using recursion.

### Function Signature

```python
from typing import List

def array_sum(arr: List) -> float:
    """
    Calculates the sum of an array of numbers using recursion.

    Parameters:
        arr (List): The list of numbers.

    Returns:
        float: The sum of the numbers.
    """
    # Function implementation goes here
```

### Constraints

- The input array can contain positive and/or negative integers.

### Hints

- Think about what your base case might be with an array
- Think about how you can break down the problem of calculating the sum of an array into smaller sub-problems.
- You can use `arr.slice(1)` to create a new array excluding the first element.

### Examples

```python
array_sum([1, 2, 3, 4, 5]) # should return 15 (1 + 2 + 3 + 4 + 5 = 15)
array_sum([-1, -2, -3, -4, -5]) # should return -15 (-1 + -2 + -3 + -4 + -5 = -15)
array_sum([]) # should return 0 (empty array)
```

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
from typing import List


def array_sum(arr: List) -> float:
    def array_sum_helper(i, arr):
        if len(arr) - 1 == i:
            return arr[len(arr) - 1]

        return arr[i] + array_sum_helper(i + 1, arr)

    return 0 if len(arr) == 0 else array_sum_helper(0, arr)
```

### Explanation

- Use `array_sum_helper` to recursively call the array with an index
- in the helper call if i is the length of the array return that number
- return the number at i plus the recursive calls of array sum helper i + 1

</details>

### Test Cases

```python
from array_sum import array_sum


def test_calculate_sum_of_array_using_recursion():
    assert array_sum([1, 2, 3, 4, 5]) == 15
    assert array_sum([-1, -2, -3, -4, -5]) == -15
    assert array_sum([]) == 0
    assert array_sum([1,2]) == 3
    assert array_sum([1]) == 1
```
