# https://leetcode.com/problems/wildcard-matching/description/
# T: O(MN)
# S: O(MN)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        memo = {}

        def dfs(i, j):
            if len(s) == i and len(p) == j:
                return True

            if i > m or j > n:
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            result = False
            if (i < m and j < n) and (s[i] == p[j] or p[j] == '?'):
                result = dfs(i + 1, j + 1)
            elif (j < n) and p[j] == '*':
                result = dfs(i + 1, j + 1) or dfs(i, j + 1) or dfs(i + 1, j)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)

if __name__ == '__main__':
    s = "aa"
    p = "a"

    print(Solution().isMatch(s, p)) # False

    s = "aa"
    p = "*"

    print(Solution().isMatch(s, p)) # True

    s = "cb"
    p = "?a"

    print(Solution().isMatch(s, p)) # False