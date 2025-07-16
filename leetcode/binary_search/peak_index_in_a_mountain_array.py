from typing import List

# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# T: O(LOGN)
# S: O(1)


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            # if peak return this mid point
            if (0 < mid < len(arr) - 1) and arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid

            if mid > 0 and arr[mid - 1] > arr[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return 0

if __name__ == '__main__':
    s = Solution()
    assert s.peakIndexInMountainArray(arr = [0,1,0]) == 1
    assert s.peakIndexInMountainArray(arr=[0,2,1,0]) == 1
    assert s.peakIndexInMountainArray(arr=[0,10,5,2]) == 1