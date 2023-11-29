# Challenge: Remove Duplicates

## Instructions

Write a function called `remove_duplicates` that takes in an array and returns a new array with duplicates removed.

### Function Signature

```python
def remove_duplicates(arr: []) -> []:
    """
    Returns a new array with duplicates removed.
    
    Parameters:
    - [] (any[]): The array to remove duplicates from.
    
    Returns:
    - any[]: The new array with duplicates removed.
    """
```


### Examples

```python
remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) # [1]
remove_duplicates([1, 2, 3, 4, 5, true, 1, 'hello' 2, 3, 'hello', true]) # [1, 2, 3, 4, 5, true, 'hello']
```

### Constraints

- The array can contain any data type

### Hints

- You can do this with a traditional 'for' loop, but if you are familiar with the `Set` object, you can use that to solve this problem. Maybe try both ways!

## Solutions

<details>
  <summary>Click For Solution 1</summary>

Using a for loop

```python
def remove_duplicates(arr):
    unique_arr = []

    s = set()
    boolean_set = set()

    for e in arr:
        if isinstance(e, bool) and e not in boolean_set:
            boolean_set.add(e)
            unique_arr.append(e)
        elif not isinstance(e, bool) and e not in s:
            unique_arr.append(e)
            s.add(e)

    return unique_arr
```

### Explanation

- Create a new array called `unique_arr`.
- Create two sets
  - One for boolean values since boolean values is stored as 1 and 0s in python
  - and the other set for the rest of the elements
- Create a `for` loop that will loop through each element in the array.
  - If the element is a boolean and hasn't been added to the boolean set
    - add to the boolean set
    - add to the new array
  - else if the element is not a boolean and the element is not in the set
    - add it to the array
    - add to the other set
- Once we have looped through the entire array, we return `unique_arr`.

</details>

### Test Cases

```python
import remove_duplicates as rd


def test_remove_duplicates_from_array():
    assert rd.remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
    assert rd.remove_duplicates(['apple', 'banana', 'orange', 'banana', 'kiwi']) == ['apple', 'banana', 'orange',
                                                                                     'kiwi']
    assert rd.remove_duplicates([True, True, False, True, False]) == [True, False]

```
