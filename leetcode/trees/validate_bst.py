from typing import Optional

from leetcode.trees.tree_node import TreeNode


# https://leetcode.com/problems/validate-binary-search-tree/

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    stack = []
    curr = root
    highest = float('-inf')
    while True:
        # iterate all to the left and appending current node to stack
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            # if stack empty break
            if not stack:
                break
            curr = stack.pop()
            # if the current val is greater the highest recorded val update highest
            if curr.val > highest:
                highest = curr.val
            else:
                # return false the current val is less than last node so not valid BST
                return False
            curr = curr.right
    return True


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
