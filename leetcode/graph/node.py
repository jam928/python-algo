class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def graph_to_string(self,node, visited=set()):
        if node is None:
            return ""
        if node in visited:
            return ""
        visited.add(node)
        result = "Node: " + str(node.val) + " Neighbors: " + str([neighbor.val for neighbor in node.neighbors]) + "\n"
        for neighbor in node.neighbors:
            result += self.graph_to_string(neighbor, visited)
        return result

    def __str__(self):
        return self.graph_to_string(self)