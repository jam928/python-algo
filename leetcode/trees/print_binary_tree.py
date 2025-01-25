from typing import Optional, List
from leetcode.trees.tree_node import TreeNode
# T:O(2^N)
# S:O(2^N)
# https://leetcode.com/problems/print-binary-tree/
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def get_height(node):
            if not node:
                return 0

            return 1 + max(get_height(node.left), get_height(node.right))

        def update_matrix(root, matrix, row, left, right):
            if not root:
                return

            mid = (left + right) // 2
            matrix[row][mid] = str(root.val)
            update_matrix(root.left, matrix, row + 1, left, mid - 1)
            update_matrix(root.right, matrix, row + 1, mid + 1, right)

        # get height of tree
        height = get_height(root)

        # calculate width
        width = 2 ** height - 1

        # create matrix
        matrix = [['' for _ in range(width)] for _ in range(height)]

        # update matrix
        update_matrix(root, matrix, 0, 0, width - 1)

        return matrix

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().printTree(root)) # [["","1",""],["2","",""]]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)

    print(Solution().printTree(root)) # [['', '', '', '1', '', '', ''], ['', '2', '', '', '', '3', ''], ['', '', '4', '', '', '', '']]