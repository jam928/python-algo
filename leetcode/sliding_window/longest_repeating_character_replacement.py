# https://leetcode.com/problems/longest-repeating-character-replacement/description/
def character_replacement(s: str, k: int) -> int:
    # utilize a map to keep track of the characters along with their freqs
    freq_map = {}

    i = 0
    max_length = 0
    max_repeat_letter_count = 0

    for j in range(len(s)):
        right_char = s[j]

        # add the character along with its freq in the map
        freq_map[right_char] = freq_map.get(right_char, 0) + 1

        # update the max repeat letter count if necessary
        max_repeat_letter_count = max(max_repeat_letter_count, freq_map[right_char])

        # shrink the window if the freq map is greater than k

        if j - i + 1 - max_repeat_letter_count > k:
            left_char = s[i]

            freq_map[left_char] = freq_map.get(left_char) - 1

            i += 1

        max_length = max(max_length, j - i + 1)

    return max_length

print(character_replacement(s = "ABAB", k = 2))
print(character_replacement(s = "AABABBA", k = 1))