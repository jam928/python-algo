from collections import deque
from typing import List

# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
# T: O(N)
# S: O(N)

def longest_subarray(nums: List[int], limit: int) -> int:
    # monotonically decreasing deque elements stored
    max_deque = deque()

    # monotonically increasing deque elements stored
    min_deque = deque()

    longest_subarray = 0
    i = 0

    for j in range(len(nums)):
        current_num = nums[j]

        # poll the elements that are less than the current number in the max_deque
        while max_deque and current_num > max_deque[-1]:
            max_deque.pop()

        # poll the elements that are greater than the current number in the min deque
        while min_deque and current_num < min_deque[-1]:
            min_deque.pop()

        # add the current number to both deques
        min_deque.append(current_num)
        max_deque.append(current_num)

        while max_deque and min_deque and max_deque[0] - min_deque[0] > limit:
            if min_deque[0] == nums[i]:
                min_deque.popleft()

            if max_deque[0] == nums[i]:
                max_deque.popleft()

            i += 1

        longest_subarray = max(longest_subarray, j - i + 1)

    return longest_subarray

if __name__ == '__main__':
    nums = [8, 2, 4, 7]
    limit = 4
    print(longest_subarray(nums, limit)) # 2

    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    print(longest_subarray(nums, limit)) # 4

    nums = [4,2,2,2,4,4,2,2]
    limit = 0
    print(longest_subarray(nums, limit)) # 3
