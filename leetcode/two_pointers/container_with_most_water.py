from typing import List

# https://leetcode.com/problems/container-with-most-water/

def max_area(height: List[int]) -> int:
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        # Calculate the height, width, and area of the current given left & right ptrs
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)

        # move the pointers accordingly
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(height)
print(result)