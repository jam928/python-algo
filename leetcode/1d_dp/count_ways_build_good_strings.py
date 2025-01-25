
# T: O(high)
# S: O(high)
# https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        mod = 10 ** 9 + 7
        dp = {}

        def dfs(length):
            if length > high:
                return 0

            if length in dp:
                return dp[length]

            result = 1 if length >= low else 0
            result += dfs(length + zero) + dfs(length + one)
            dp[length] = result
            return dp[length] % mod

        return dfs(0)

if __name__ == '__main__':
    print(Solution().countGoodStrings(low = 3, high = 3, zero = 1, one = 1)) # 8
    print(Solution().countGoodStrings(low = 2, high = 3, zero = 1, one = 2)) # 5