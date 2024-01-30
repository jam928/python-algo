def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0

    # keep track of the freq count of the characters in a dictionary
    freq_count = {}

    # keep track of the longest
    longest = float('-inf')

    # sliding window approach
    # we extend while obligating the contract, and we shrink if we are violating it
    i = 0
    for j in range(len(s)):
        right = s[j]
        # add the j char to the dictionary
        freq_count[right] = freq_count.get(right, 0) + 1

        # shrink the window if the rightmost character freq count is greater than 1
        while freq_count[right] > 1:
            left = s[i]
            # remove the leftmost character
            freq_count[left] = freq_count.get(left, 0) - 1

            # remove character from dictionary if the freq count is zero
            if freq_count[left] == 0:
                del freq_count[left]

            # increment the i pointer
            i += 1

        # update the longest if necessary
        longest = max(longest, j - i + 1)

    return longest

print(length_of_longest_substring("abcabcbb")) # 3
print(length_of_longest_substring("bbbbb")) # 1
print(length_of_longest_substring("pwwkew")) # 3