# https://leetcode.com/problems/longest-common-prefix/description/
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    # The longest common prefix will be the shortest string compared with the longest string
    first = min(strs)
    last = max(strs)

    prefix = ''

    for i in range(len(first)):
        if first[i] != last[i]:
            break
        prefix += first[i]

    return prefix

print(longest_common_prefix(["flower","flow","flight"])) # "fl"
print(longest_common_prefix(["dog","racecar","car"])) # ""