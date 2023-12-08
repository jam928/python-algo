# Challenge: Valid Anagrams

## Instructions

Write a function called `valid_anagrams` that takes in two strings and determines whether they are valid anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Function Signature

```python
def valid_anagrams(str1: str, str2: str) -> bool:
    """
    Determines whether two strings are valid anagrams.
    :param str1: The first string.
    :type str1: str
    :param str2: The second string.
    :type str2: str
    :return: True if the strings are valid anagrams, False otherwise.
    :rtype: bool
    """
    # Implementation of the function goes here

```

### Examples

```python
valid_anagrams('listen', 'silent') # true
valid_anagrams('hello', 'world') # false
valid_anagrams('astronomer', 'moonstarer') # true
```

### Hints

- Split the strings into arrays of characters, then reduce each array into an object of character frequencies for the strings
- Compare the frequencies

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def valid_anagrams(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    freq_count_map = {}

    for c in str1:
        freq_count_map.update({c: freq_count_map.get(c, 0) + 1})

    for c in str2:
        if c not in freq_count_map:
            return False
        freq_count_map.update({c: freq_count_map.get(c) - 1})

        if freq_count_map.get(c) == 0:
            freq_count_map.pop(c)

    return len(freq_count_map) == 0
```

</details>

### Test Cases

```python
import valid_anagrams as v


def test_valid_anagrams():
    assert v.valid_anagrams('listen', 'silent') is True
    assert v.valid_anagrams('hello', 'world') is False
    assert v.valid_anagrams('astronomer', 'moonstarer') is True
    assert v.valid_anagrams('apple', 'banana') is False
```
