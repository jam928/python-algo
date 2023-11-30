# Challenge: Array Intersection

## Instructions

Write a function called `array_intersection` that takes in two arrays and returns an array containing the intersection of the two input arrays (i.e., the common elements that appear in both arrays).

### Function Signature

```python
from typing import List

def array_intersection(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Returns the intersection of two arrays.
    
    Parameters:
    - arr1 (List[int]): The first array.
    - arr2 (List[int]): The second array.
    
    Returns:
    - List[int]: The intersection of the two arrays.
    """
    # Your function logic here
    pass
```

### Examples

```python
array_intersection([1, 2, 3, 4, 5], [1, 3, 5, 7, 9]); # should return [1, 3, 5]
array_intersection([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]); # should return []
array_intersection([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]); # should return [1, 2, 3, 4, 5]
```

### Constraints

- The input arrays can contain any number of elements
- The input arrays can contain any positive integer

### Hints

- You could use a for loop to iterate through the first array and check if each element is in the second array using the `includes` method.
- You could also take the approach of using a Set to store the elements of the first array and then iterate through the second array and check if each element is in the Set using the `has` method.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

```python
def array_intersection(arr1, arr2):
    intersection = []

    for element in arr1:
        if element in arr2 and element not in intersection:
            intersection.append(element)

    return intersection
```

### Explanation

- Iterate through the first array
- For each element, check if it is in the second array using the `includes` method
- If it is, check if it is already in the intersection array using the `includes` method
- If it is not, push it into the intersection array
- Return the intersection array

Time: O(n+m)
Space: O(1)
</details>

<details>
  <summary>Click For Solution 2</summary>

In this solution, we will use a Set. A Set is a data structure that stores unique values. We will have a section on maps, sets later. If you are not familiar with sets, that is fine. You can still follow along with this solution.

```python
def array_intersection(arr1, arr2):
    s = set()

    for e in arr1:
        s.add(e)

    intersection_arr = []

    for e in arr2:
        if e in s:
            intersection_arr.append(e)

    return intersection_arr
```

### Explanation

- Create a new Set from the first array
- Iterate through the second array and check if each element is in the set using the in keyword
- If it is, push it into the intersection array
- Return the intersection array


Time: O(n + m)
Space: O(n + min(n, m))
</details>

### Test Cases

```python
import array_intersection as ai

def test_array_intersection():
  assert ai.array_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3,4,5]
  assert ai.array_intersection([10, 20, 30], [30, 40, 50]) == [30]
  assert ai.array_intersection([1, 2, 3], [4, 5, 6]) == []
```
