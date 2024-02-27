# https://leetcode.com/problems/clone-graph/
from collections import deque
from typing import Optional

from leetcode.graph.node import Node


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return node

    # store visited nodes
    visited = {}
    new_node = Node(node.val)
    visited[node.val] = new_node  # store node.val -> node

    q = deque()
    q.append(node)

    while len(q) != 0:
        curr = q.popleft()
        # iterate though curr neighbors'
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = Node(neighbor.val)
                q.append(neighbor)
            visited[curr.val].neighbors.append(visited[neighbor.val])

    return new_node

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