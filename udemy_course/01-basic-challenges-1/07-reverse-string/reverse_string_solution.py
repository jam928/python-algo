def reverse_string(str):
    return str[::-1]


def reverse_string_2(str):
    reverse_str = ""

    for i in range(len(str) - 1, -1, -1):
        reverse_str += str[i]

    return reverse_str
