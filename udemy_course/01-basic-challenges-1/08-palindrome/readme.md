# Challenge: Palindrome

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. An example of a palindrome is "madam".

## Instructions

Write a function called `is_palindrome` that takes in a string and returns `true` if the string is a palindrome and `false` if it is not.

### Function Signature

```python
/**
 * Returns true if the string is a palindrome.
 * @param {string} str - The string to check.
 * @returns {boolean} - True if the string is a palindrome, false otherwise.
 */
function isPalindrome(str: string): boolean;

def is_palindrome(str: str) -> boolean:
    """
    Returns true if the string is a palindrome.
    
    Parameters:
    - str (str): The string to check.
    
    Returns:
    - boolean: True if the string is a palindrome, false otherwise.
    """
```

### Examples

```python
is_palindrome('madam') # true
is_palindrome('racecar') # true
is_palindrome('hello') # false
is_palindrome('') # true
```

### Constraints

- The input string will only contain lowercase letters and spaces
- The function should ignore spaces when checking if the string is a palindrome

### Hints

- You can solve this in a way that is similar to the reverse string challenge with some added steps.
- Remember, you want to remove any non-alphanumeric characters from the string before comparing it to the reversed string. There are multiple ways to do this, but one way is to use the `replace` method with a regular expression of `/[^a-z0-9]/g`.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

Using `replace` with a regular expression is the easiest way to solve this challenge.

```python
def is_palindrome(s):
    formatted_str = ''.join(c.lower() for c in s if c.isalnum())
    reversed_str = formatted_str[::-1]
    return formatted_str == reversed_str
```

### Explanation

- Take the input string and sanize the string by keeping the characters that are alphanumeric
- join by ''
- get the reverse string of the santize string
- compare both and if they are equal return true otherwise return false
</details>

### Test Cases

```python
import palindrome as pd


def test_palindrome_strings():
    assert pd.is_palindrome("racecar") is True
    assert pd.is_palindrome("Hello") is False
    assert pd.is_palindrome("A man, a plan, a canal, Panama") is True
    assert pd.is_palindrome("12321") is True

```
