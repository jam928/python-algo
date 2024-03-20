# T: O(m*n) where m is the number of rows; n number of columns
# S: O(m*n) where m is the number of rows; n number of columns

# https://leetcode.com/problems/unique-paths/description/
def unique_paths(m: int, n: int) -> int:
    dp = [[None] * n for _ in range(m)]

    def helper(i, j):
        if i == m - 1 and j == n - 1:
            return 1

        if i >= m or j >= n:
            return 0

        if dp[i][j]:
            return dp[i][j]

        count = helper(i + 1, j) + helper(i, j + 1)
        dp[i][j] = count
        return dp[i][j]

    return helper(0, 0)


print(unique_paths(3, 7))  # 28
print(unique_paths(3, 2))  # 3
