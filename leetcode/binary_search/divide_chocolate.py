from typing import List

# https://leetcode.com/problems/divide-chocolate/
# T: O(N LOG S) where s is total sweetness
# S: O(1)

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left = 1
        right = sum(sweetness) // (k + 1)

        while left < right:
            mid = (left + right + 1) // 2

            num_of_subarrays = 0
            subarray_sum = 0

            for num in sweetness:
                subarray_sum += num
                if subarray_sum >= mid: # if it's greater than mid then we must split
                    num_of_subarrays += 1
                    subarray_sum = 0

            if num_of_subarrays > k:
                left = mid
            else:
                right = mid - 1
        return right