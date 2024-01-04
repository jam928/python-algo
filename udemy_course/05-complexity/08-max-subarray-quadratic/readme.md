# Challenge: Maximum Subarray Sum - O(n^2) Solution

## Instructions

Write a function called `maxSubarraySum` that takes an array of integers and a positive integer `k` as input. The function should find the maximum sum of any subarray of length `k` using an O(n^2) solution by using nested for loops.

We will re-visit this and use the sliding window technique to use an O(n) solution.

### Function Signature

```python
from typing import List

def max_subarray_sum(arr: List[int], k: int) -> int:
    """
    Finds the maximum sum of any subarray of length k in the input array using an O(n^2) solution.

    Parameters:
        arr (List[int]): The input list of integers.
        k (int): The length of the subarray.

    Returns:
        int: The maximum sum of any subarray of length k.
    """
    # Function implementation goes here
```

### Examples

```python
arr1 = [2, 5, 3, 1, 11, 7, 6, 4]
k1 = 3
print(max_subarray_sum(arr1, k1)) # Output: 24

arr2 = [-2, -5, -3, -1, -11, -7, -6, -4];
k2 = 4;
print(max_subarray_sum(arr2, k2)); # Output: -9
```

### Constraints

- The input integer `k` will be between 1 and the length of the array.

### Hints

- You can use two nested loops to iterate through all possible subarrays of length `k` and calculate their sums.

### Solutions

<details>
  <summary>Click For Solution</summary>

```python
def max_subarray_quadratic(arr, k):
    max_sum = 0

    for i in range(len(arr) - k):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += arr[j]

        max_sum = max(current_sum, max_sum)

    return max_sum
```

### Explanation

- The function `max_subarray_quadratic` uses two nested loops to iterate through all possible subarrays of length `k`.
- For each subarray, it calculates the sum using a nested loop and keeps track of the maximum sum encountered.
- Finally, it returns the maximum sum.

</details>

### Test Cases

```python
from max_subarray_quadratic import max_subarray_quadratic


def test_maximum_subarray_using_squared_solution():
    arr1 = [2, 5, 3, 1, 11, 7, 6, 4]
    k1 = 3
    max_subarray_quadratic(arr1, k1) == 24

    arr2 = [-2, -5, -3, -1, -11, -7, -6, -4]
    k2 = 4
    max_subarray_quadratic(arr2, k2) == -9
```

---

Please note that the provided solution has a time complexity of O(n^2) due to the nested loops.
