# Challenge: Count Occurrences


## Instructions

Write a function called `count_occurrences()` that takes in a string and a character and returns the number of occurrences of that character in the string.

### Function Signature

```python
def count_occurrences(str: str, char: str) -> int:
    """
    Returns the number of occurrences of a character in a string.

    Parameters:
    - str (str): The string to search.
    - char (str): The character to search for.

    Returns:
    - int: The number of occurrences of the character in the string.
    """
```

### Examples

```python
count_occurrences('hello', 'l') # 2
count_occurrences('hello', 'z') # 0
```

### Constraints

- Lowercase and uppercase characters are considered different characters. If you want, you can make the function case insensitive

### Hints

- You can loop through a string just like you can loop through an array.
- You can use the `++` operator to increment a variable.
- You could take another approach and use the `split()` method to split the string into an array of substrings based on the given character.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

```python
def count(word, letter):
    letter_count = 0

    for c in word:
        if c == letter:
            letter_count += 1

    return letter_count
```

### Explanation

- Initialize a `count` variable to 0.

- Iterate through the string and check if the current character is equal to the character we're looking for. If it is, we increment the `count` variable.

- After the loop, we return the `count` variable.

- To make the function case insensitive, we can convert the string and character to lowercase before looping through the string.

</details>

<details>
  <summary>Click For Solution 2</summary>

```python
def count_2(word, letter):
    return len(word.split(letter)) - 1
```

### Explanation

- Utilize the split method of the string to split it into an array of substrings based on the given character.

- Since splitting the string removes the character, the resulting array will have one less element than the number of occurrences of the character. Therefore, we can simply subtract 1 from the length of the array to get the count of occurrences.

This solution may be prettier, but it actually is not as efficient as the loop. The for loop solution directly counts the occurrences while iterating through the string, whereas the split solution involves splitting the string into an array and performing additional operations. The difference is negligible, but it is still good to be aware of.

</details>

### Test Cases

```python
import count_occurrences


def test_count_occurrences_of_a_character():
    assert count_occurrences.count("hello", "l") == 2
    assert count_occurrences.count("programming", "m") == 2
    assert count_occurrences.count("banana", "a") == 3

```
