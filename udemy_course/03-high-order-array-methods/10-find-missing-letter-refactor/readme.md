# Challenge: Find Missing Letter Refactor

## Instructions

In the last section, we created a function called`find_missing_letter` that takes in an array of consecutive (increasing) letters as input and returns the missing letter in the array.

I want to do that same thing using high order array methods. It is possible to do it using `map`, `filter`, `reduce`, or `forEach`.

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
find_missing_letter(['a', 'b', 'c', 'd', 'f']) # => "e"
find_missing_letter(['O', 'Q', 'R', 'S']) # => "P"
find_missing_letter(['t', 'u', 'v', 'w', 'x', 'z']) # => "y"
```

### Constraints

- The input array will always contain at least two letters
- The input array will only contain letters in one case (lower or upper)
- Use only high order array methods. No for loops allowed.

### Hints

- You can use `map` to get an array of the unicode numbers (using charCodeAt) of the letters in the input array and then use `find` to find the missing character code.
- You can also use `filter` as well as `reduce`

## Solutions

<details>
  <summary>Click For Solution 1 </summary>

This solution uses the `map` and `find` methods.

```python
def find_missing_letter(arr):
    # create a list of char codes for each letter in the array
    char_codes = [ord(letter) for letter in arr]

    # find the missing letter using list comprehension return the current character plus one;
    # if the char code of the next one difference with the current char is greater than 1
    missing_letter = next((chr(char_codes[i] + 1) for i in range(len(char_codes)) if char_codes[i+1] - char_codes[i] > 1), "")

    return missing_letter
```

### Explanation

- create variable called `char_codes` and use list comprehensions to store the ascii code of each character using ord(letter)
- to find the missing letter
  - find the first that meets the below condition
    - iterate the `char_codes` array and if the char codes at i+1 and the current char code numeric values is greater than 1 
      - return the chr char codes i + 1
    - otherwise if no value found return an empty string

</details>

### Test Cases

```python
import find_missing_letter_refactor as f


def test_find_missing_letter():
    assert f.find_missing_letter(['a', 'b', 'c', 'e']) == 'd'
    assert f.find_missing_letter(['X', 'Z']) == 'Y'
    assert f.find_missing_letter(['m', 'n', 'o', 'q', 'r']) == 'p'
    assert f.find_missing_letter(['F', 'G', 'H', 'J']) == 'I'

```
