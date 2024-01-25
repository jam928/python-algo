# Challenge: Longest Consecutive Sequence

## Instructions

Write a function called `longest_consecutive_sequence` that takes an array of integers as input and returns the length of the longest consecutive sequence of integers in the array.

A consecutive sequence is a sequence of consecutive integers, meaning each integer in the sequence is exactly one more than the previous integer.

### Function Signature

```python
def longest_consecutive_sequence(nums):
    """
    Returns the length of the longest consecutive sequence in the array.
    :param nums: List of integers.
    :return: The length of the longest consecutive sequence.
    """
    # Your implementation goes here
    pass
```

### Examples

```python
longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) # Output: 4 (The longest consecutive sequence is [1, 2, 3, 4])
longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 9, 1]) # Output: 10 (The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### Constraints

- The input array will contain only integers
- The input array may contain duplicate integers

### Hints

- You can use a Set to efficiently find consecutive sequences in the array.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def longest_consecutive_sequence(nums):
    # Create new set
    num_set = set(nums)
    # Create longest sequence variable
    longest_sequence = 0

    # Loop through set
    for num in num_set:
        # If set does not have num - 1, identify the starting element of a potential consecutive sequence.
        if num - 1 not in num_set:
            # Create current num and current sequence variables
            current_num = num
            current_sequence = 1

            # While set has current num + 1, is the next consecutive number in the set?
            while current_num + 1 in num_set:
                # Increment current num and current sequence
                current_num += 1
                current_sequence += 1

            # Set longest sequence to the max of longest sequence and current sequence
            longest_sequence = max(longest_sequence, current_sequence)

    # Return longest sequence
    return longest_sequence
```

### Explanation

- Create a Set called `numSet` from the input array `nums`. The Set will allow us to efficiently check if an integer exists in the array in constant time.
- Initialize a variable `longestSequence` to 0, which will store the length of the longest consecutive sequence found so far.
- Iterate through each integer `num` in the `numSet` using a `for...of` loop. For each integer, check if its previous integer `num - 1` exists in the `numSet`. If `num - 1` is not present, it means that `num` is the starting element of a consecutive sequence.
- Initialize two variables `currentNum` and `currentSequence`. `currentNum` is set to the current integer `num`, and `currentSequence` is set to 1, as we have found the first element of a consecutive sequence.
- Use a `while` loop to iterate as long as the next integer `currentNum + 1` exists in the `numSet`. For each iteration, increment `currentNum` and `currentSequence` to extend the consecutive sequence.
- After the `while` loop ends, update `longestSequence` to the maximum value between the current `longestSequence` and `currentSequence`. This way, we keep track of the longest consecutive sequence found so far.
- After the loop finishes, return `longestSequence` as the final output, which represents the length of the longest consecutive sequence in the input array.

</details>

### Test Cases

```python
from longest_consecutive import longest_consecutive_sequence


def test_longest_consecutive_sequence():
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 9, 1]) == 10
```

**Note**: You need to define the `longestConsecutiveSequence` function as shown in the example. The test cases verify that the function correctly returns the length of the longest consecutive sequence in the input array.
