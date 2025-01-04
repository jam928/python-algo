from typing import List

# https://leetcode.com/problems/maximal-square/description/
# T: O(MN)
# S: O(MN)

def maximal_square(matrix: List[List[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    max_sq_len = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] != '1':
                continue
            # check northwest, north, or west min
            # if its a 1 for all sides then we get a square of length 2
            # if we encounter even a single zero then minimum value will be zero and a square of length 1 will be formed.
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            max_sq_len = max(dp[i][j], max_sq_len)

    return max_sq_len * max_sq_len

if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(maximal_square(matrix)) # 4