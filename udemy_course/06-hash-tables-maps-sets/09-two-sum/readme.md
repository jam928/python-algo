# Challenge: Two Sum

## Instructions

Write a function called `two_sum` that takes an array of integers and a target integer as input and returns an array of indices of the two numbers that add up to the target.

### Function Signature

```python
from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Returns a list of indices of two numbers that add up to the target.
    
    Parameters:
    - nums (List[int]): The input list of integers.
    - target (int): The target sum.
    
    Returns:
    - List[int]: A list of indices of the two numbers.
    """
    # Your function implementation goes here
    pass  # Placeholder for function body
```

### Examples

```python
print(two_sum([2, 7, 11, 15], 9))
# Output: [0, 1] (2 + 7 = 9)

print(two_sum([3, 2, 4], 6));
# Output: [1, 2] (2 + 4 = 6)

print(two_sum([3, 3], 6));
# Output: [0, 1] (3 + 3 = 6)
```

### Constraints

- Each input integer is unique.

### Hints

- You can use a Set to keep track of numbers you've seen so far while iterating through the array.

### Solution

<details>
  <summary>Click to reveal solution</summary>

```python
from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> List[int]:
    # Add elements to set while iterating thru target
    nums_dict = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement], index]
        nums_dict.update({num: index})

    return []
```

### Explanation

- Create a `dict` called `nums_dict` to store numbers that have been seen while iterating through the array.
- Iterate through the input array `nums`. For each number, calculate its complement (the number needed to reach the target) as `target - num`.
- If the complement is already in `nums_dict`, return an array containing the indices of the complement and the current number.
- If the complement is not in `nums_dict`, add the current number to the dict.
- If no solution is found, return an empty array.

</details>

### Test Cases

```python
from two_sum import two_sum


def test_two_sum_1():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    assert set(result) == {0, 1}


def test_two_sum_2():
    nums = [3, 2, 4]
    target = 6
    result = two_sum(nums, target)
    assert set(result) == {1, 2}


def test_two_sum_3():
    nums = [3, 3]
    target = 6
    result = two_sum(nums, target)
    assert set(result) == {0, 1}
```
