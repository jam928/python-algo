from typing import Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/binary-tree-pruning/description/
# T: O(N)
# S: O(N)

def prune_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    # LRD
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)

    # remove node if zero and its a leaf node
    if not root.left and not root.right and root.val == 0:
        return None

    return root

if __name__ == '__main__':
