# Challenge: Reverse String Recursion

## Instructions

Write a function called `reverse_string` that takes in a string and returns the reversed version of the string. Be sure to use recursion in your solution.

### Function Signature

```python
def reverse_string(s: str) -> str:
    """
    Returns the reverse of a string.
    
    Args:
    - s (str): The string to reverse.

    Returns:
    - str: The reverse of the string.
    """
```

## Examples

```python
reverse_string('hello') # should return 'olleh'
reverse_string('world') # should return 'dlrow'
reverse_string('') # should return ''
reverse_string('a') # should return 'a'
reverse_string('racecar') # should return 'racecar'
```

### Hints

- As a base case, you can check if the string is empty and return an empty string if so.
- You can use recursion to reverse the string by recursively calling the function with the substring starting from the second character and then concatenating the first character at the end.
- Remember how unwinding works and how function returns are added to the call stack in the reverse order of the function calls.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def reverse_string(s):
    # Base case - if s is empty, return empty string
    if s == '':
        return ''

    # Recursive case - return the last character of s and call reverse_string again
    return reverse_string(s[1:]) + s[0]
```

### Explanation

The `reverseString` function uses recursion to reverse the string.

- If the input string is empty (`str === ''`), return an empty string (`''`). Otherwise, it calls itself with the substring starting from the second character (`str.substr(1)`) and concatenates the first character of the original string at the end (`str[0]`).

For example, if the input is `'hello'`, the function first calls itself with `'ello'` and concatenates `'h'` at the end. Then it calls itself with `'llo'` and concatenates `'e'` at the end. This process continues until the input becomes an empty string, and then the function starts concatenating the characters in reverse order, resulting in the reversed string `'olleh'`.

It is important to have that base case of an empty string, otherwise the function will continue to call itself with substrings of the original string until it runs out of memory and crashes.

#### More Explanation

Let's break it down a little more...

1. When we call reverseString('hello'), it executes reverseString('ello') + 'h'.
2. Now, reverseString('ello') calls reverseString('llo') + 'e'.
3. Continuing, reverseString('llo') calls reverseString('lo') + 'l'.
4. In the next call, reverseString('lo') calls reverseString('o') + 'l'.
5. Finally, reverseString('o') returns 'o'.

Now, we can start "unwinding" the recursion and concatenating the characters to form the reversed string:

1. 'o' + 'l' gives 'ol'.
2. 'ol' + 'l' gives 'oll'.
3. 'oll' + 'e' gives 'olle'.
4. 'olle' + 'h' gives 'olleh'.

So, the function concatenates the characters in reverse order as it "unwinds" the recursion, effectively reversing the original string.

We could even cut this solution down to a single line:

```python
def reverse_string_2(s):
    return '' if s == '' else reverse_string(s[1:]) + s[0]
```

</details>

### Test Cases

```python
import reverse_string_recursion as r


def test_reverse_a_string():
    assert r.reverse_string("Hello") == 'olleH'
    assert r.reverse_string("JavaScript") == 'tpircSavaJ'
    assert r.reverse_string("12345") == '54321'

```
