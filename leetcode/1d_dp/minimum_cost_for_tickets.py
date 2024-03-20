from typing import List


def min_cost_tickets(days: List[int], costs: List[int]) -> int:
    memo = {}

    def helper(index):
        if index >= len(days):
            return 0

        if index in memo:
            return memo[index]

        min_cost = float('inf')

        # one day pass
        min_cost = min(min_cost, costs[0] + helper(index + 1))

        # one week pass
        till_day = days[index] + 7
        till_index = index
        while till_index < len(days) and days[till_index] < till_day:
            till_index += 1
        min_cost = min(min_cost, costs[1] + helper(till_index))

        # one month pass
        till_day = days[index] + 30
        till_index = index
        while till_index < len(days) and days[till_index] < till_day:
            till_index += 1
        min_cost = min(min_cost, costs[2] + helper(till_index))

        memo[index] = min_cost
        return memo[index]

    return helper(0)


print(min_cost_tickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))  # 11
print(min_cost_tickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))  # 17
