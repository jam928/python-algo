from typing import List

# T: O(n)
# S: O(1)
# https://leetcode.com/problems/gas-station/


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    # if the sum of the gas is less than the sum of cost then no solution will exist
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])

        # this position is not going to work, so try next possible position
        if total < 0:
            total = 0
            start = i + 1

    return start


print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # 3
print(can_complete_circuit([2, 3, 4], [3, 4, 3]))  # -1
