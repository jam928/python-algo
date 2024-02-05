from typing import Optional

from leetcode.linked_list.list_node import ListNode


# https://leetcode.com/problems/reverse-linked-list/description/

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    while head is not None:
        # swap pointers with the prev and head
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(reverse_list(head))

head = None
head = ListNode(1)
head.next = ListNode(2)
print(reverse_list(head))
