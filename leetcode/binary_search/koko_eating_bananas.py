from math import ceil
from typing import List


# https://leetcode.com/problems/koko-eating-bananas/description/

# # 1. Binary search on the from 1 to max element in the array
#     # 2. k will be the mid point from left and right element
#     # 3. calculate the total time by time = ceil(pile/k)
#     # 4. if total_time <= h update global result var and shrink the right
#     # 5. else shrink the left
def min_eating_speed(piles: List[int], h: int) -> int:
    left = 1
    right = max(piles)

    result = right

    # modified binary search
    while left <= right:
        k = (left + right) // 2

        # calc the total time with k hour
        total_time = 0
        for pile in piles:
            time = ceil(pile / k)
            total_time += time

        if total_time <= h:
            # we found a potential solution for k; lets move the right pointer to k - 1 for potential smaller k values
            result = k
            right = k - 1
        else:
            left = k + 1

    return result


print(min_eating_speed(piles=[3, 6, 7, 11], h=8))  # 4
print(min_eating_speed(piles=[30, 11, 23, 4, 20], h=5))  # 30
print(min_eating_speed(piles=[30, 11, 23, 4, 20], h=6))  # 23
