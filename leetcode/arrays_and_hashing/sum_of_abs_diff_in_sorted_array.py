from typing import List


# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

def get_sum_absolute_differences(nums: List[int]) -> List[int]:
    n = len(nums)
    total_sum = sum(nums)
    prefix_sum = 0
    result = [0] * n

    for i in range(len(nums)):
        left_count = i
        right_count = n - i - 1
        left_sum = (left_count * nums[i] - prefix_sum)
        right_sum = (total_sum - prefix_sum - nums[i] * (right_count + 1))
        result[i] = left_sum + right_sum

        prefix_sum += nums[i]

    return result

if __name__ == '__main__':
    print(get_sum_absolute_differences([2,3,5])) # [4,3,5]
    print(get_sum_absolute_differences([1,4,6,8,10])) # [24,15,13,15,21]