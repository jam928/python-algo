from typing import Optional

from leetcode.linked_list.list_node import ListNode

# https://leetcode.com/problems/linked-list-cycle/description/

def has_cycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    # use slow and fast pointers; at some point the slow and fast pointer will meet
    slow, fast = head, head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next

print(has_cycle(head1))

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2

print(has_cycle(head2))

head3 = ListNode(1)

print(has_cycle(head3))
