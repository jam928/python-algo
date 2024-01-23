from typing import List

def anagram_grouping(words: List[str]) -> List[List[str]]:

    anagram_map = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams_list = anagram_map.get(sorted_word, [])
        anagrams_list.append(word)
        anagram_map.update({sorted_word: anagrams_list})

    return list(anagram_map.values())