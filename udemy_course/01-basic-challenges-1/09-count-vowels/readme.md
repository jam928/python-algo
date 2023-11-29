# Challenge: Count Vowels

## Instructions

Write a function called `count_vowels` that takes in a string and returns the number of vowels in the string.

### Function Signature

```python
def count_vowels(str: str) -> int:
    """
    Returns the number of vowels in a string.
    
    Parameters:
    - str (str): The string to check.
    
    Returns:
    - int: The number of vowels in the string.
    """
```

### Examples

```python
count_vowels('hello') # 2
count_vowels('why') # 0
count_vowels('mississippi') # 4
```

### Constraints

- It shouldn't matter if the input string is uppercase or lowercase

### Hints


## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def count_vowels(s):
    vowel_str = "aeiouAEIOU"
    s = s.lower()
    vowel_count = 0
    for c in s:
        if c in vowel_str:
            vowel_count = vowel_count + 1

    return vowel_count
```

## Explanation

- Make the string lowercase. This is because we want to count both uppercase and lowercase vowels.
- Create a variable called `vowel_count` and set it to `0`. This is the variable we will use to keep track of how many vowels we have found.
- Create a `for` loop that will loop through each character in the string. 
- Check if the character in the vowel str. If it is, we increment `vowel_count` by `1`. Once we have looped through the entire string, we return `vowel_count`.

</details>

### Test Cases

```python
import count_vowels as cv

def test_count_vowels_in_str():
    assert cv.count_vowels("Hello World!") == 3
    assert cv.count_vowels("JavaScript") == 3
    assert cv.count_vowels("OpenAI Chatbot") == 6
    assert cv.count_vowels("Coding Challenge") == 5

```
