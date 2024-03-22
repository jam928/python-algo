# https://leetcode.com/problems/distinct-subsequences/description/ Overall, the time and space complexity of the
# algorithm is O(n * m), where n is the length of string s and m is the length of string t.

def num_distinct(s: str, t: str) -> int:
    memo = {}

    def helper(i, j):
        if j >= len(t):
            return 1

        if i >= len(s):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        count = 0
        if s[i] == t[j]:
            count = helper(i + 1, j + 1) + helper(i + 1, j)  # count subseq if iterate both and only if iterate i
        else:
            count = helper(i + 1, j)

        memo[(i, j)] = count
        return count

    return helper(0, 0)


print(num_distinct(s="rabbbit", t="rabbit"))  # 3
print(num_distinct(s="babgbag", t="bag"))  # 5
