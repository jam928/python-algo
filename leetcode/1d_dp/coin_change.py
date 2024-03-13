from typing import List

# https://leetcode.com/problems/coin-change/description/
# T: O(n * m)
# S:  O(n)
def coin_change(coins: List[int], amount: int) -> int:
    memo = {}

    def helper(amount):
        if amount in memo:
            return memo[amount]

        # base case
        if amount == 0:
            return 0

        min_count = 999999

        if amount < 0:
            return min_count

        for coin in coins:
            if amount - coin >= 0 and coin <= amount:
                count = helper(amount - coin) + 1
                min_count = min(count, min_count)
        memo[amount] = min_count
        return memo[amount]

    count = helper(amount)
    return count if count != 999999 else -1

print(coin_change(coins = [1,2,5], amount = 11)) # 3
print(coin_change(coins = [2], amount = 3)) # -1
print(coin_change(coins = [1], amount = 0)) # 0
