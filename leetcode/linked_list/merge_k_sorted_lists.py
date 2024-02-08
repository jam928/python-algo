import heapq
from typing import List, Optional

from leetcode.linked_list.list_node import ListNode


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    result = ListNode(-1)

    pq = []

    # store nodes in heapq
    for lst in lists:
        while lst:
            heapq.heappush(pq, lst.val)
            lst = lst.next
    curr = result

    # remove nodes in pq and store new list
    while pq:
        val = heapq.heappop(pq)
        curr.next = ListNode(val)
        curr = curr.next

    return result.next

list_node1 = ListNode(1)
list_node1.next = ListNode(4)
list_node1.next.next = ListNode(5)

list_node2 = ListNode(1)
list_node2.next = ListNode(3)
list_node2.next.next = ListNode(4)

list_node3 = ListNode(2)
list_node3.next = ListNode(6)

lists_nodes = [list_node1, list_node2, list_node3]

print(merge_k_lists(lists_nodes)) # [1, 1, 2, 3, 4, 4, 5, 6]
