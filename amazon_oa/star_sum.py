from collections import defaultdict


def max_total_value(cities, connections, from_city, to_city, values, k):
    """
    :type cities: int
    :type connections: int
    :type from_city: List[int]
    :type to_city: List[int]
    :type values: List[int]
    :type k: int
    :rtype: int
    """
    graph = defaultdict(list)
    for i in range(connections):
        graph[from_city[i]].append((to_city[i], values[to_city[i] -1]))
        graph[to_city[i]].append((from_city[i], values[from_city[i] - 1]))

    max_total_value = float('-inf')

    for city in range(1, cities + 1):
        current = graph[city]

        max_value = values[city - 1]
        current_sum = values[city - 1]

        # sort the current list by greatest to least
        current.sort(key = lambda x: x[1], reverse=True)

        count = 0
        for neighbor, val in current:
            if count == k:
                break
            count += 1
            current_sum += values[neighbor - 1]
            max_value = max(max_value, current_sum)

        max_total_value = max(max_total_value, max_value)

    return max_total_value

cities = 7
connections = 8
from_city  = [2,3,4,4,5,5,6,1]
to_city = [5,6,5,1,6,7,7,7]
values = [-30,-20,15,30,-10,5,20]
k = 3
print(max_total_value(cities, connections, from_city, to_city, values, k))