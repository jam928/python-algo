from typing import Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    result = []

    def helper(root):
        if not root:
            return

        helper(root.left)
        result.append(root.val)
        helper(root.right)

    helper(root)
    return result[k - 1]

tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.left.right = TreeNode(2)

print(kth_smallest(tree, 1)) # 1

tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right = TreeNode(6)
tree.left.right = TreeNode(4)
tree.left.left = TreeNode(2)
tree.left.left.left = TreeNode(1)

print(kth_smallest(tree, 3)) # 3