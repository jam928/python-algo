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
                return "None,"

            return f"{root.val},{seralize_helper(root.left)}{seralize_helper(root.right)}"

        return seralize_helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # construct the tree via preorder traversal
        def deserialize_helper(data_list):
            val = data_list.pop(0)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = deserialize_helper(data_list)
            node.right = deserialize_helper(data_list)

            return node

        data_list = data.split(',')
        return deserialize_helper(data_list[:-1])

if __name__ == '__main__':
    codec = Codec()
    bt = TreeNode(1)
    bt.left = TreeNode(2)
    bt.right = TreeNode(3)
    bt.right.left = TreeNode(4)
    bt.right.right = TreeNode(5)

    serialized_data = codec.serialize(bt)
    print(f"Serialized data: {serialized_data}")
    print(codec.deserialize(serialized_data))