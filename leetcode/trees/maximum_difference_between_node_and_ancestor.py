from typing import Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
# T: O(N)
# S: O(H)

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def helper(node):

            if not node:
                return 0

            left_subtree_min = left_subtree_max = node.val
            if node.left:
                left_subtree_min, left_subtree_max = helper(node.left)

            right_subtree_min = right_subtree_max = node.val
            if node.right:
                right_subtree_min, right_subtree_max = helper(node.right)

            self.result = max(self.result, abs(node.val - left_subtree_min), abs(node.val - left_subtree_max),
                              abs(node.val - right_subtree_min), abs(node.val - right_subtree_max))

            return min(left_subtree_min, right_subtree_min, node.val), max(left_subtree_max, right_subtree_max,
                                                                           node.val)

        helper(root)
        return self.result