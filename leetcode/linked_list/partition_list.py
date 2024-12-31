from typing import Optional

from leetcode.linked_list.list_node import ListNode

# https://leetcode.com/problems/partition-list/
# T: O(N)
# S: O(N)

def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    # split lists into 2
    # left ll has values left than X
    # right ll has values greater than or equal to X

    left_ll = []
    right_ll = []

    curr = head
    while curr:
        if curr.val < x:
            left_ll.append(curr.val)
        else:
            right_ll.append(curr.val)
        curr = curr.next

    # merge left and right LL
    left_ll.extend(right_ll)
    dummy = ListNode()
    result = dummy

    for num in left_ll:
        dummy.next = ListNode(num)
        dummy = dummy.next

    return result.next