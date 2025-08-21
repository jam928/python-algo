from typing import Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/convert-bst-to-greater-tree/
# T: O(N)
# S: O(H)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root, n):
            if not root:
                return n # return cumulative sum if node is null
            
            right_subtree = helper(root.right, n)

            # update current node's value by adding accumlated sum
            root.val += right_subtree

            # traverse left subtree with updated sum
            return helper(root.left, root.val)

        helper(root, 0)
        return root
            