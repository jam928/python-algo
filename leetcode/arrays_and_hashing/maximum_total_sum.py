from typing import List

# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/
# T: O(NLOGN)
# S: O(N)

def maximum_total_sum(maximumHeight: List[int]) -> int:
    # sort the array
    maximumHeight = sorted(maximumHeight, reverse=True)

    max_sum_heights = maximumHeight[0]
    for i in range(1, len(maximumHeight)):
        # the current height would the min of the max of the current height or -1 from its previous neighbor
        maximumHeight[i] = min(maximumHeight[i], maximumHeight[i - 1] - 1)
        if maximumHeight[i] <= 0:
            return -1
        max_sum_heights += maximumHeight[i]

    return max_sum_heights