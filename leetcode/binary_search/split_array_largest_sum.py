from typing import List

# https://leetcode.com/problems/split-array-largest-sum/description/
# T: O(N * LOG(S)) where s largest potential sum
# S: O(1)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        result = float('inf')

        while left <= right:
            mid = (left + right) // 2

            num_of_subarrays = 1
            subarray_sum = 0

            for num in nums:
                if num + subarray_sum <= mid:
                    subarray_sum += num
                else:
                    num_of_subarrays += 1
                    subarray_sum = num

            if num_of_subarrays <= k:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.splitArray(nums = [7,2,5,10,8], k = 2)) # 18
    print(s.splitArray(nums = [1,2,3,4,5], k = 2)) # 9

