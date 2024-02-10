from leetcode.trees.tree_node import TreeNode, list_to_tree


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # if the root is b/t p and q then the root must be the LCA
    if (p and q and root) and ((p.val <= root.val <= q.val) or (q.val <= root.val <= p.val)):
        return root

    # recursively go left if the current node value is too high for p & q
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)

    # o.w go right
    return lowest_common_ancestor(root.right, p, q)


lst = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
bt = list_to_tree(lst)
p = TreeNode(2)
q = TreeNode(8)
print(lowest_common_ancestor(bt, p, q))  # 6

p = TreeNode(2)
q = TreeNode(4)
print(lowest_common_ancestor(bt, p, q))  # 2
