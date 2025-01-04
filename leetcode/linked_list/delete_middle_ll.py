from typing import Optional

from leetcode.linked_list.list_node import ListNode

# T: O(N)
# S: O(1)

# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    # find the middle node
    prev, mid = find_middle(head)

    if prev == mid:
        return None
    elif prev:
        prev.next = mid.next

    return head


def find_middle(node):
    slow = node
    fast = node
    prev = slow

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    return prev, slow