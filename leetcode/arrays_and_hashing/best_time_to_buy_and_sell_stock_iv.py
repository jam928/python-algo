from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
# T: O(N * K)
# S: O(N * K)
def maxProfit(k: int, prices: List[int]) -> int:
    dp = {}

    def helper(i, k, on):
        if i >= len(prices):
            return 0

        if (i, k, on) in dp:
            return dp[(i, k, on)]

        profit = 0
        profit = max(profit, helper(i + 1, k, on))
        if on:
            profit = max(profit, prices[i] + helper(i + 1, k - 1, False))
        elif k > 0:
            profit = max(profit, helper(i + 1, k, True) - prices[i])

        dp[(i, k, on)] = profit
        return profit

    return helper(0, k, False)