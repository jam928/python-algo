from collections import deque

from leetcode.trees.tree_node import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # encode the binary tree by , via preorder traveral
        def seralize_helper(root):
            if not root:
                return "X:"

            return f"{root.val}:{seralize_helper(root.left)}{seralize_helper(root.right)}"

        return seralize_helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # construct the tree via preorder traversal
        def deserialize_helper(q):
            if len(q) == 0:
                return None
            val = q.popleft()
            if val == 'X':
                return None
            node = TreeNode(int(val))
            node.left = deserialize_helper(q)
            node.right = deserialize_helper(q)

            return node

        data_list = data.split(':')
        q = deque(data for data in data_list)
        return deserialize_helper(q)

if __name__ == '__main__':
    codec = Codec()
    bt = TreeNode(1)
    bt.left = TreeNode(2)
    bt.right = TreeNode(3)
    bt.right.left = TreeNode(4)
    bt.right.right = TreeNode(5)

    serialized_data = codec.serialize(bt)
    print(f"Serialized data: {serialized_data}")
    print(f"Deserialized data: {codec.deserialize(serialized_data)}")