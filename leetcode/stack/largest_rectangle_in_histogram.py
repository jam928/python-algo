from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]

        maxArea = 0
        length_of_heights = len(heights)
        for i,height in enumerate(heights):
            # pop out elements in stack if they are larger than the current element
            while stack and stack[-1] != -1 and (heights[stack[-1]] >= height):
                currentHeight = heights[stack.pop()]
                currentWidth = i - stack[-1] - 1
                maxArea = max(maxArea, currentHeight * currentWidth)

            stack.append(i)

        while stack and stack[-1] != -1:
            currentHeight = heights[stack.pop()]
            currentWidth = length_of_heights - stack[-1] - 1
            maxArea = max(maxArea, currentHeight * currentWidth)

        return maxArea

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    print(Solution().largestRectangleArea(heights)) # 10

    heights = [2,4]
    print(Solution().largestRectangleArea(heights)) # 4