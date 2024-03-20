from collections import defaultdict


# T: O(V+E)
# S: O(V)
class ConnectedComponents:

    def __dfs(self, arr, v, visited, edge_map):
        if visited[v]:
            return

        visited[v] = True
        arr.append(v)

        for neighbor in edge_map[v]:
            if visited[neighbor]:
                continue
            self.__dfs(arr, neighbor, visited, edge_map)

    def connected_components(self, edges, n):
        visited = [False for _ in range(n)]

        connected_graphs = []
        edge_map = defaultdict(list)

        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])

        # dfs approach
        for v in range(n):
            if visited[v]:
                continue
            connected_list = []
            self.__dfs(connected_list, v, visited, edge_map)
            connected_graphs.append(connected_list)
        return connected_graphs


if __name__ == "__main__":
    edges = [[1, 0], [2, 1], [3, 4]]
    v = 5
    count = ConnectedComponents().connected_components(edges, v)
    print(count)
