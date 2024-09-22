from collections import defaultdict
from typing import List

# https://leetcode.com/problems/group-anagrams/description/

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)

    for s in strs:
        # sort the string to add to map
        sorted_str = ''.join(sorted(s))
        # map the sorted str as key and the word as the value
        anagram_map[sorted_str].append(s)

    return list(anagram_map.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]

print(group_anagrams([""]))
# [[""]]

print(group_anagrams(["a"]))
# [["a"]]