# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# T: O(N * TARGET * K)
# S: O(N * TARGET)
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        mod = pow(10, 9) + 7

        def helper(n, k, target):
            if target == 0 and n == 0:
                return 1

            if target < 0 or n == 0:
                return 0

            if (n, target) in dp:
                return dp[n, target]

            count = 0
            for i in range(1, k + 1):
                count += helper(n - 1, k, target - i)

            count %= mod
            dp[(n, target)] = count
            return count

        return helper(n, k, target)

if __name__ == '__main__':
    s = Solution()
    assert s.numRollsToTarget(1,6,3) == 1
    assert s.numRollsToTarget(2,6,7) == 6
    assert s.numRollsToTarget(30, 30, 500) == 222616187