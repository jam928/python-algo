from collections import deque, defaultdict
from typing import List


# https://leetcode.com/problems/evaluate-division/description/

# T: O(n) + O(m * (V+E)) # where n is the adj list and m is number of queries
# S: O(n) + O(V)


def calc_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adj_list = defaultdict(list)

    for i in range(len(values)):
        equation = equations[i]
        adj_list[equation[0]].append((equation[1], values[i]))
        adj_list[equation[1]].append((equation[0], 1 / values[i]))

    result = []
    for query in queries:
        result.append(bfs(query[0], query[1], adj_list))

    return result


def bfs(from_node, to_node, adj_list):
    if from_node not in adj_list:
        return -1

    q = deque()
    visited = set()
    q.append((from_node, 1.0))

    while q:
        (current_node, current_number) = q.popleft()

        if current_node == to_node:
            return current_number

        visited.add(current_node)

        for (other_node, other_number) in adj_list[current_node]:
            if other_node in visited:
                continue
            q.append((other_node, current_number * other_number))

    return -1.0


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calc_equation(equations, values, queries))  # [6.00000,0.50000,-1.00000,1.00000,-1.00000]

    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    print(calc_equation(equations, values, queries))  # [3.75000,0.40000,5.00000,0.20000]

    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(calc_equation(equations, values, queries))  # [0.50000,2.00000,-1.00000,-1.00000]
