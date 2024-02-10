from typing import Optional

from leetcode.trees.tree_node import TreeNode


# https://leetcode.com/problems/diameter-of-binary-tree/

def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    # update the max diameter globally on each node
    max_diameter = [-1]

    def find_diameter_helper(root):
        if not root:
            return 0

        left_diameter = find_diameter_helper(root.left)
        right_diameter = find_diameter_helper(root.right)

        max_diameter[0] = max(max_diameter[0], left_diameter + right_diameter)

        # return the max of either left or right subtrees plus one
        return max(left_diameter, right_diameter) + 1

    find_diameter_helper(root)
    return max_diameter[0]


bt = TreeNode(1)
bt.left = TreeNode(2)
bt.left.left = TreeNode(4)
bt.left.right = TreeNode(5)
bt.right = TreeNode(3)

print(diameter_of_binary_tree(bt))  # 3

bt2 = TreeNode(1)
bt2.left = TreeNode(2)

print(diameter_of_binary_tree(bt2)) # 1
