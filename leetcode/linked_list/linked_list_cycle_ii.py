from typing import Optional

from leetcode.linked_list.list_node import ListNode


# https://leetcode.com/problems/linked-list-cycle-ii/
# T: O(N)
# S: O(1)
def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    # use the torq and hare algo

    slow = fast = head
    has_cycle = False
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # reset the slow pointer and iterate till we reach the fast ptr
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next

if detect_cycle(head1):
    print(f'Tail connects to node index: {head1.next.val}')
else:
    print('No cycle')

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2

if detect_cycle(head2):
    print(f'Tail connects to node index: {head2.next.val}')
else:
    print('No cycle')

head3 = ListNode(1)

if detect_cycle(head3):
    print(f'Tail connects to node index: {head3.next.val}')
else:
    print('No cycle')