# Challenge: Are all characters unique?

## Instructions

Write a function called `are_all_characters_unique` that takes in a string and returns `true` or `false` depending on whether all characters in the string are unique (i.e., no character is repeated).

### Function Signature

```python
def are_all_characters_unique(s):
    """
    Returns True if all characters in a string are unique.
    :param s: The string to check.
    :type s: str
    :return: Whether all characters in the string are unique.
    :rtype: bool
    """
```

### Examples

```python
are_all_characters_unique('abcdefg') # true
are_all_characters_unique('abcdefgA') # true
are_all_characters_unique('programming') # false
are_all_characters_unique('') # true
are_all_characters_unique('a') # true
```

### Constraints

- It should be case sensitive, so `a` and `A` are considered different characters
- An empty string should return `true` by default

### Hints

- You can use a for loop to iterate through the string and check if the current character is in the set or object.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

Using a `Set`:

```python
def are_all_characters_unique(s):
  """
  Returns True if all characters in a string are unique.
  :param s: The string to check.
  :type s: str
  :return: Whether all characters in the string are unique.
  :rtype: bool
  """
  # Create a new set
  char_set = set()

  # Loop through the string
  for char in s:
    # If the set already has the current character, return False
    if char in char_set:
      return False
    # Add the current character to the set
    char_set.add(char)

  # If no characters are repeated, return True
  return True
```

### Explanation

-Initialize a new `Set` to keep track of the characters we've seen so far.

- Iterate through the string and check if the current character is in the set. If it is, we return `false` because it means we've seen the character before. If it isn't, we add it to the set.
- If we make it through the entire string without returning `false`, we return `true` because it means we haven't seen any characters more than once.

</details>

<details>
  <summary>Click For Solution 2</summary>

Using an object:

```python
def are_all_characters_unique_2(s):
  """
  Returns True if all characters in a string are unique.
  :param s: The string to check.
  :type s: str
  :return: Whether all characters in the string are unique.
  :rtype: bool
  """
  # Create a dictionary to keep track of the characters in the string
  char_count = {}

  # Loop through the string
  for char in s:
    # If the character is already in the dictionary, return False
    if char_count.get(char):
      return False
    # Add the current
    char_count.update({char: True})
    
  return True
```

### Explanation

This solution is similar except we use an object instead of a `Set` to keep track of the characters we've seen so far.

Then we iterate through the string and check if the current character is in the object. If it is, we return `false` because it means we've seen the character before. If it isn't, we add it to the object.

If we make it through the entire string without returning `false`, we return `true` because it means we haven't seen any characters more than once.

</details>

### Test Cases

```python
import are_all_characters_unique as char_unique


def test_unique_characters_in_a_string():
    assert char_unique.are_all_characters_unique('abcdefg') is True
    assert char_unique.are_all_characters_unique('abcdefgA') is True
    assert char_unique.are_all_characters_unique('programming') is False
    assert char_unique.are_all_characters_unique('') is True
    assert char_unique.are_all_characters_unique('a') is True

```
