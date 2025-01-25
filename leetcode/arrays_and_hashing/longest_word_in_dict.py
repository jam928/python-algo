from typing import List

# https://leetcode.com/problems/longest-word-in-dictionary/description/
# T: O(N LOG N + N * M)
# S: O(N * M) Where M is the length of the average word

def longest_word(words: List[str]) -> str:
    # Sort the words by length; if the same length, sort lexicographically
    words.sort(key=lambda word: (len(word), word))

    # Initialize a frequency map with an empty string
    freq_map = {"": 0}
    max_freq = 0
    result = ""

    for word in words:
        prefix = word[0:len(word) - 1]

        # If the prefix is found, update the frequency of the current word
        if prefix in freq_map:
            freq_map[word] = freq_map[prefix] + 1

        # Update max if the current word's frequency is greater than the current max
        if max_freq < freq_map.get(word, 0):
            max_freq = freq_map[word]
            result = word

    return result

if __name__ == "__main__":
    print(longest_word(["w","wo","wor","worl","world"])) # world
    print(longest_word(["a","banana","app","appl","ap","apply","apple"])) # apple