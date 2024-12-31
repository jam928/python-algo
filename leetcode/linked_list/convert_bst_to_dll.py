from leetcode.trees.tree_node import TreeNode

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def bst_to_dll(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Helper function to perform the in-order traversal of the tree.
        def in_order_traverse(node):
            # Base case: if the node is None, return to the previous call.
            if node is None:
                return

            # Recursive case: traverse the left subtree.
            in_order_traverse(node.left)

            # Process the current node.
            if self.previous:
                # Link the previous node with the current node from the left.
                self.previous.right = node
                # Link the current node with the previous node from the right.
                node.left = self.previous
            else:
                # If this node is the leftmost node, it will be the head of the doubly linked list.
                self.head = node
            # Mark the current node as the previous one before the next call.
            self.previous = node

            # Recursive case: traverse the right subtree.
            in_order_traverse(node.right)

        # If the input tree is empty, return None.
        if root is None:
            return None

        # Initialize the head and previous pointer used during the in-order traversal.
        self.head = self.previous = None
        # Perform the in-order traversal to transform the tree to a doubly linked list.
        in_order_traverse(root)
        # Connect the last node visited (previous) with the head of the list to make it circular.
        self.previous.right = self.head
        self.head.left = self.previous

        # Return the head of the doubly linked list.
        return self.head

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    dll = Solution().bst_to_dll(root)

    s = set()
    arr = []
    while dll not in s:
        s.add(dll)
        arr.append(dll.value)
        dll = dll.right

    print(arr)