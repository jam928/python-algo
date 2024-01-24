# Challenge: Symmetric Difference Challenge

## Instructions

We'll start with a pretty simple challenge. Write a function called `symmetric_difference` that takes in two arrays and returns an array containing the symmetric difference of the two arrays. The symmetric difference of two arrays is a new array containing only the elements that are present in one of the arrays but not both, with no duplicates.

### Function Signature

```python
from typing import List

def symmetric_difference(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Returns a list containing the symmetric difference of two lists.
    
    Parameters:
    - arr1 (List[int]): The first list of integers.
    - arr2 (List[int]): The second list of integers.
    
    Returns:
    - List[int]: The list containing the symmetric difference of the two lists.
    """
    # Your function implementation goes here
    pass  # Placeholder for function body
```

### Examples

```python
symmetric_difference([1, 2, 3], [3, 4, 5])
# Output: [1, 2, 4, 5]

symmetric_difference([1, 2, 2, 3, 4], [2, 3, 3, 4, 5])
# Output: [1, 5]

symmetric_difference([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
# Output: []

symmetric_difference([1, 2, 3], [4, 5, 6])
# Output: [1, 2, 3, 4, 5, 6]
```

### Hints

- You can use two Sets to keep track of elements in both arrays and then find the elements that are present in only one of the sets.
- Be mindful of duplicate elements and handle them appropriately.

## Solutions

<details>
  <summary>Click For Solution</summary>

```js
from typing import List


def symmetric_difference(arr1: List[int], arr2: List[int]) -> List[int]:
    # Store the elements of arr1 and arr2 in set
    arr1_set = set(arr1)
    arr2_set = set(arr2)

    # Iterate thru elements of list1 and list2 and if the element is not in set then add to result array
    result = []

    for e in arr1:
        if e not in arr2_set:
            result.append(e)

    for e in arr2:
        if e not in arr1_set:
            result.append(e)

    return result
```

### Explanation

- To find the symmetric difference, create two `Set` objects, `set1` and `set2`, from `arr1` and `arr2` respectively. The `Set` data structure allows us to efficiently check for the existence of an element.
- Initialize an empty array called `result` to store the symmetric difference.
- Iterate through each element in `arr1` using a `for...of` loop. For each element in `arr1`, we use the `has()` method of `set2` to check if the element exists in `set2`. If the element is not found in `set2`, it means it is present in `arr1` but not in `arr2`, and push it into the `result` array.
- Similarly, iterate through each element in `arr2` using another `for...of` loop. For each element in `arr2`, we use the `has()` method of `set1` to check if the element exists in `set1`. If the element is not found in `set1`, it means it is present in `arr2` but not in `arr1`, and push it into the `result` array.
- Return the `result` array, which contains the elements that are present in only one of the input arrays, with no duplicates.

</details>

### Test Cases

```python
from symmetric_difference import symmetric_difference

def test_symmetric_difference():
    assert symmetric_difference([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
    assert symmetric_difference([1, 2, 2, 3, 4], [2, 3, 3, 4, 5]) == [1, 5]
    assert symmetric_difference([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == []
    assert symmetric_difference([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
```
