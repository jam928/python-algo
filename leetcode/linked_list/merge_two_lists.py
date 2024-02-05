from typing import Optional

from leetcode.linked_list.list_node import ListNode

# https://leetcode.com/problems/merge-two-sorted-lists/

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    result_head = result

    # iterate both linked lists
    # if the list 1 val is less than list2 val add it to result
    # o.w other way around
    while (list1 is not None) or (list2 is not None):
        list1_val = list1.val if list1 is not None else 101  # add the max + 1 if its null to add the other element instead
        list2_val = list2.val if list2 is not None else 101
        if list1_val < list2_val:
            result.next = ListNode(list1_val)
            result = result.next
            list1 = list1.next
        else:
            result.next = ListNode(list2_val)
            result = result.next
            list2 = list2.next

    return result_head.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
print(merge_two_lists(head, head2))
