from typing import Optional

from leetcode.trees.tree_node import TreeNode


# https://leetcode.com/problems/validate-binary-search-tree/

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    stack = []
    result = [True]

    def helper(root):
        if not root:
            return

        helper(root.left)
        if stack:
            last_value = stack.pop()
            if last_value >= root.val:
                result[0] = False
        stack.append(root.val)
        helper(root.right)

    helper(root)

    return result[0]


bt = TreeNode(2)
bt.left = TreeNode(1)
bt.right = TreeNode(3)

print(is_valid_bst(bt))  # true

bt2 = TreeNode(5)
bt2.left = TreeNode(1)
bt2.right = TreeNode(4)
bt2.right.left = TreeNode(3)
bt2.right.right = TreeNode(6)

print(is_valid_bst(bt2))  # false
