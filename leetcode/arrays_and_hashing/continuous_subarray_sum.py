from typing import List

# https://leetcode.com/problems/continuous-subarray-sum/

def check_subarray_sum(nums: List[int], k: int) -> bool:
    prefix_sum = {0: -1}
    current_sum = 0

    for i in range(len(nums)):
        current_sum = (current_sum + nums[i]) % k

        if current_sum in prefix_sum:
            if i - prefix_sum[current_sum] > 1:
                return True
        else:
            prefix_sum[current_sum] = i

    return False