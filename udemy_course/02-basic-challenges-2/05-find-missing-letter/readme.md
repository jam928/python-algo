# Challenge: Find Missing Letter

## Instructions

Write a function called `find_missing_letter` that takes in an array of consecutive (increasing) letters as input and returns the missing letter in the array.

### Function Signature

```python
def find_missing_letter(arr):
    """
    Returns the missing letter in an array of consecutive letters.
    :param arr: list of consecutive letters.
    :type arr: List[str]
    :return: The missing letter.
    :rtype: str
    """
    # Your implementation here to find the missing letter in the list 'arr'
```

### Examples

```python
find_missing_letter(['a', 'b', 'c', 'd', 'f']); # => "e"
find_missing_letter(['O', 'Q', 'R', 'S']); # => "P"
find_missing_letter(['t', 'u', 'v', 'w', 'x', 'z']); # => "y"
```

### Constraints

- The input array will only contain letters in one case (lower or upper)
- If no letters are in the array, return an empty string

### Hints

- You can put the alphabet in a string and use the `indexOf` method to get the index of a letter in the alphabet string.
- Another approach would be to use the `charCodeAt` method to get the unicode value of a letter. 

## Solutions

<details>
  <summary>Click For Solution 1 </summary>

```python
def find_missing_letter(arr):
  # Create a string of the alphabet
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

  # Find the index of the first letter in the array in the alphabet string
  start_index = alphabet.index(arr[0])

  # Loop through the array
  for i in range(len(arr)):
    # If the current letter in the array is not the same as the current letter in the alphabet string, return the current letter in the alphabet string
    if arr[i] != alphabet[start_index + i]:
      return alphabet[start_index + i]

  # If no letter is missing, return an empty string
  return ''
```

### Explanation

- Declare a variable `alphabet` and assign it a string of all the letters of the alphabet.
- Declare a variable `start_index` and assigned it the index of the first letter of the input array in the `alphabet` string.
- Loop through the input array and check if the current letter in the input array is not equal to the letter at the current index in the `alphabet` string.
- If it is not equal, return the letter at the current index in the `alphabet` string.
- If we get to the end of the loop without returning anything, we return an empty string.

</details>

<details>
  <summary>Click For Solution 2 </summary>

```python
def find_missing_letter_2(arr):
  # Find the char code of the first letter in the array
  start = ord(arr[0])

  # Loop through the array
  for i in range(1, len(arr)):
    # Find the char code of the current letter in the array
    current = ord(arr[i])

    # If the difference between the current char code and the start char code is greater than 1, return the letter that is missing
    if current - start > 1:
      # Convert the char code to a letter
      return chr(start + 1)

    # Update the start char code
    start = current

  # If no letter is missing, return an empty string
  return ''
```

### Explanation

- Declare a variable `start` and assigned it the ASCII code of the first letter of the input array.
- Loop through the input array and check if the ASCII code of the current letter minus the ASCII code of the previous letter is greater than 1.
- If it is, return the letter that is one greater than the previous letter.
- If we get to the end of the loop without returning anything, we return an empty string.

</details>

### Test Cases

```python
import find_missing_letter as fml


def test_find_missing_letter():
    assert fml.find_missing_letter(['a', 'b', 'c', 'e']) == 'd'
    assert fml.find_missing_letter(['X', 'Z']) == 'Y'
    assert fml.find_missing_letter(['m', 'n', 'o', 'q', 'r']) == 'p'
    assert fml.find_missing_letter(['F', 'G', 'H', 'J']) == 'I'

```
