
# T: O(N*M) where n is the length of bt and m is the length of ll
# S: O(N+M) where n is the length of bt and m is the length of ll
# https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if self.dfs(head, root):
            return True
        if not root:
            return False
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, list_node, tree_node):
        if not list_node:
            return True
        if not tree_node or list_node.val != tree_node.val:
            return False
        return self.dfs(list_node.next, tree_node.left) or self.dfs(list_node.next, tree_node.right)