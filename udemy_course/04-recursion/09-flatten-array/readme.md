# Challenge: Flatten Array

## Instructions

Write a function called `flatten_array` that takes in an array containing nested arrays of integers and returns a new array with all the integers from the nested arrays flattened into a single level.

### Function Signature

```python
from typing import List

def flatten_array(arr: List[int]) -> List[int]:
    """
    Returns a flattened list.

    Parameters:
        arr (List[int]): The list containing nested lists.

    Returns:
        List[int]: The flattened list.
    """
    # Function implementation goes here
```

### Examples

```python
flatten_array([1, [2, 3], [4, 5, [6]]]) # should return [1, 2, 3, 4, 5, 6]
flatten_array([
  [1, 2],
  [3, [4, 5]],
  [6, [7]],
]) # should return [1, 2, 3, 4, 5, 6, 7]
flatten_array([1, [2, [3, [4, [5]]]]]) # should return [1, 2, 3, 4, 5]
```

### Constraints

- The input array can contain nested arrays of any depth
- The input array can contain any number of nested arrays

### Hints

- You can use recursion to traverse the nested arrays and flatten them.
- If the current element is an array, you can recursively call the `flattenArray` function on that element to flatten it further.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
from typing import List


def flatten_array(arr: List[int]) -> List[int]:
    def flatten_array_helper(i, arr, result):
        if len(arr) == i:
            return

        if isinstance(arr[i], list):
            flatten_array_helper(0, arr[i], result)
        else:
            result.append(arr[i])
        flatten_array_helper(i + 1, arr, result)

    result = []
    flatten_array_helper(0, arr, result)
    return result

```

### Explanation

- use a helper function passing i to iterate thru array
- if i is the length of the array return
- if the element at i is a list recursively call the flatten array
- else append the current element to the result array
- recursively go to other elements by flatten_array_helper(i + 1, arr, result)

</details>

### Test Cases

```python
from flatten_array import flatten_array


def test_flatten_nested_arrays():
    assert flatten_array([1, [2, 3], [4, 5, [6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_array([[1, 2], [3, [4, 5]], [6, [7]]]) == [1, 2, 3, 4, 5, 6, 7]
    assert flatten_array([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]

```
