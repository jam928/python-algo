from typing import List


# https://leetcode.com/problems/coin-change-ii/

# Time Complexity: O(2^n)
# Space Complexity: O(amount * len(coins))

def change(amount: int, coins: List[int]) -> int:
    memo = {}

    def dfs(current_amount, index):
        # base case
        if current_amount == amount:
            return 1

        if current_amount > amount or index == len(coins):
            return 0

        if (current_amount, index) in memo:
            return memo[(current_amount, index)]

        # dfs the current amount plus the current coin without incrementing the index
        # and dfs the current amount with increment the index
        memo[(current_amount, index)] = dfs(current_amount + coins[index], index) + dfs(current_amount, index + 1)
        return memo[(current_amount, index)]

    count = dfs(0, 0)
    return count


print(change(amount=5, coins=[1, 2, 5]))  # 4
print(change(amount=3, coins=[2]))  # 0
print(change(amount=10, coins=[10]))  # 1
