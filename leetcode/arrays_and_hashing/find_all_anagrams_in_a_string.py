from collections import defaultdict
from typing import List


# https://leetcode.com/problems/find-all-anagrams-in-a-string/

def find_anagrams(s: str, p: str) -> List[int]:
    # store freq in map for p string
    freq_map = defaultdict(int)
    for c in p:
        freq_map[c] += 1

    matched = 0
    i = 0

    result = []
    for j in range(len(s)):
        current_char = s[j]
        if current_char in freq_map:
            freq_map[current_char] -= 1

            if freq_map[current_char] == 0:
                matched += 1

        if j >= len(p) - 1:
            if matched == len(freq_map):
                result.append(i)

            left_char = s[i]

            if left_char in freq_map:
                if freq_map[left_char] == 0:
                    matched -= 1
                freq_map[left_char] += 1
            i += 1

    return result

if __name__ == '__main__':
    print(find_anagrams(s = "cbaebabacd", p = "abc")) # [0,6]
    print(find_anagrams(s = "abab", p = "ab")) # [0,1,2]
