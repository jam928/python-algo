# Challenge: Phone Number Directory

## Instructions

You are building a phone number directory application. Implement a function called `phoneNumberDirectory` that takes an array of phone numbers as input and returns a Map with names as keys and corresponding phone numbers as values.

### Function Signature

```python
from typing import List, Dict

def phone_number_directory(phone_numbers: List[str]) -> Dict[str, str]:
    """
    Builds a phone number directory from an array of phone numbers.

    Parameters:
    - phone_numbers (List[str]): An array of phone numbers in the format "Name:PhoneNumber".

    Returns:
    - Dict[str, str]: A dictionary with names as keys and corresponding phone numbers as values.
    """
    # Your code here
```

### Examples

```python
phone_numbers = [
  'John:123-456-7890',
  'Jane:987-654-3210',
  'Joe:555-555-5555',
];

print(phone_number_directory(phone_numbers));
# Output: Map { 'John' => '123-456-7890', 'Jane' => '987-654-3210', 'Joe' => '555-555-5555' }
```

### Constraints

- The input array elements should be formatted as `NAME:PHONENUMBER`

### Hints

- Loop through the input array and use the `split()` method to separate the name and phone number in each element of the `phoneNumbers` array before adding to the map

## Solutions

<details>
  <summary>Click For Solution</summary>

```python
from typing import List, Dict


def phone_number_directory(phone_numbers: List[str]) -> Dict[str, str]:
    """
    Builds a phone number directory from an array of phone numbers.

    Parameters:
    - phone_numbers (List[str]): An array of phone numbers in the format "Name:PhoneNumber".

    Returns:
    - Dict[str, str]: A dictionary with names as keys and corresponding phone numbers as values.
    """
    # Your code here

    phone_book = {}
    for entry in phone_numbers:
        name, phone_number = entry.split(':')
        phone_book[name] = phone_number

    return phone_book
```

### Explanation

- Create a new Map called `phone_book`
- Iterate through the `phone_numbers` array using a `for...of` loop
- Use the `split()` method to separate the name and phone number from each entry using the colon `:` as the separator
- Set each name as the key and its corresponding phone number as the value in the Map
- Return the `phone_book`, which now contains the phone number directory

</details>

### Test Cases

```python
from phone_number_directory import phone_number_directory

def test_phone_number_directory():
    phone_numbers = [
        'John:123-456-7890',
        'Jane:987-654-3210',
        'Joe:555-555-5555',
    ]

    result = phone_number_directory(phone_numbers)

    assert result['John'] == '123-456-7890'
    assert result['Jane'] == '987-654-3210'
    assert result['Joe'] == '555-555-5555'
```
