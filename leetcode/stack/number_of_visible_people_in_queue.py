from typing import List

# https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/
# T: O(N)
# S: O(N)

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        n = len(heights)
        result = [0] * n
        stack = []

        for index, height in enumerate(heights):
            # if the current height is greater than the last element in stack increment its count
            while stack and height > heights[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] += 1

            if stack:  # if the stack is not empty then increment the last value 1
                result[stack[-1]] += 1

            stack.append(index)

        return result

if __name__ == '__main__':
    s = Solution()
    assert s.canSeePersonsCount([10,6,8,5,11,9]) == [3,1,2,1,1,0]
    assert s.canSeePersonsCount([5,1,2,3,10]) == [4,1,1,1,0]
