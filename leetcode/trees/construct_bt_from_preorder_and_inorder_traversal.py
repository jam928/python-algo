from typing import List, Optional

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # if either arrays are empty, it means we exhausted all nodes to traverse
    # so return none saying empty subtree
    if not preorder or not inorder:
        return None

    # the first element of the preorder array represents the value of the curr root node
    root_val = preorder[0]
    root = TreeNode(root_val)

    # find the root val's position in the inorder traveral
    # this indicates that left to the index is the left subtree
    # and to the right of the index is the right subtree
    root_index = inorder.index(root_val)

    # left subtree can be constructed from 1 to root_index + 1(pre order)
    # anything after root index for inorder
    root.left = build_tree(preorder[1:root_index + 1], inorder[:root_index])

    # right subtree can be constructed from root_index + 1 to the end(for both array's)
    root.right = build_tree(preorder[root_index + 1:], inorder[root_index + 1:])

    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

print(build_tree(preorder, inorder)) # [3,9,20,null,null,15,7]


preorder = [-1]
inorder = [-1]

print(build_tree(preorder, inorder)) # [-1]
