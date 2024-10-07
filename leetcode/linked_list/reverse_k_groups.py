from typing import Optional

from leetcode.linked_list.list_node import ListNode


# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        # get kth node
        kth_node = get_kth_node(group_prev, k)

        # break out of loop if kth is null hence done reversing
        if not kth_node:
            break

        # reverse group
        prev = kth_node.next
        curr = group_prev.next
        group_next = kth_node.next
        reverse(prev, curr, group_next)

        # update pointers
        temp = group_prev.next
        group_prev.next = kth_node
        group_prev = temp  # update the group prev for the next iteration

    return dummy.next

def get_kth_node( node, k):
    curr = node
    while curr and k > 0:
        k -= 1
        curr = curr.next

    return curr

def reverse(prev, curr, group_next):
    while curr != group_next:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

print(f'Original list: {head1}')
print(reverse_k_group(head=head1, k=2))

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)

print(reverse_k_group(head=head2, k=3))
