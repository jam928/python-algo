def longest_common_substring(str1, str2):
    memo = {}  # Dictionary to store results of subproblems

    def helper(i, j, current_length):
        # Base case: If any index exceeds the bounds of the strings
        if i == len(str1) or j == len(str2):
            return current_length

        # Check if the current state is already computed
        if (i, j, current_length) in memo:
            return memo[(i, j, current_length)]

        # If characters match, increment `current_length` and move to the next pair
        new_length = current_length
        if str1[i] == str2[j]:
            new_length = helper(i + 1, j + 1, current_length + 1)

        # Explore other possibilities by resetting current length
        result = max(
            new_length,  # Current match length
            helper(i + 1, j, 0),  # Skip current character in `str1`
            helper(i, j + 1, 0)  # Skip current character in `str2`
        )

        # Save result in memo
        memo[(i, j, current_length)] = result
        return result

    return helper(0, 0, 0)


# Example usage
str1 = "adac"
str2 = "adadac"
print(longest_common_substring(str1, str2))  # Output: 4
