# Challenge: Display Likes

## Instructions

Write a function called `display_likes` that takes in an array of names and returns a string of who likes the post.

The function should return a string formatted as follows:

- If no one likes it, it should return `'no one likes this'`
- If one person likes it, it should return `'{name} likes this'`
- If two people like it, it should return `'{name1} and {name2} like this'`
- If three people like it, it should return `'{name1}, {name2} and {name3} like this'`
- If more than three people like it, it should return `'{name1}, {name2} and {x} others like this'`

### Function Signature

```python
def display_likes(names: list[str]) -> str:
    """
    Returns a string of who likes the post.

    Parameters:
    - names (list[str]): The names of the people who like the post.

    Returns:
    - str: A string of who likes the post.
    """
    # Your function implementation goes here
```

### Examples

```python
display_likes([]) # 'no one likes this'
display_likes(['Peter']) # 'Peter likes this'
display_likes(['Jacob', 'Alex']) # 'Jacob and Alex like this'
display_likes(['Max', 'John', 'Mark']) # 'Max, John and Mark like this'
display_likes(['Alex', 'Jacob', 'Mark', 'Max']) # 'Alex, Jacob and 2 others like this'
display_likes(['Alex', 'Jacob', 'Mark', 'Max', 'Jill']) # 'Alex, Jacob and 3 others like this'
```

### Constraints

- The input array will only contain strings

### Hints

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def display_likes(names):
    length_of_names = len(names)
    if length_of_names == 0:
        return "no one likes this"
    elif 1 == length_of_names:
        return f"{names[0]} likes this"
    elif 2 == length_of_names:
        return f"{names[0]} and {names[1]} like this"
    elif 3 == length_of_names:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {length_of_names - 2} others like this"
```

### Explanation

This is pretty simple as it just requires a bunch of if statements. We could also use a switch statement here, but it would be a bit more verbose.

- Get the length of the array and then check if it's 0, 1, 2, 3, or more. Depending on the length, we return the appropriate string.
- If there are more than 3 names, we return the first two names, and then the length minus 2 for the number of others.

</details>

### Test Cases

```python
import display_likes as dl


def test_display_likes():
    assert dl.display_likes([]) == 'no one likes this'
    assert dl.display_likes(['Peter']) == 'Peter likes this'
    assert dl.display_likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert dl.display_likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'
    assert dl.display_likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'
    assert dl.display_likes(['Alex', 'Jacob', 'Mark', 'Max', 'Jill']) == 'Alex, Jacob and 3 others like this'
});
```
