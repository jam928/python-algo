from collections import deque
from typing import Optional, List

from leetcode.trees.tree_node import TreeNode

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque()

        q.append(root)

        result = []
        while q:
            max_node = float('-inf')

            for _ in range(len(q)):
                current = q.popleft()

                max_node = max(max_node, current.val)

                if current.left:
                    q.append(current.left)

                if current.right:
                    q.append(current.right)

            result.append(max_node)

        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)

    root.right = TreeNode(2)
    root.right.right = TreeNode(9)

    print(Solution().largestValues(root)) # [1,3,9]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(Solution().largestValues(root)) # [1,3]