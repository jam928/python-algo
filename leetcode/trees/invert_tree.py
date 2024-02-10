from typing import Optional

from leetcode.trees.tree_node import TreeNode


# https://leetcode.com/problems/invert-binary-tree/description/

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # post order traversal recursive
    if not root:
        return root

    # Deep traverse left & right
    left_node = invert_tree(root.left)
    right_node = invert_tree(root.right)

    # swap nodes
    root.left = right_node
    root.right = left_node

    return root


bt = TreeNode(4)
bt.left = TreeNode(2)
bt.left.left = TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(6)
bt.right.right = TreeNode(9)

print(invert_tree(bt))  # [4, 7, 2, 9, 6, 3, 1]

bt2 = TreeNode(2)
bt2.left = TreeNode(1)
bt2.right = TreeNode(3)

print(invert_tree(bt2))  # [2, 3, 1]
