# Challenge: Valid IPv4 Addresses

## Instructions

Write a function called `is_valid_ipv4` that takes a string as input and returns `true` if the input is a valid IPv4 address in dot-decimal format, and `false` otherwise. An IPv4 address should consist of four octets, with values between 0 and 255, inclusive.

### Function Signature

```python
def is_valid_ipv4(input_str: str) -> bool:
    """
    Checks if a given string is a valid IPv4 address.
    :param input_str: The input string to check.
    :type input_str: str
    :return: True if the input is a valid IPv4 address, False otherwise.
    :rtype: bool
    """
    # Your implementation here to check if the input is a valid IPv4 address
```

### Examples

```python
is_valid_ipv4('1.2.3.4') # true
is_valid_ipv4('123.45.67.89') # true
is_valid_ipv4('1.2.3') # false
is_valid_ipv4('1.2.3.4.5') # false
is_valid_ipv4('123.456.78.90') # false
is_valid_ipv4('123.045.067.089') # false
```

### Constraints

- The input will be a single string.

### Hints

- You can use the `split()` method to break the string into parts based on the dot character.
- You can use `every()` to check if all octets are within the valid range of 0 to 255.

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
def is_valid_ipv4(input_str: str) -> bool:
    octets = input_str.split(".")
    return len(octets) == 4 and all(0 <= int(octet) <= 255 and octet == str(int(octet)) for octet in octets)
```

## Explanation

- Split the input string into an array of strings using the `split()` method.
- Check if the array has exactly four elements. If not, return `false`.
- Use the `all()` method to check if all octets are valid.
  - Convert the octet to a number using `int()`.
  - Check if the number is between 0 and 255, inclusive.
  - Check if the octet is equal to the number converted back to a string. This is to check for leading zeros.

</details>

### Test Cases

```python
import valid_ipv4 as v


def test_valid_ipv4_addresses():
    ipv4_addresses = {
        '1.2.3.4': True,
        '123.45.67.89': True,
        '1.2.3': False,
        '1.2.3.4.5': False,
        '123.456.78.90': False,
        '123.045.067.089': False
    }

    for e in ipv4_addresses:
        assert v.is_valid_ipv4(e) is ipv4_addresses[e]
```

You can use this template for your challenge to validate IPv4 addresses in dot-decimal format!
