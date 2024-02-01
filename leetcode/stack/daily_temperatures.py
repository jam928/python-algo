from typing import List


# https://leetcode.com/problems/daily-temperatures/description/
# T: O(N)
# S: O(N)

def daily_temperatures(temperatures: List[int]) -> List[int]:
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


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
print(daily_temperatures([30, 40, 50, 60]))  # [1,1,1,0]
print(daily_temperatures([30, 60, 90]))  # [1,1,0]
