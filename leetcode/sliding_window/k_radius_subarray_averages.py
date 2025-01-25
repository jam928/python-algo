from typing import List

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        result = [0] * n
        current_sum = 0

        for i in range(n):
            if i < k:
                result[i] = -1  # elements less than k before

            current_sum += nums[i]

            # if we are within range compute average at i-k
            if i >= 2 * k:
                result[i - k] = (current_sum // (2 * k + 1))
                current_sum -= nums[i - 2 * k]

            if i >= n - k:
                result[i] = -1  # elements less than k after

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3)) # [-1,-1,-1,5,4,4,-1,-1,-1]
    print(s.getAverages(nums = [100000], k = 0)) # [100000]
    print(s.getAverages(nums = [8], k = 100000)) # [-1]
