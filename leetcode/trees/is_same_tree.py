from typing import Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/same-tree/

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # if both are null then we exhausted all nodes in both trees so return true
    if p is None and q is None:
        return True

    # if p is null but q is not or vice verse return false
    if (p and q is None) or (p is None and q):
        return False

    # if p val is not equal to q val return false
    if p.val != q.val:
        return False

    # if p left subtree is not the same as q left subtree return false;
    # do same for right subtree
    left_subtrees = is_same_tree(p.left, q.left)
    right_subtrees = is_same_tree(p.right, q.right)

    return True if left_subtrees and right_subtrees else False

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(is_same_tree(p,q)) # true

p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

print(is_same_tree(p,q)) # true

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)

q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(2)

print(is_same_tree(p,q)) # false