def reverse_string(s: str) -> str:
    # Base case - if s is empty, return empty string
    if s == '':
        return ''

    # Recursive case - return the last character of s and call reverse_string again
    return reverse_string(s[1:]) + s[0]
