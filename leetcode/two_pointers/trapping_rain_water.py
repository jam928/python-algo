from typing import List


# https://leetcode.com/problems/trapping-rain-water/

def trap(height: List[int]) -> int:
    if len(height) < 3:
        return 0

    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    trapped_water = 0

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max < right_max:
            trapped_water += left_max - height[left]
            left += 1
        else:
            trapped_water += right_max - height[right]
            right -= 1

    return trapped_water

print(trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9