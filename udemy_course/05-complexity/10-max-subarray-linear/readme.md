# Challenge: Maximum Subarray Sum - O(n) Solution

## Instructions

Write a function called `max_subarray_sum` that takes an array of integers and a positive integer `k` as input. The function should find the maximum sum of any subarray of length `k` using an O(n) solution by using the sliding window technique.

### Function Signature

```python
from typing import List

def max_subarray_sum(arr: List[int], k: int) -> int:
    """
    Finds the maximum sum of any subarray of length k in the input array using an O(n) solution.

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
print(max_subarray_sum(arr2, k2)) # Output: -9
```

### Constraints

- The input integer `k` will be between 1 and the length of the array.

### Hints

- You can use the sliding window technique to efficiently track the sum of subarrays of length k as you iterate through the array.

### Solutions

<details>
  <summary>Click For Solution</summary>

```python
def max_subarray_sum(arr, k):
    current_sum = 0
    max_sum = 0

    for i in range(k):
        max_sum += arr[i]

    current_sum = max_sum

    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(current_sum, max_sum)

    return max_sum
```

### Explanation

- maxSum and currentSum are initialized to 0. These variables will be used to track the maximum sum and the sum of the current sliding window, respectively.

- The first loop (for loop) calculates the sum of the first k elements in the array arr and assigns it to maxSum. This initializes the currentSum and maxSum for the first sliding window.

- currentSum is then set to the value of maxSum. This sets the initial sum of the current sliding window.

- The second loop (for loop) starts at index k and iterates through the array arr. This loop implements the sliding window technique.

- Within the second loop, currentSum is updated using the sliding window concept. The element that leaves the window (at index i - k) is subtracted, and the new element entering the window (at index i) is added.

- An optional console.log statement logs the update of currentSum for visualization purposes, showing how the window slides and how the current sum changes.

- maxSum is updated using the Math.max function to keep track of the maximum sum encountered during the sliding window traversal.

- Finally, the function returns the maxSum, which represents the maximum sum of any subarray of length k in the input array.

</details>

### Test Cases

```python
from max_subarray_linear import max_subarray_sum


def test_maximum_subarray_using_linear_solution():
    arr1 = [2, 5, 3, 1, 11, 7, 6, 4]
    k1 = 3
    max_subarray_sum(arr1, k1) == 24

    arr2 = [-2, -5, -3, -1, -11, -7, -6, -4]
    k2 = 4
    max_subarray_sum(arr2, k2) == -9
```

---

- T: O(n)
- S: O(1)
