from typing import Optional

from leetcode.linked_list.list_node import ListNode

# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:

    # store nodes list
    nodes_list = []

    curr = head
    while curr:
        nodes_list.append(curr.val)
        curr = curr.next

    # split the lists by k
    split_lists = [nodes_list[i:i + k] for i in range(0, len(nodes_list), k)]

    # iterate from right to left for each of the lists
    # except for the lists that are not of size k
    # add to new ll and return it
    result = ListNode(-1)

    curr = result

    for lst in split_lists:

        if len(lst) != k:
            for element in lst:
                curr.next = ListNode(element)
                curr = curr.next
        else:
            for j in range(len(lst) - 1, -1, -1):
                curr.next = ListNode(lst[j])
                curr = curr.next

    return result.next

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

print(reverse_k_group(head1, 2))

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)

print(reverse_k_group(head1, 3))
