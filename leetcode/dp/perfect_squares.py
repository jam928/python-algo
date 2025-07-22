from collections import defaultdict

# T: O(N*SQRT(N))
# S: O(N)
# https://leetcode.com/problems/perfect-squares/description/

class Solution:
    def numSquares(self, n: int) -> int:
        dp = defaultdict(int)

        def calculateSquares(n):
            if n == 0:
                return 0

            if n in dp:
                return dp[n]

            min_value = float('inf')
            i = 1
            while (i * i) <= n:
                result = 1 + calculateSquares(n - (i * i))
                min_value = min(min_value, result)
                i += 1

            dp[n] = min_value
            return dp[n]

        return calculateSquares(n)

if __name__ == "__main__":
    s = Solution()
    assert s.numSquares(12) == 3
    assert s.numSquares(13) == 2