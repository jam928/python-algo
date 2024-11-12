from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root

    # traverse left then right
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # if the left & right are not null
    # that means we found p & q LCA node
    if left and right:
        return root

    return left if left else right

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    p = root.left
    q = root.right

    print(lowest_common_ancestor(root, p, q).val)