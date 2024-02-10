from typing import Optional

from leetcode.trees.tree_node import TreeNode


# https://leetcode.com/problems/maximum-depth-of-binary-tree/

def max_depth(root: Optional[TreeNode]) -> int:
    # post order traversal
    if not root:
        return 0

    # traverse left and right nodes
    left_sum = max_depth(root.left)
    right_sum = max_depth(root.right)

    # get max sum of both
    max_sum = max(left_sum, right_sum) + 1

    # return max sum
    return max_sum

bt = TreeNode(3)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)

print(max_depth(bt)) # 3

bt2 = TreeNode(1)
bt2.right = TreeNode(20)

print(max_depth(bt2)) # 2
