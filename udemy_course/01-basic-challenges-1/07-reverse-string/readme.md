# Challenge: Reverse String

## Instructions

Write a function called `reverseString` that takes in a string and returns the reverse of that string. In this section, we are really focusing on loops without using any built-in methods, so try that first. If you get stuck, you can always use the built-in methods to solve the problem.

### Function Signature

```python
def reverse_string(str: str) -> str:
    """
    Returns the reverse of a string.
    
    Parameters:
    - str (str): The string to reverse.
    
    Returns:
    - str: The reverse of the string.
    """
```

### Examples

```python
reverse_string('hello') # 'olleh'
revers_string('world') # 'dlrow'
reverse_string('') # ''
```

### Constraints

- The input string will only contain lowercase letters and spaces

### Hints

- You can also do this without using any of the built-in methods and just use a for loop.
- You could also use the methods `split`, `reverse`, and `join` to solve this problem.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

This solution uses a for loop to reverse the string.

```python
def reverse_string(str):
    reverse_str = ""

    for i in range(len(str) - 1, -1, -1):
        reverse_str += str[i]

    return reverse_str
```

## Explanation

- Create a variable called `reversed` and set it equal to an empty string.
- Create a for loop that starts at the last index of `str` and decrements by 1 until it reaches 0.
- Add the character at the current index to the `reversed` variable.
- Return the `reversed` variable.

</details>

<details>
  <summary>Click For Solution 2</summary>

This solution uses built-in methods to reverse the string.

```python
def reverse_string(str):
    return str[::-1]
```

### Explanation

str: This is the string variable or literal that you want to reverse.

[::-1]: This is the slice notation. The general syntax for a slice is start:stop:step, and all three parts are optional.

In this case, start is not specified, so it defaults to the beginning of the string.

stop is not specified, so it defaults to the end of the string.

step is specified as -1, which means it will iterate the string with a step of -1, effectively reversing the string.

</details>

### Test Cases

```python
def test_reverse_string():
    assert rs.reverse_string("Hello") == 'olleH'
    assert rs.reverse_string("JavaScript") == 'tpircSavaJ'
    assert rs.reverse_string("12345") == '54321'
```
