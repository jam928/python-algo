from typing import List

# https://leetcode.com/problems/palindrome-partitioning/
# T: O(2 ^ N)
# S: O(K) where k is the length of the string

def partition(s: str) -> List[List[str]]:
    result = []
    partition = []

    def dfs(i):
        if i >= len(s):
            result.append(list(partition))
            return
        for j in range(i, len(s)):
            if not is_palindrome(s, i, j):
                continue
            partition.append(s[i:j + 1])
            dfs(j + 1)
            partition.pop()

    dfs(0)
    return result


def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

print(partition(s = "aab")) # [['a', 'a', 'b'], ['aa', 'b']]
print(partition(s = "a")) # [['a']]