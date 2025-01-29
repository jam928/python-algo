from typing import List


# T: O(N LOG S)
# S: O(1)
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = 1
        right = max(bloomDay)
        while left < right:
            days = (left + right) // 2

            flowers = bouquets = 0

            for day in bloomDay:
                flowers = flowers + 1 if day <= days else 0

                if flowers == k:
                    bouquets += 1
                    if bouquets == m:
                        break
                    flowers = 0

            if bouquets == m:
                right = days
            else:
                left = days + 1

        return left

if __name__ == '__main__':
    solution = Solution()
    print(solution.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1)) # 3
    print(solution.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2)) # -1
    print(solution.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3)) # 12