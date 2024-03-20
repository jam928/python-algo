from typing import List

# T: O(E * V) where e is the number of edges and v number of vertices
# S: O(V) # where v is the number of vertices

# https://leetcode.com/problems/redundant-connection/description/
class FindRedundantConnection:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        for edge in edges:
            if self.__find(parent, edge[0]) == self.__find(parent, edge[1]):
                return edge
            else:
                self.__union(parent, edge[0], edge[1])

        return edges[0]

    def __find(self, parent, v):
        if parent[v] == v:
            return parent[v]
        return self.__find(parent, parent[v])

    def __union(self, parent, u, v):
        parent1 = self.__find(parent, u)
        parent2 = self.__find(parent, v)
        parent[parent2] = parent1


if __name__ == '__main__':
    frd = FindRedundantConnection()
    print(frd.find_redundant_connection(edges=[[1, 2], [1, 3], [2, 3]]))  # [2,3]
    # print(frd.find_redundant_connection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]])) # [1,4]
