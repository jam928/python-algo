# https://leetcode.com/problems/clone-graph/
from collections import deque
from typing import Optional

from leetcode.graph.node import Node


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    hashmap = {}

    def dfs(node):
        if not node:
            return node

        if node.val in hashmap:
            return hashmap[node.val]

        copy = Node(node.val)

        hashmap[copy.val] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node2.neighbors.append(node3)
node3.neighbors.append(node2)
node3.neighbors.append(node4)
node4.neighbors.append(node1)
node4.neighbors.append(node3)

print(clone_graph(node1)) # [[2,4],[1,3],[2,4],[1,3]]