# Challenge: Format Phone Number

## Instructions

Write a function called `format_phone_number` that takes in an array of numbers and returns a string representing the phone number formed by concatenating the numbers in the specified format.

### Function Signature

```python
def format_phone_number(numbers):
    """
    Returns a string representing a phone number.
    :param numbers: The numbers to use in the phone number.
    :type numbers: list of int
    :return: The formatted phone number.
    :rtype: str
    """
    pass
```

### Examples

```python
format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => "(123) 456-7890"
format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]) # => "(519) 555-4468"
format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]) # => "(345) 501-2527"
```

### Constraints

- The input array will always have 10 numbers
- The numbers can be any integer from 0 to 9

### Hints

- You can use the `''.join'` method to concatenate the numbers in the array.

## Solutions

<details>
  <summary>Click For Solution 1</summary>

```python
def format_phone_number_1(numbers):
    # Get the first 3 numbers and join them together
    area_code = ''.join(map(str,numbers[0:3]))

    # Get the next 3 numbers and join them together
    prefix = ''.join(map(str,numbers[3:6]))

    # Get the last 4 numbers and join them together
    line_number = ''.join(map(str,numbers[6:]))

    return f"({area_code}) {prefix}-{line_number}"
```

### Explanation

- Create 3 variables to store the area code, prefix, and line number.
- Use the `Array.join` method to concatenate the numbers in the array.

</details>

<details>
  <summary>Click For Solution 2</summary>

```python
def format_phone_number_2(numbers):
    # Join all the numbers together
    formatted = ''.join(map(str,numbers))

    return f"({formatted[0:3]}) {formatted[3:6]}-{formatted[6:]}"
```

### Explanation

- Created a variable to store the numbers in the array concatenated together.

</details>

<details>
  <summary>Click For Solution 3</summary>

One line arrow function:

```python
def format_phone_number_3(numbers):
    formatted_number = f"({''.join(map(str, numbers[:3]))}) {''.join(map(str, numbers[3:6]))}-{''.join(map(str, numbers[6:]))}"
    return formatted_number
```

### Explanation

This is similar to the second solution, but we used an arrow function and Array.slice method chaining.

</details>

### Test Cases

```python
import format_phone_number as format


def test_format_phone_number():
    assert format.format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == '(123) 456-7890'
    assert format.format_phone_number([5, 0, 2, 4, 8, 1, 9, 6, 3, 7]) == '(502) 481-9637'
    assert format.format_phone_number([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == '(999) 999-9999'
```
