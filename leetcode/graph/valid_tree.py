from typing import List
from collections import defaultdict


# T: O(V+E)
# S: O(V)

def valid_tree(n: int, edges: List[List[int]]) -> bool:
    if not n:
        return True

    adj_list = defaultdict(list)

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = set()

    def cycle(node, prev_node):
        if node in visited:
            return True

        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor == prev_node:
                continue
            if cycle(neighbor, node):
                return True
        return False

    return not cycle(0, -1) and len(visited) == n

print(valid_tree(n = 5, edges = [[0,1], [0,2], [0,3], [1,4]])) # True
print(valid_tree(n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]])) # False