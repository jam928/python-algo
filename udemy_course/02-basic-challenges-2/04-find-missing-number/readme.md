# Challenge: Find The Missing Number

## Instructions

Write a function called `find_missing_number` that takes in an array of unique numbers from 1 to n (inclusive), where one number is missing. It should return the missing number.

### Function Signature

```python
from typing import List

def find_missing_number(arr: List[int]) -> int:
    """
    Returns the missing number in an array of unique numbers from 1 to n (inclusive).

    Parameters:
    - arr (List[int]): The array of numbers.

    Returns:
    - int: The missing number.
    """
    # Your function implementation goes here
```

### Examples

```python
find_missing_number([1, 2, 3, 4, 6, 7, 8, 9, 10]); # 5
find_missing_number([10, 8, 6, 7, 5, 4, 2, 3, 1]); # 9
find_missing_number([10, 5, 1, 2, 4, 6, 8, 3, 9]); # 7
```

### Constraints

- If an empty array is passed in, it should return `1`
- If nothing is passed in, it should return `undefined`

### Hints

- Calculate the sum of the numbers from 1 to n (inclusive). The formula for this is `n * (n + 1) / 2`. `n` is the length of the array plus 1.
- Calculate the sum of the numbers in the array.
- Subtract the sum of the numbers in the array from the sum of the numbers from 1 to n (inclusive).
- You could use a for loop or the reduce method to calculate the sum of the numbers in the array. We will be focusing on methods like reduce in the next section, but I will still show you both ways.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def find_missing_number(arr):
    if len(arr) == 0:
        return 1

    n = len(arr) + 1

    expected_sum = n * (n+1) / 2
    actual_sum = sum(arr)

    return expected_sum - actual_sum
```

### Explanation

The `findMissingNumber` function takes in an array of unique numbers from 1 to n (inclusive), where one number is missing, and returns the missing number.

We first calculate the sum of the numbers from 1 to n (inclusive) using the formula `n * (n + 1) / 2`. This is called the gauss formula. We store this value in a variable called `expected_sum`.

To be more clear, let's look at an example. If we have an array of numbers from 1 to 10, the sum of those numbers is 55. We can calculate this using the gauss formula. `10 * (10 + 1) / 2 = 55`. We can also calculate this using a for loop or the reduce method.

Next, we calculate the sum of the numbers in the array. We store this value in a variable called `actual_sum`.

We then return the difference between the expected sum and the actual sum. This will be the missing number.

Again, you can use a for loop or the reduce method to calculate the sum of the numbers in the array.

</details>

### Test Cases

```python
import find_missing_number as fmn


def test_finding_the_missing_number():
    assert fmn.find_missing_number([1, 2, 3, 5]) == 4
    assert fmn.find_missing_number([10, 8, 6, 7, 5, 4, 2, 3, 1]) == 9
    assert fmn.find_missing_number([1, 3, 4, 5, 6]) == 2
```
