from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        root = self

        result = []
        if not root:
            return ""

        # store nodes for each level in a queue
        queue = deque()

        # store the first node to the queue
        queue.append(root)

        while queue:
            size_level = len(queue)
            level_list = []

            for _ in range(size_level):
                current = queue.popleft()

                level_list.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            result.extend(level_list)

        return str(result)


def list_to_tree(lst):
    if not lst:
        return None

    def helper(index):
        if index < len(lst) and lst[index] is not None:
            node = TreeNode(lst[index])
            node.left = helper(2 * index + 1)
            node.right = helper(2 * index + 2)
            return node
        return None

    return helper(0)
