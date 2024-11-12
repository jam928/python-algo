from collections import defaultdict
from typing import List

from leetcode.trees.tree_node import TreeNode

class Solution:

    def vertical_traversal(self, root: TreeNode) -> List[List[int]]:
        cache = defaultdict(list)

        def helper(root, horiz_dist):
            if not root:
                return

            cache[horiz_dist].append(root.val)

            # store nodes in left subtree
            helper(root.left, horiz_dist - 1)

            # store nodes in right subtree
            helper(root.right, horiz_dist + 1)

        helper(root, 0)
        keys = cache.keys()
        min_horiz_dist = min(keys)
        max_horiz_dist = max(keys)

        result = []

        for dist in range(min_horiz_dist, max_horiz_dist + 1):
            result.append(cache[dist])

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

    print(Solution().vertical_traversal(root))