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
