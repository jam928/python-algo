# Challenge: Validate Email

## Instructions

Write a function called `validate_email` that takes in a string and returns whether the string is a valid email address. For the purposes of this challenge, a valid email address is defined as a string that contains an `@` symbol and a `.` symbol.

### Function Signature

```python
def validate_email(email):
    """
    Returns whether the string is a valid email address.
    :param email: The email address to validate.
    :type email: str
    :return: Whether the email address is valid.
    :rtype: bool
    """
    pass
```

### Examples

```js
validate_email('john@gmail.com'); # true
validate_email('john@gmail'); # false
```

### Hints

- If you know regular expressions, this is a great place to use them. I am going to give you two solutions. One uses regular expressions and one doesn't.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

Using a regular expression:

```python
import re


def validate_email(email):
    """
    Returns whether the string is a valid email address.
    :param email: The email address to validate.
    :type email: str
    :return: Whether the email address is valid.
    :rtype: bool
    """
    # Regular expression for a basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Using re.match() to check if the email matches the pattern
    match = re.match(pattern, email)

    # Return True if there is a match, otherwise, return False
    return bool(match)
```

### Explanation

The regular expression is a bit complicated, but it is a good example of how powerful regular expressions can be. Let's break it down:

- ^ asserts the start of the string.
- [A-Za-z0-9._%+-]+ matches one or more occurrences of letters (both uppercase and lowercase), digits, dots, underscores, percent signs, plus signs, and hyphens. This represents the local part of the email address before the "@" symbol.
- @ matches the "@" symbol.
- [A-Za-z0-9.-]+ matches one or more occurrences of letters, digits, dots, and dashes. This represents the domain name of the email address.
- \. matches the dot (".") character. It needs to be escaped with a backslash because the dot has a special meaning in regular expressions.
- [A-Za-z]{2,} matches two or more occurrences of letters. This represents the top-level domain (TLD) of the email address.
- $ asserts the end of the string.

</details>

<details>
  <summary>Click For Solution 2</summary>

Not using regular expression:

```python
def validate_email(email):
    if '@' not in email:
        return False

    [local_part, domain] = email.split('@')

    # if the length of the first part of the email is 0 or length of the domain is less than 3
    # return false as does not mean the requirements of a valid email
    if len(local_part) == 0 or len(domain) < 3:
        return False

    domain_extension = domain.split('.')

    if len(domain_extension) < 2 or len(domain_extension[1]) < 2:
        return False

    return True
```

### Explanation

This solution is a bit more complicated, but it doesn't use regular expressions.

- Validate if the `@` is in the string.
- Use the `split` method to split the email address into two parts: the local part and the domain. We use destructuring to assign the two parts to variables.
- Check if the local part is empty or if the domain is less than three characters long. If either of these conditions is true, we return `false`.
  Split the domain into parts using the `split` method. We check if the domain has at least two parts and if the last part is at least two characters long.
- If either of these conditions is false, return `false`.

Finally, if none of the conditions are false, we return `true`.

</details>

### Test Cases

```python
import validate_email as valid_email


def test_email_addresses():
    valid_email_addresses = ['john@example.com', 'jane.doe@domain.org']

    for email in valid_email_addresses:
        assert valid_email.validate_email(email) is True

    invalid_email_addresses = ['invalid-email', '@domain.com', 'user@domain']

    for email in invalid_email_addresses:
        assert valid_email.validate_email(email) is False
```
