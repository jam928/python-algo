from collections import defaultdict
from typing import List

from leetcode.trees.tree_node import TreeNode

# T: O(NLOGN)
# S: O(N)
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
class Solution:

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        cache = defaultdict(list)

        def helper(root, horiz_dist, level):
            if not root:
                return

            cache[horiz_dist].append((root.val, level))

            # store nodes in left subtree
            helper(root.left, horiz_dist - 1, level + 1)

            # store nodes in right subtree
            helper(root.right, horiz_dist + 1, level + 1)

        helper(root, 0, 0)
        keys = cache.keys()
        min_horiz_dist = min(keys)
        max_horiz_dist = max(keys)

        result = []

        for dist in range(min_horiz_dist, max_horiz_dist + 1):
            # sort list by level for each of the horizontal distances
            arr = sorted(cache[dist], key = lambda x: x[1])
            arr = list(map(lambda x: x[0], arr))
            result.append(arr)

        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.right = TreeNode(9)

    print(Solution().verticalOrder(root))