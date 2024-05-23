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

def max_path_sum_2(root: Optional[TreeNode]) -> str:
    # Initialize variables to store the maximum path sum and path
    max_sum = float('-inf')
    max_path = []

    def dfs(node):
        nonlocal max_sum, max_path

        if not node:
            return 0, []

        # Recursively get the max sum and path for left and right subtrees
        left_sum, left_path = dfs(node.left)
        right_sum, right_path = dfs(node.right)

        # Calculate the maximum single path sum including the current node
        max_single = max(left_sum + node.val, right_sum + node.val, node.val)

        # Calculate the maximum sum as a path that passes through the current node
        max_top = max(max_single, left_sum + node.val + right_sum)

        # Update the max_sum and max_path if needed
        if max_top > max_sum:
            max_sum = max_top
            possible_paths_map = {
                left_sum + node.val + right_sum: left_path + [node.val] + right_path,
                left_sum + node.val: left_path + [node.val],
                right_sum + node.val: [node.val] + right_path
            }
            max_path += possible_paths_map.get(max_top, node.val)

        # Return the maximum path sum including the current node and the path
        path = left_path if left_sum > right_sum else right_path
        return max_single, path

    # Start the DFS traversal
    dfs(root)

    return max_sum, max_path

bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)

# print(max_path_sum(bt)) # 6
print(max_path_sum_2(bt))

bt = TreeNode(-10)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)

# print(max_path_sum(bt)) # 42
print(max_path_sum_2(bt))