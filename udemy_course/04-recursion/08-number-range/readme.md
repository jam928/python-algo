# Challenge: Number Range Using Recursion

## Instructions

Write a function called `number_range` that takes in a `start_num` and an `end_num` and returns an array of numbers from `start_num` to `end_num`, inclusive. Be sure to use recursion in your solution.

### Function Signature

```python
def number_range(start_num: int, end_num: int) -> list[int]:
    """
    Returns an array of numbers from startNum to endNum, inclusive.

    Parameters:
        start_num (int): The starting number.
        end_num (int): The ending number.

    Returns:
        list[int]: An array of numbers.
    """
    # Function implementation goes here
```

### Examples

```python
number_range(1, 5) # should return [1, 2, 3, 4, 5]
number_range(3, 10) # should return [3, 4, 5, 6, 7, 8, 9, 10]
number_range(7, 7) # should return [7] (only one number)
```

### Hints

- You can construct the array by first calling `number_range` on a smaller range and then adding the `end_num` to the array.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def number_range(start_num: int, end_num: int) -> list[int]:
    # Check if the start_num is equal to end_num (base case)
    if start_num == end_num:
        # If they are equal, return a list containing just the start_num
        return [start_num]

    # If they are not equal, call the range_of_numbers function recursively on a smaller range
    # This creates a list of numbers from start_num to end_num - 1
    numbers = number_range(start_num, end_num - 1)

    # Append the current value of end_num to the 'numbers' list
    numbers.append(end_num)

    # Return the 'numbers' list containing all the numbers from start_num to end_num
    return numbers
```

### Explanation

- We first add our base case and check if the `start_num` is equal to the `end_num`. If so, we return the `start_num` in an array.
- For the recursive case, we set the variable `numbers` to the function with the start_num and one less than the `end_num`.
- Then we add the `end_num` to the `numbers` array and return it.

That is the gist of it, but let's go step by step for `number_range(1, 5)`

Step 1: Since `start_num(1)` is not equal to `end_num(5)`, we move to the recursive block.

Step 2: We make a recursive call to `number_range(1, 4)`, which will further call `number_range(1, 3)` and so on, until we reach the base case.

Step 3: The base case is reached when `start_num(1)` becomes equal to endNum (1). At this point, the function returns an array containing just the number 1.

Step 4: The unwinding begins. The result of `number_range(1, 2)` is now an array `[1, 2]`. Then, the result of `number_range(1, 3)` is `[1, 2, 3]`, and so on, until we finally get the result of `number_range(1, 5)` as `[1, 2, 3, 4, 5]`.

The function follows the same recursive process to build the array of numbers, starting with the base case and adding numbers one by one as it unwinds the recursive calls.

</details>

### Test Cases

```python
from number_range import number_range


def test_calculating_the_range_of_numbers():
    assert number_range(1, 5) == [1, 2, 3, 4, 5]
    assert number_range(3, 10) == [3, 4, 5, 6, 7, 8, 9, 10]
    assert number_range(7, 7) == [7]

```
