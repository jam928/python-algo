import sys

# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
# T: O(N)
# S: O(N)
class Solution:
    def numOfWays(self, n: int) -> int:
        dp = {}
        return self.dfs(n, 0, 0, 0, dp)

    def dfs(self, n, a0, b0, c0, dp):
        if n == 0:
            return 1

        if (n, a0, b0, c0) in dp:
            return dp[(n, a0, b0, c0)]

        ans = 0
        colors = [1, 2, 3]  # Red: 1, Yellow: 2, Green: 3

        for a in colors:
            if a == a0:
                continue  # Check if the same color with the below neighbor
            for b in colors:
                if b == b0 or b == a:
                    continue  # Check if the same color with the below neighbor or the left neighbor
                for c in colors:
                    if c == c0 or c == b:
                        continue  # Check if the same color with the below neighbor or the left neighbor
                    ans += self.dfs(n - 1, a, b, c, dp)
                    ans %= 1_000_000_007  # Python equivalent for modulo operation

        dp[(n, a0, b0, c0)] = ans
        return ans

if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    s = Solution()
    print(s.numOfWays(1)) # 12
    print(s.numOfWays(5000)) # 30228214