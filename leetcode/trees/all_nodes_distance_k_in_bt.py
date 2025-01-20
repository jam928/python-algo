# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from typing import List
from leetcode.trees.tree_node import TreeNode

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution:
    # traverse through the tree till target node is found
    # once target is found then traverse the tree as a graph bfs
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # store the child mapping to its parent
        child_parent_map = {}

        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                # if we found the target then break out of the bfs traversal
                if curr.val == target.val:
                    break

                # append left and right child nodes
                if curr.left:
                    q.append(curr.left)
                    child_parent_map[curr.left] = curr

                if curr.right:
                    q.append(curr.right)
                    child_parent_map[curr.right] = curr

        result = []
        self.bfs(target, child_parent_map, result, k)
        return result

    def bfs(self, target, child_parent_map, result, k):
        q = deque()
        q.append(target)

        # use set to keep track of the visited nodes
        visited = set()

        distance = 0

        while q:
            if distance == k:
                result.extend(node.val for node in q)
                break

            for _ in range(len(q)):
                curr = q.popleft()

                if curr in visited:
                    continue

                visited.add(curr)

                if curr.left and curr.left not in visited:
                    q.append(curr.left)

                if curr.right and curr.right not in visited:
                    q.append(curr.right)

                if curr in child_parent_map and child_parent_map[curr] not in visited:
                    q.append(child_parent_map[curr])

            distance += 1