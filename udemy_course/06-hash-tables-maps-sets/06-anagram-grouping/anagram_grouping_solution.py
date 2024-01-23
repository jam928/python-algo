from collections import defaultdict

def anagram_grouping(words):
    anagram_groups = defaultdict(list)

    for word in words:
        # Sort the characters of the word alphabetically.
        sorted_chars = ''.join(sorted(word))

        # Add the word to the corresponding group in the dictionary.
        anagram_groups[sorted_chars].append(word)

    # Return the values of the dictionary as a list.
    return list(anagram_groups.values())
