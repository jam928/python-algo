from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

def max_profit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(1, len(prices)):
        # if the current day is greater than the previous day then add it up then the max profit variable
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

if __name__ == '__main__':
    print(max_profit([7,1,5,3,6,4])) # 7
    print(max_profit([1,2,3,4,5])) # 4
    print(max_profit([7,6,4,3,1])) # 0
    print(max_profit([3,3,5,0,0,3,1,4])) # 6