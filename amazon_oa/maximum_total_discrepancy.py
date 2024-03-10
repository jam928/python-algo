from collections import defaultdict


def maximum_total_disc(n, edges, from_node, to_node, weight):
    graph = defaultdict(list)

    for i in range(edges):
        graph[from_node[i]].append((to_node[i], weight[to_node[i] - 1]))
        graph[to_node[i]].append((from_node[i], weight[from_node[i] - 1]))

    max_total_disc = float('-inf')
    for node in range(1, n + 1):
        visited = set()
        max_discrepancy = dfs(visited, node, 0, graph, weight)
        max_total_disc = max(max_total_disc, max_discrepancy)

    return max_total_disc


def dfs(visited, node, distance, graph, weight):
    if node in visited:
        return 0

    visited.add(node)
    max_disc = distance * weight[node - 1]

    for neighbor, val in graph[node]:
        max_disc += dfs(visited, neighbor, distance + 1, graph, weight)

    visited.remove(node)

    return max_disc


n = 5
edges = 4
from_node = [1, 2, 2, 1]
to_node = [2, 3, 5, 4]
weight = [2, 1, 4, 2, 3]

print(maximum_total_disc(n, edges, from_node, to_node, weight))
