from typing import List

# https://leetcode.com/problems/group-anagrams/description/

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams_list = anagram_map.get(sorted_word, [])
        anagrams_list.append(word)
        anagram_map.update({sorted_word: anagrams_list})

    return list(anagram_map.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]

print(group_anagrams([""]))
# [[""]]

print(group_anagrams(["a"]))
# [["a"]]