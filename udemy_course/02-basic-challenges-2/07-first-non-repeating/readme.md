# Challenge: Find First Non-Repeating Character

This challenge is similar to the last. So if you understood that, you should be able to get this one on your own.

## Instructions

Write a function called `find_first_non_repeating_character` that takes in a string and returns the first non-repeating character in the string.

If there are no non-repeating characters, the function should return `null`.

### Function Signature

```python
def find_first_non_repeating_character(s):
    """
    Returns the first non-repeating character in a string.
    :param s: The string to search.
    :type s: str
    :return: The first non-repeating character in the string or None if there are no non-repeating characters.
    :rtype: str or None
    """
    # Your implementation here to find the first non-repeating character in the string
```

### Examples

```python
find_first_non_repeating_character('aabccdeff'); # should return 'b'
find_first_non_repeating_character('aabbcc'); # should return null
find_first_non_repeating_character('abcdef'); # should return 'a'
```

### Constraints

- The input string will only contain lowercase letters and spaces

### Hints

- You can use an object or a map to keep track of the number of times each character appears in the string.
- You can iterate through the string and check if the current character has only appeared once.

## Solutions

<details>
  <summary>Click For Solution 1 </summary>

Using a `Map`:

```python
def find_first_non_repeating_character(s):
    freq_count_map = {}

    for c in s:
        freq_count_map.update({c: freq_count_map.get(c, 0) + 1})

    for c in s:
        if freq_count_map.get(c) == 1:
            return c

    return None
```

### Explanation

- Initialize a map to keep track of the number of times each character appears in the string.
- Iterate through the string and add each character to the map. If the character is already in the map, we increment its count by 1. If it isn't, we set its count to 1.
- Iterate through the string again and check the map to see if the current character has a count of 1. If it does, we return it because it's the first non-repeating character.
- If we make it through the entire string without returning a character, we return null because there are no non-repeating characters.

</details>


### Test Cases

```python
import first_non_repeating as fnr


def test_find_first_non_repeating_character():
    assert fnr.find_first_non_repeating_character("aabccdeff") == "b"
    assert fnr.find_first_non_repeating_character("aabbcc") is None
    assert fnr.find_first_non_repeating_character("hello world") == "h"

```
