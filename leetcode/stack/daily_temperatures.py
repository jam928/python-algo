from typing import List


# https://leetcode.com/problems/daily-temperatures/description/
# T: O(N)
# S: O(N)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        # maintain stack of indices
        stack = []

        for i in range(n):
            # remove elements from the stack if the current temperature is greater than the ones in the stack
            # means the current temperature is warmer than the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # difference of the current index and the prev_index
                result[prev_index] = i - prev_index
            stack.append(i)

        return result

if __name__ == '__main__':
    s = Solution()
    assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1,1,4,2,1,1,0,0]
    assert s.dailyTemperatures([30, 40, 50, 60]) == [1,1,1,0]
    assert s.dailyTemperatures([30, 60, 90]) == [1,1,0]
