# Challenge: Hashtag Generator

## Instructions

Write a function called `generate_hashtag` that takes a string as input and returns a hashtag-generated string according to the rules below. If the generated hashtag string is longer than 140 characters or the input/result is an empty string, the function should return `false`.

### Function Signature

```python
def generate_hashtag(s: str) -> Union[str, bool]:
    """
    Generates a hashtag from the input string.
    :param s: The input string.
    :type s: str
    :return: The generated hashtag string or False.
    :rtype: str or bool
    """
    # Implementation of the function goes here
```

### Examples

```python
generate_hashtag("JavaScript is awesome") # "#JavaScriptIsAwesome"
generate_hashtag("hello world") # "#HelloWorld"
generate_hashtag("This is a very very very very very very very very very very very very very very long input that should result in a false hashtag because it exceeds the character limit of 140") # false
generate_hashtag("") # false
```

### Constraints

- Return `false` if the input string is empty or contains only whitespace characters.
- Return `false` if the generated hashtag string is longer than 140 characters.
- Every word in the hashtag should start with a capital letter.
- The input string may contain leading/trailing whitespace characters.

### Hints

- You can use the string manipulation methods `trim()`, `strip()`, and `join()` to work with the input string.
- Use string methods to capitalize the first letter of each word.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

```python
def generate_hashtag(s):
  # If the string is empty or contains only whitespace characters, return False.
  if s.strip() == '':
    return False

  # Split the string into an array of words.
  words = s.strip().split()

  # Return a new list with the first letter of each word capitalized.
  capitalized_words = [word.capitalize() for word in words]

  # Join the words together into a string, prefixed with a hash.
  hashtag = '#' + ''.join(capitalized_words)

  # If the hashtag is longer than 140 characters, return False, otherwise return the hashtag.
  return False if len(hashtag) > 140 else hashtag
```

### Explanation

- Check if the input string is empty or contains only whitespace characters. If so, return `false`.
- Split the input string into an array of words using the `split()` method. The `split()` method accepts a regular expression as an argument. The regular expression `/\s+/` matches one or more whitespace characters.
- Use list comprehension to capitalize each word in words
- Join the capitalized words into a string using the `join()` method. The `join()` method accepts a string as an argument. The string is used to join the elements of the array. In this case, we want to join the elements of the array without any characters between them.
- Check if the generated hashtag string is longer than 140 characters. If so, return `false`.
- Return the generated hashtag string.

</details>

<details>
  <summary>Click For Solution 2</summary>

```python
from typing import Union

def generate_hashtag(s: str) -> Union[str, bool]:
    # Split the string into an array of words.
    # Capitalize each word in the split and then join it with a ''
    # Concat with #
    hashtag = '#' + ''.join(word.capitalize() for word in s.split())

    # If the hashtag is only one character long or longer than 140 characters, return False, otherwise return the hashtag.
    return False if len(hashtag) == 1 or len(hashtag) > 140 else hashtag

```

### Explanation

- Concat `#` with a join operation of each word that is capitalized in the string split. Join with ''
- return false if len of above string is 1(means the join operation joined with an empty string)
- return false if the length of the above word is greater than 140
- else return the above word

</details>

### Test Cases

```python
import hashtag_generator as h


def test_generating_hashtags():
    assert h.generate_hashtag(' Hello there thanks for trying my Kata') == '#HelloThereThanksForTryingMyKata'
    assert h.generate_hashtag('    Hello     World   ') == '#HelloWorld'
    assert h.generate_hashtag('') is False
    assert h.generate_hashtag('This is a very very very very very very very very very very very very very very long input that should result in a false hashtag because it exceeds the character limit of 140') is False
```
