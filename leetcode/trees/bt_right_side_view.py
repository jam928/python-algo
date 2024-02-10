from collections import deque
from typing import Optional, List

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/binary-tree-right-side-view/

def right_side_view(root: Optional[TreeNode]) -> List[int]:
    # level order traversal; on each level store the last node in the list

    result = []

    if not root:
        return []

    # store each level nodes in queue
    queue = deque()

    # append first node in queue
    queue.append(root)

    # iterate till we have no more elements in the queue
    while queue:
        # iterate the size of the level and append its child for the next iteration
        size_level = len(queue)

        # the last element value will be the last element in the level
        last_element = -1
        for i in range(size_level):
            current = queue.popleft()

            last_element = current.val

            # append its children for next level iteration
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        result.append(last_element)

    return result

bt = TreeNode(1)
bt.left = TreeNode(2)
bt.left.right = TreeNode(5)
bt.right = TreeNode(3)
bt.right.right = TreeNode(4)

print(right_side_view(bt))

bt2 = TreeNode(1)
bt2.right = TreeNode(3)

print(right_side_view(bt2))

