from typing import List

# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/
# T: O(NLOGN)
# S: O(N)

def maximum_total_sum(maximum_height: List[int]) -> int:
    # sort the array
    maximum_height = sorted(maximum_height, reverse=True)

    max_sum_heights = maximum_height[0]
    for i in range(1, len(maximum_height)):
        # the current height would the min of the max of the current height or -1 from its previous neighbor
        maximum_height[i] = min(maximum_height[i], maximum_height[i - 1] - 1)
        if maximum_height[i] <= 0:
            return -1
        max_sum_heights += maximum_height[i]

    return max_sum_heights

if __name__ == '__main__':
    print(maximum_total_sum([2,3,4,3])) # 10
    print(maximum_total_sum([15,10])) # 25
    print(maximum_total_sum([2,2,1])) # -1