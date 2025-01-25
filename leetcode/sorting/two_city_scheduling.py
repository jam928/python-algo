from typing import List

# https://leetcode.com/problems/two-city-scheduling/description/
# T: O(N LOG N)
# S: O(N)

def two_city_sched_cost(costs: List[List[int]]) -> int:
    # get the total costs for city a
    total_city_a_costs = 0
    refunds_city_b = []

    for cost in costs:
        total_city_a_costs += cost[0]
        # compute the refunds if were to pick city b for each of the ticket
        refunds_city_b.append(cost[1] - cost[0])

        # sort the refunds array to get possible refunds
    refunds_city_b.sort()

    # get the first n/2 higest refunds in array and use that to subtract from total_city_a_costs
    min_cost = total_city_a_costs + sum(refunds_city_b[0:len(refunds_city_b) // 2])

    return min_cost

if __name__ == '__main__':
    print(two_city_sched_cost([[10,20],[30,200],[400,50],[30,20]])) # 110
    print(two_city_sched_cost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])) # 1859
    print(two_city_sched_cost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]])) # 3086