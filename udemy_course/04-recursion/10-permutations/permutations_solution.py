def permutations(s):
    # Create a list to store the permutations
    result = []

    # If s is an empty string, append an empty string to result and return
    if len(s) == 0:
        result.append('')
        return result

    # Loop through each character in s
    for i in range(len(s)):
        # Get the first character
        first_char = s[i]
        # Get the rest of the string
        rest_of_string = s[:i] + s[i + 1:]
        # Get the permutations of the rest of the string
        sub_permutations = permutations(rest_of_string)

        # Loop through each permutation in sub_permutations
        for j in range(len(sub_permutations)):
            # Append the first character and the permutation to result
            result.append(first_char + sub_permutations[j])

    # Return result
    return result
