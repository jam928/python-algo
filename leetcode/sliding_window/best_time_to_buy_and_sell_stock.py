from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices: List[int]) -> int:

    # keep of the min price so far while iterating the array
    # keep track of the max profit by the current price minus the min price seen so far to achive max profit
    max_profit, min_price = 0, 99999

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

print(max_profit([7,1,5,3,6,4])) # 5
print(max_profit([7,6,4,3,1])) # 0