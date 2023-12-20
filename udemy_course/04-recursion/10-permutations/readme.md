# Challenge: Permutations

## Instructions

Write a function called `permutations` that takes in a string as a parameter and returns an array of all possible permutations of the characters in the string.

### Function Signature

```python
from typing import List

def permutations(str_: str) -> List[str]:
    """
    Returns all possible permutations of the characters in a string.

    Parameters:
        str_ (str): The string to permute.

    Returns:
        List[str]: A list of all possible permutations of the characters in the string.
    """
    # Function implementation goes here
```

### Examples

```python
permutations('abc')#  ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
permutations('dog')#  ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']
```

### Constraints

- The input string will only contain lowercase letters
- The input string will not contain any duplicate characters

### Hints

- Think about how you can break down the problem of generating permutations using recursion.
- Consider what the base case for your recursion should be.
- You can use the `slice` method to remove a character from a string.
- you can use a for loop to iterate over the characters in the string and another for loop to iterate over the sub-permutations.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def permutations(s):
    # Create a list to store the permutations
    result = []

    # If s is an empty string, append an empty string to result and return
    if len(s) == 0:
        result.append('')
        return result

    # Loop through each character in s
    for i in range(len(s)):
        # Get the first character
        first_char = s[i]
        # Get the rest of the string
        rest_of_string = s[:i] + s[i + 1:]
        # Get the permutations of the rest of the string
        sub_permutations = permutations(rest_of_string)

        # Loop through each permutation in sub_permutations
        for j in range(len(sub_permutations)):
            # Append the first character and the permutation to result
            result.append(first_char + sub_permutations[j])

    # Return result
    return result
```

### Explanation

- Intialize an empty array result to store the permutations.
- The base case is checked at the beginning. If the input string str is empty (length is 0), it means there are no characters to permute. In this case, an empty string is added to the result array, representing the only permutation for an empty string. The function then returns the result array.
- If the input string is not empty, the function proceeds to generate permutations using recursion and a loop.
- The outer loop iterates through each character of the input string str.
- Inside the loop, it extracts the current character (firstChar) from the input string.
- Create the restOfString by removing the current character from the input string. This restOfString will be used for generating permutations of the remaining characters.
- The function recursively calls itself with the restOfString to get all possible permutations of the remaining characters.
- The inner loop iterates through each permutation obtained from the recursive call (subPermutations).
- In the inner loop, the function appends the current character firstChar to each permutation obtained from the recursive call. This creates new permutations by inserting the current character in different positions.
- The new permutations are added to the result array.
- After the outer loop finishes, the function has generated all possible permutations of the input string.
- Finally, the result array containing all permutations is returned as the output of the function.

</details>

### Test Cases

```python
from permutations import permutations


def test_permutations():
    assert permutations('abc') == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert permutations('dog') == ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']
    assert permutations('') == ['']
```
