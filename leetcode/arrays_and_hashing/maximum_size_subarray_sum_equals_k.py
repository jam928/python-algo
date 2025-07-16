from collections import defaultdict
from typing import List

# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
# T: O(N)
# S: O(N)

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_to_index_mapping = defaultdict(int)

        current_sum = 0
        max_len = 0

        sum_to_index_mapping[0] = -1

        for i in range(len(nums)):
            current_sum += nums[i]

            if (current_sum - k) in sum_to_index_mapping:
                max_len = max(max_len, i - sum_to_index_mapping[current_sum - k])

            # store cumulative sum in dict, only if its not seen
            if current_sum not in sum_to_index_mapping:
                sum_to_index_mapping[current_sum] = i

        return max_len

if __name__ == '__main__':
    nums = [1,-1,5,-2,3]
    k = 3
    print(Solution().maxSubArrayLen(nums, k)) # 4

    nums = [-2,-1,2,1]
    k = 1
    print(Solution().maxSubArrayLen(nums, k)) # 2