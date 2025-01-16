from typing import Optional

from leetcode.linked_list.list_node import ListNode

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/reverse-linked-list-ii/

def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == right:
        return head

    curr = head
    stack = []

    prev = curr
    left_pos = 0

    # traverse the list
    while curr:
        left_pos += 1

        if left_pos == right:
            stack.append(curr.val)
            # popout the elements out of the stack and start from the prev node
            while stack:
                prev.val = stack.pop()
                prev = prev.next
            break
        elif left_pos == left:
            prev = curr
            stack.append(curr.val)
        elif len(stack) != 0:
            stack.append(curr.val)

        curr = curr.next

    return head