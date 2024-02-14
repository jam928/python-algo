from math import inf
from typing import Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

def max_path_sum(root: Optional[TreeNode]) -> int:
    # update the max path sum globally on each node
    max_sum = [float(-inf)]

    def helper(root):
        if not root:
            return 0

        # retrieve the left and right max path sum recursively
        # do not include negative that why we compare max with zero
        left_max_sum = max(helper(root.left), 0)
        right_max_sum = max(helper(root.right), 0)

        # update the max sum
        max_sum[0] = max(max_sum[0], left_max_sum + root.val + right_max_sum)

        # return the max of either left or right subtree + curr val
        return max(left_max_sum, right_max_sum) + root.val

    helper(root)

    return max_sum[0]

bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)

print(max_path_sum(bt)) # 6

bt = TreeNode(-10)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)

print(max_path_sum(bt)) # 42