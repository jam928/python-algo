# Challenge: Hello World Sample Challenge

This is a practice challenge to show you how things are set up and how to test, etc.

## Instructions

Write a function called `hello_world` that returns a string of 'Hello World!'.

### Function Signature

```python
def hello_world() -> str:
    """
    Returns a string containing 'Hello World!

    Returns:
    - str: The string 'Hello World!'
    """
hello_world() # 'Hello World!'
```

### Constraints

I will put any constraints here. They will vary depending on the challenge.

- The function must return a string

### Hints

- I will put a couple hints here. You can choose to use them or not.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def hello_world():
    return 'Hello World!'
```

### Explanation

I will put the explanation to the solution here. The length and depth of the explanation will vary depending on the challenge.

</details>

### Test Cases

Py test run it in pycharm.

```python
import hello_world
def test_return_hello_world_as_a_string():
    result = hello_world.hello_world()
    assert result == 'Hello World!'
```
