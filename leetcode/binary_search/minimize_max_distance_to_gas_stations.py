from math import ceil
from typing import List

# T: O(N LOG S)
# S: O(1)
# https://leetcode.com/problems/minimize-max-distance-to-gas-station/

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        left = pow(10, -6)
        right = stations[-1] - stations[0]

        while left + pow(10, -6) < right:
            mid = (left + right) / 2
            count = 0

            for i in range(1, len(stations)):
                count += ceil((stations[i] - stations[i - 1]) / mid) - 1

            if count > k:
                left = mid  # mid to small so lets try larger solutions
            else:
                right = mid  # lets find a bigger mid

        return right

if __name__ == "__main__":
    s = Solution()
    print(s.minmaxGasDist(stations = [1,2,3,4,5,6,7,8,9,10], k = 9)) # 0.50
    print(s.minmaxGasDist(stations = [23,24,36,39,46,56,57,65,84,98], k = 1)) # 14.00