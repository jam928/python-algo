from typing import List

# https://leetcode.com/problems/number-of-zero-filled-subarrays/

def zero_filled_subarray(nums: List[int]) -> int:
    count = result = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            count = 0

        result += count

    return result

if __name__ == '__main__':
    print(zero_filled_subarray([1,3,0,0,2,0,0,4])) # 6
    print(zero_filled_subarray([0,0,0,2,0,0])) # 9
    print(zero_filled_subarray([2,10,2019])) # 0