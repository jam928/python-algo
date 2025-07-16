from math import inf
from typing import Optional, List

from leetcode.trees.tree_node import TreeNode

# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> float:
        # update the max path sum globally on each node
        self.max_sum = float('-inf')

        def helper(root):
            if not root:
                return 0

            # retrieve the left and right max path sum recursively
            # do not include negative that why we compare max with zero
            left_max_sum = max(helper(root.left), 0)
            right_max_sum = max(helper(root.right), 0)

            # update the max sum
            self.max_sum = max(self.max_sum, left_max_sum + root.val + right_max_sum)

            # return the max of either left or right subtree + curr val
            return max(left_max_sum, right_max_sum) + root.val

        helper(root)

        return self.max_sum

    def maxPathSumWithPath(self, root: Optional[TreeNode]) -> List[int]:
        # update the max path sum globally on each node
        self.max_sum = float('-inf')
        self.max_path_arr = []

        def find_max_path_sum(node):
            # bas case
            if not node:
                return 0, []

            # recursively go left and right path sums
            left_sum, left_path = find_max_path_sum(node.left)
            right_sum, right_path = find_max_path_sum(node.right)

            # Calculate possible sums
            paths = [
                (node.val, [node.val]),
                (node.val + left_sum, [node.val] + left_path),
                (node.val + right_sum, [node.val] + right_path),
                (node.val + left_sum + right_sum, left_path + [node.val] + right_path)
            ]

            # find the best path for the current node
            max_single, best_path = max(paths, key=lambda x: x[0])

            # update global maximum and path if needed
            if max_single > self.max_sum:
                self.max_sum = max_single
                self.max_path_arr = best_path

            # check if full path (left + curr + right) is better
            # if paths[-1][0] > self.max_sum:
            #     self.max_sum = paths[-1][0]
            #     self.max_path_arr = paths[-1][1]

            return max_single, best_path

        find_max_path_sum(root)
        return self.max_path_arr

if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.maxPathSum(root)) # 42
    print(sol.maxPathSumWithPath(root)) # [15, 20, 7]

    root = TreeNode(9)
    root.left = TreeNode(6)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(-6)
    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(2)
    root.right.right.left.left = TreeNode(-6)
    root.right.right.left.left.left = TreeNode(-6)
    root.right.right.left.right = TreeNode(-6)

    print(sol.maxPathSum(root)) # 16
    print(sol.maxPathSumWithPath(root)) # [6, -3, 2, -6, -6, -6, -6]