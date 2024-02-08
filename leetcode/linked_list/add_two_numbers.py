from typing import Optional

from leetcode.linked_list.list_node import ListNode

# https://leetcode.com/problems/add-two-numbers/

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    new_ll = ListNode(-1)
    result = new_ll

    carry = 0
    while l1 or l2 or carry > 0:
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0

        # add the two nodes plus the carry
        sum_of_nodes = num1 + num2 + carry

        # the next carry is sum of the nodes divide by 10
        carry = sum_of_nodes // 10

        # the value of the new node will be sum of nodes module 10
        new_ll.next = ListNode(sum_of_nodes % 10)
        new_ll = new_ll.next

        # iterate to next element in list for both LL
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(add_two_numbers(l1, l2))

l1 = ListNode(0)

l2 = ListNode(0)

print(add_two_numbers(l1, l2))
