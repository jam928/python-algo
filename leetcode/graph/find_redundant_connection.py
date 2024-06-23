from collections import defaultdict
from typing import List

# T: O(E * V) where e is the number of edges and v number of vertices
# S: O(V) # where v is the number of vertices

# https://leetcode.com/problems/redundant-connection/description/
class FindRedundantConnection:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        # Function to perform DFS to check if adding an edge will form a cycle
        def dfs(source, target):
            if source in visited:
                return False

            visited.add(source)
            if source == target:
                return True
            return any(dfs(neighbor, target) for neighbor in graph[source])

        # Create a graph as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            visited = set()
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)


if __name__ == '__main__':
    frd = FindRedundantConnection()
    print(frd.find_redundant_connection(edges=[[1, 2], [1, 3], [2, 3]]))  # [2,3]
    # print(frd.find_redundant_connection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]])) # [1,4]
