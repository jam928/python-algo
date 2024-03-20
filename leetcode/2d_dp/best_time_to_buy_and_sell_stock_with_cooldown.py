from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# T: O(n)
# S: O(n)

def max_profit(prices: List[int]) -> int:
    memo = {}

    def calc(index, transaction):
        # base case
        if index >= len(prices):
            return 0

        if (index, transaction) in memo:
            return memo[(index, transaction)]

        max_profit = 0

        if transaction == 'buy':
            # we have the option to buy now or buy later
            buy_now = calc(index + 1, "sell") - prices[index]
            buy_later = calc(index + 1, "buy")

            max_profit = max(buy_now, buy_later)
        elif transaction == "sell":
            # we have the option to sell now or sell later
            sell_now = calc(index + 1, "cooldown") + prices[index]
            sell_later = calc(index + 1, "sell")

            max_profit = max(sell_now, sell_later)
        elif transaction == "cooldown":
            # cool down, so now we can buy the next day if we want to
            max_profit = calc(index + 1, "buy")

        memo[(index, transaction)] = max_profit
        return memo[(index, transaction)]

    return calc(0, "buy")


print(max_profit(prices=[1, 2, 3, 0, 2]))  # 3
print(max_profit([1]))  # 0
print(max_profit([1, 2, 4]))  # 3
print(max_profit([2, 1, 4]))  # 3
