# Challenge: Title Case

## Instructions

Write a function called `title_case` that takes in a string and returns the string with the first letter of each word capitalized.

### Function Signature

```python
def title_case(s: str) -> str:
    """
    Returns a string with the first letter of each word capitalized.
    
    :param s: The string to capitalize.
    :type s: str
    :return: The string with the first letter of each word capitalized.
    :rtype: str
    """
```

### Examples

```python
title_case("I'm a little tea pot"); # I'm A Little Tea Pot
title_case('sHoRt AnD sToUt'); # Short And Stout
title_case('HERE IS MY HANDLE HERE IS MY SPOUT'); # Here Is My Handle Here Is My Spout
```

### Constraints

- You may assume that each word consists of only letters and spaces

### Hints

## Solutions

<details>
  <summary>Click For Solution 1</summary>

```python
def title_case(str):
  words = str.lower().split(' ')

  for i, character in enumerate(words):
    words[i] = words[i][0].upper() + words[i][1:]

  return ' '.join(words)

```

### Explanation

- Split the string into an array of words and put them all in lowercase.
- Iterate through the array and capitalize the first letter of each word by using the 0 index of the word and concatenating it with the rest of the word.
- Join the array back into a string and return it.

</details>

### Test Cases

```python
import title_case as tc
import pytest


def test_converting_string_to_title_case():
    assert tc.title_case("hello world") == 'Hello World'
    assert tc.title_case("javascript programming") == 'Javascript Programming'
    assert tc.title_case("openai chatbot") == 'Openai Chatbot'
    assert tc.title_case("I'm a little tea pot") == "I'm A Little Tea Pot"
    assert tc.title_case("sHoRt AnD sToUt") == "SHoRt AnD SToUt"
    assert tc.title_case("HERE IS MY HANDLE HERE IS MY SPOUT") == 'HERE IS MY HANDLE HERE IS MY SPOUT'
```
