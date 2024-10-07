from leetcode.linked_list.Node import Node
from typing import Optional


# https://leetcode.com/problems/copy-list-with-random-pointer/description/

def copy_random_list(head: 'Optional[Node]') -> 'Optional[Node]':
    cache = {}

    # store the old nodes along with the new node val
    curr = head
    while curr:
        cache[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        # map the node next and random from the map
        node = cache.get(curr)
        node.next = cache.get(curr.next)
        node.random = cache.get(curr.random)

        curr = curr.next

    return cache.get(head)
