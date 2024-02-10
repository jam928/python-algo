from typing import Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/balanced-binary-tree/

def is_balanced(root: Optional[TreeNode]) -> bool:
    # keep track of depth of each node in a global var
    is_balanced = [True]

    def is_balanced_helper(root):
        if not root:
            return 0

        # get the left and right subdepth
        left_depth = is_balanced_helper(root.left)
        right_depth = is_balanced_helper(root.right)

        # update is balanced var
        diff = abs(left_depth - right_depth)
        if diff > 1:
            is_balanced[0] = False

        # return max
        return max(left_depth, right_depth) + 1

    is_balanced_helper(root)
    return is_balanced[0]

bt = TreeNode(3)
bt.left = TreeNode(9)
bt.right = TreeNode(20)
bt.right.left = TreeNode(15)
bt.right.right = TreeNode(7)

print(is_balanced(bt)) # true

bt2 = TreeNode(1)
bt2.left = TreeNode(2)
bt2.left.left = TreeNode(3)
bt2.left.right = TreeNode(3)
bt2.left.left.left = TreeNode(4)
bt2.left.left.right = TreeNode(4)
bt2.right = TreeNode(2)

print(is_balanced(bt2)) # false