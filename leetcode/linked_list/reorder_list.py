# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode.linked_list.list_node import ListNode

# https://leetcode.com/problems/reorder-list/

class ReOrderList:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        result = head

        # find the middle node
        mid = self.__find_middle(head)

        # reverse from middle next node to null
        mid_reverse = self.__reverse(mid.next)

        # set the original mid next as null
        mid.next = None

        # merge two head ptr and mid reverse ptr
        self.__merge(head, mid_reverse)

        print(result)

    def __find_middle(self, node):
        slow = node
        fast = node

        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def __reverse(self, node):
        prev = None

        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        return prev

    def __merge(self, head, second_head):
        # swap the current head next with the second head
        # swap the second head next with the current head next
        # iterate both heads
        while head and second_head:
            head_next = head.next
            second_head_next = second_head.next

            head.next = second_head
            second_head.next = head_next

            head = head_next
            second_head = second_head_next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    reorder_list = ReOrderList().reorder_list(head)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)

    reorder_list2 = ReOrderList().reorder_list(head2)