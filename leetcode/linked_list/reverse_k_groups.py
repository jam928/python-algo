from typing import Optional

from leetcode.linked_list.list_node import ListNode


# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    curr = head
    count = 0
    while curr and count != k:
        curr = curr.next
        count += 1

    if count == k:
        curr = reverse_k_group(curr, k)
        while count > 0:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
            count -= 1
        head = curr
    return head


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

print(f'Original list: {head1}')
print(reverse_k_group(head1, 2))

# head2 = ListNode(1)
# head2.next = ListNode(2)
# head2.next.next = ListNode(3)
# head2.next.next.next = ListNode(4)
# head2.next.next.next.next = ListNode(5)
#
# print(reverse_k_group(head1, 3))
