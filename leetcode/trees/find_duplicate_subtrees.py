# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from leetcode.trees.tree_node import TreeNode

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/find-duplicate-subtrees/
def find_duplicate_subtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    subtrees = {}

    duplicates = []

    def serializer(node):
        if not node:
            return ''

        left_path = serializer(node.left)
        right_path = serializer(node.right)

        path = f'{node.val},{left_path},{right_path}'
        subtrees[path] = subtrees.get(path, 0) + 1

        if subtrees[path] == 2:
            duplicates.append(node)

        return path

    serializer(root)
    return duplicates

if __name__ == '__main__':
    bt = TreeNode(1)
    bt.left = TreeNode(2)
    bt.left.left = TreeNode(4)
    bt.right = TreeNode(3)
    bt.right.left = TreeNode(2)
    bt.right.left.left = TreeNode(4)
    bt.right.right = TreeNode(4)

    duplicate_subtrees = find_duplicate_subtrees(bt)
    print(f'{duplicate_subtrees}')