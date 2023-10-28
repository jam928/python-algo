Write a function called `find_max_number` that takes in an array of numbers and returns the largest number in the array.

### Function Signature

```python
def find_max_number(arr):
    """
    Returns the largest number in an array.
    
    :param arr: List of numbers.
    :type arr: List[int]
    :return: The largest number in the array.
    :rtype: int
    """
```

### Examples

```python
find_max_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # 10
find_max_number([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) # 10
find_max_number([1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) #  10
```

### Hints

- There is a very easy way to do this using a specific built-in method. I would suggest not doing it that way. Try to solve this problem using a `for` loop.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

This is the easy way to do it. There is a method called `Math.max()` that will return the largest number in an array. This is not the way I would suggest doing it, but it is good to know that this method exists.

```python
def find_max_number(arr) {
  return max(*arr);
}
```

### Explanation

There is not too much explanation needed here.

</details>

<details>
  <summary>Click For Solution 2</summary>

Here is another way of solving it using a `for` loop.

```python
def find_max_number(arr):
    max = float('-inf')

    for e in arr:
        if e > max:
            max = e

    return max
```

### Explanation

- Create a variable called `max` and setting it equal to the first element in the array.
- Loop through the array starting at the second element.
- Check if the current element is greater than the current value of `max`. If it is, we set `max` equal to the current element.
- Return `max` after the loop is finished.

</details>

### Test Cases

```python
import find_max_number
import pytest
def test_find_max_number_in_array():
  assert find_max_number.find_max([1, 5, 3, 9, 2]) == 9
  assert find_max_number.find_max([0, -1, -5, 2]) == 2
  assert find_max_number.find_max([10, 10, 10, 10]) == 10
```
