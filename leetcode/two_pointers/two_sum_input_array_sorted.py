from typing import List

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def two_sum(numbers: List[int], target: int) -> List[int]:
    # use 2 pointers i and j
    i = 0
    j = len(numbers) - 1

    while i < j:
        sum_of_num = numbers[i] + numbers[j]
        if sum_of_num == target:
            return [i + 1, j + 1]
        # need larger numbers so increment i
        if sum_of_num < target:
            i += 1
        # need smaller numbers so decrement j
        elif sum_of_num > target:
            j -= 1

    return []

print(two_sum([2,7,11,15], 9)) # [1,2]
print(two_sum([2,3,4], 6)) # [1,3]
print(two_sum([-1,0], -1)) # [1,2]