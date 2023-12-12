def reverse_string(s):
    # Base case - if s is empty, return empty string
    if s == '':
        return ''

    # Recursive case - return the last character of s and call reverse_string again
    return reverse_string(s[1:]) + s[0]


def reverse_string_2(s):
    return '' if s == '' else reverse_string(s[1:]) + s[0]
