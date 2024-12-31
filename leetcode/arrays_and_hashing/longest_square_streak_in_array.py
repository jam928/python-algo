from typing import List

# https://leetcode.com/problems/longest-square-streak-in-an-array/
# T: O(N LOG N)
# S: O(N)

def longest_square_streak(nums: List[int]) -> int:
    # sort and convert the list to a set for quick lookup
    nums.sort()
    num_set = set(nums)

    longest_streak = 0

    for num in nums:
        current_streak = 0
        current = num

        # continue as long as we find the square in the set
        while current in num_set:
            current_streak += 1
            current = current * current

        if current_streak >= 2:
            longest_streak = max(longest_streak, current_streak)

    # if the streak of least 2 was found return that else -1
    return longest_streak if longest_streak >= 2 else -1

if __name__ == '__main__':
    print(longest_square_streak([4,3,6,16,8,2])) # 3
    print(longest_square_streak([2,3,5,6,7])) # -1