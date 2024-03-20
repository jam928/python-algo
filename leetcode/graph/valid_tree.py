from typing import List
from collections import defaultdict


# T: O(V+E)
# S: O(V)

def valid_tree(n: int, edges: List[List[int]]) -> bool:
    graph = defaultdict(list)

    # build the graph
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    visited = set()

    def dfs(root):
        visited.add(root)
        for node in graph[root]:
            if node in visited:
                continue
            dfs(node)
    dfs(0)
    return len(visited) == n and len(edges) == n - 1

print(valid_tree(n = 5, edges = [[0,1], [0,2], [0,3], [1,4]])) # True
print(valid_tree(n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]])) # False