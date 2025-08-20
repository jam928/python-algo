from collections import defaultdict
from typing import List

# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# T: O(N)
# S: O(N)

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)

        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))

        def dfs(node):
            result = 0
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                
                if (node, neighbor) in roads: # this is the edge we need to constuct
                    result += 1

                visited.add(neighbor)
                result += dfs(neighbor)

            return result

        visited = set([0])
        return dfs(0)
        
if __name__ == '__main__':
    s = Solution()
    assert s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3
    assert s.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]) == 2
    assert s.minReorder( n = 3, connections = [[1,0],[2,0]]) == 0

