from collections import deque
from typing import Optional, List

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/binary-tree-level-order-traversal/

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []

    # store nodes for each level in a queue
    queue = deque()

    # store the first node in a queue
    queue.append(root)

    # iterate till queue is empty
    while queue:
        size_level = len(queue)

        # add each size level elements in list
        level_list = []

        for i in range(size_level):
            current = queue.popleft()

            level_list.append(current.val)

            # add its children to the queue for next level iteration
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        result.append(level_list)

    return result

bt = TreeNode(3)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)

print(level_order(bt)) # [[3], [9, 20], [15, 7]]

bt = TreeNode(1)

print(level_order(bt)) # [[1]]