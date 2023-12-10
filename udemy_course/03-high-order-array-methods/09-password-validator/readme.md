# Challenge: Password Validation

## Instructions

Write a function called `validate_password` that takes in a string and validates it based on the following criteria:

1. The password must be at least 8 characters long.
2. The password must contain at least one uppercase letter.
3. The password must contain at least one lowercase letter.
4. The password must contain at least one digit.

The function should return `true` if the password is valid according to the criteria, and `false` otherwise.

### Function Signature

```python
def validate_password(password: str) -> bool:
    """
    Validates a password based on certain criteria.
    :param password: The password to be validated.
    :type password: str
    :return: True if the password is valid, False otherwise.
    :rtype: bool
    """
    # Implementation of the function goes here
```

### Examples

```python
validate_password('Abc12345') # should return true
validate_password('password123') # should return false (no uppercase letter)
validate_password('Pass') # should return false (length less than 8 characters)
validate_password('HelloWorld') # should return false (no digit)
```

### Constraints

- The input password can contain any combination of letters and digits.
- The input password can contain both uppercase and lowercase letters.

### Hints

- You can use the `any` function to check the list for at least one upper, lower, and digit

## Solution

<details>
  <summary>Click For Solution</summary>

```python
def validate_password(password: str):
    is_length_valid = len(password) >= 8
    contains_lowercase_character = any(c.islower() for c in password)
    contains_uppercase_character = any(c.isupper() for c in password)
    contains_digit = any(c.isdigit() for c in password)

    return is_length_valid and contains_uppercase_character and contains_lowercase_character and contains_digit
```

### Explanation

- Create a variable called `is_length_valid` and assign it the value of `true` if the password is at least 8 characters long, and `false` otherwise.
- Create a variable called `contains_lowercase_character` and assign it the value of `true` if the password contains at least one lowercase letter, and `false` otherwise.
- Create a variable called `contains_lowercase_character` and assign it the value of `true` if the password contains at least one uppercase letter, and `false` otherwise.
- Create a variable called `contains_digit` and assign it the value of `true` if the password contains at least one digit, and `false` otherwise.
- Return the result of the expression `is_length_valid && contains_lowercase_character && contains_lowercase_character && contains_digit`.

The `any` function is used to check if at least one character in the password meets a certain condition. The `any` function takes in a callback function as an argument. The callback function is called for each character in the password. If the callback function returns `true` for at least one character, then the `any` function returns `true`. Otherwise, the `some` function returns `false`.

</details>

### Test Cases

```python
import password_validator as pv


def test_password_validation():
    assert pv.validate_password("Abc12345") is True
    assert pv.validate_password("password123") is False
    assert pv.validate_password("Pass") is False
    assert pv.validate_password("HelloWorld") is False
```
