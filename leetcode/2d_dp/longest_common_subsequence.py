# https://leetcode.com/problems/longest-common-subsequence/description/
# T: 0(m * n) where m is the length of text1; where n is the length of text 2
# S: 0(m * n) where m is the length of text1; where n is the length of text 2

def longest_common_subsequence(text1: str, text2: str) -> int:
    memo = {}

    def dfs(i, j):
        # If we are out of bounds return 0
        if i >= len(text1) or j >= len(text2):
            return 0

        # if we already visited this value in the dp then just return that
        if (i, j) in memo:
            return memo[(i, j)]

        count = 0
        # if both chars equal to each other increment both pointers and dfs
        if text1[i] == text2[j]:
            count = dfs(i + 1, j + 1) + 1
        else:
            # try dfs left and right ptr
            left = dfs(i + 1, j)
            right = dfs(i, j + 1)
            count = max(left, right)

        # set the current i,j from count value
        memo[(i, j)] = count
        return memo[(i, j)]

    return dfs(0, 0)


print(longest_common_subsequence(text1="abcde", text2="ace"))  # 3
print(longest_common_subsequence(text1="abc", text2="abc"))  # 3
print(longest_common_subsequence(text1="abc", text2="def"))  # 0
