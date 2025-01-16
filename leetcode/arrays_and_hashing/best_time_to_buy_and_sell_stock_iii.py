from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# T: O(N)
# S: O(N)

def max_profit(prices: List[int]) -> int:
    n = len(prices)
    memo = {}

    def helper(index, buy, count):
        if index == n or count == 0:  # we reach the end of the array or we exhausted the number of transactions
            return 0

        if (index, buy, count) in memo:
            return memo[(index, buy, count)]

        profit = 0
        if buy:
            buy_now = -prices[index] + helper(index + 1, False, count)  # include the current price
            buy_later = helper(index + 1, True, count)  # do not include current price
            profit = max(buy_now, buy_later)
        else:
            sell_now = prices[index] + helper(index + 1, True, count - 1)  # sell at current price
            sell_later = helper(index + 1, False, count)  # sell later
            profit = max(sell_now, sell_later)

        memo[(index, buy, count)] = profit

        return profit

    return helper(0, True, 2)