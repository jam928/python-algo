def replace_pattern(string):
    new_string = ""
    i = 0
    while i < len(string):
        if string[i] == "[":
            num_str = ""
            j = i
            i += 1
            while string[i].isdigit():
                num_str += string[i]
                i += 1
            num = int(num_str)
            i += 1  # Move past the closing bracket
            replace_string = ""
            if string[j - 1] == 'x':
                replace_string = string[j - 3:j]
            else:
                replace_string = string[j - 1:j]
            replacement = replace_string * (num - 1)
            new_string += replacement
        else:
            new_string += string[i]
            i += 1
    return new_string


def count_decoded_letters(input):
    """
    :type input: String
    :rtype: int[]
    """

    s = replace_pattern(input)

    counts = [0] * 26
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i+2] == 'x' and (10 <= int(s[i:i+2]) <= 26):
            counts[int(s[i:i+2]) - 1] += 1
            i+=3
        else:
            counts[int(s[i:i+1]) - 1] += 1
            i+=1
    return counts

# Test cases
print(count_decoded_letters("8512x[2]15x"))  # Example 1
print(count_decoded_letters("18x14x18x[2]11x18x11x[3]"))  # Example 2
print(count_decoded_letters("1212x12323x23123"))  # Example 3
