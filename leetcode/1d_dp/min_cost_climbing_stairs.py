from typing import List

# https://leetcode.com/problems/min-cost-climbing-stairs/
# T: O(N)
# S: O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            # get the min cost from last step or last two steps
            cost[i] = min(cost[i] + cost[i - 1], cost[i] + cost[i - 2])

        # get the min cost from last 2 elements in the array
        return min(cost[len(cost) - 1], cost[len(cost) - 2])

if __name__ == '__main__':
    s = Solution()
    assert s.minCostClimbingStairs([10,15,20]) == 15
    assert s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6
