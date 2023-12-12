import functools

def find_missing_letter(arr):
    # `start` is the character code of the first character in the array
    start = ord(arr[0])

    # `missing_char_code` is the character code of the missing character
    missing_char_code = next(
        (current for current in map(lambda char: ord(char), arr) if current - start > 1),
        None
    )

    # if `missing_char_code` is truthy, return the character that is one less than the character code
    return chr(missing_char_code - 1) if missing_char_code else ''


def find_missing_letter_2(arr):
    # `missing_char_code` is the character code of the missing character
    missing_char_code = next(
        (char for index, char in enumerate(arr[1:]) if ord(char) - ord(arr[index]) > 1),
        None
    )

    # if `missing_char_code` is truthy, return the character that is one less than the character code
    return chr(ord(missing_char_code) - 1) if missing_char_code else ''
