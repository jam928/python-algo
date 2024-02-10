from typing import Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/subtree-of-another-tree/

def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # keep track of each node and see the current node structure is the same as the subroot
    is_sub_tree = [False]

    bt_root = root
    sub_root = subRoot

    def is_subtree_helper(bt_root, sub_root):
        if not bt_root:
            return

        # if the current node and the sub root node is the same val traverse both and check if they are the same
        # if they are update the global var is sub tree
        if bt_root.val == sub_root.val:
            result = is_same_tree(bt_root, sub_root)
            if result:
                is_sub_tree[0] = True
                return

        is_subtree_helper(bt_root.left, sub_root)
        is_subtree_helper(bt_root.right, sub_root)

    is_subtree_helper(bt_root, sub_root)
    return is_sub_tree[0]


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

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

sub_root = TreeNode(4)
sub_root.left = TreeNode(1)
sub_root.right = TreeNode(2)

print(is_subtree(root, sub_root)) # True

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(0)

sub_root = TreeNode(4)
sub_root.left = TreeNode(1)
sub_root.right = TreeNode(2)

print(is_subtree(root, sub_root)) # False