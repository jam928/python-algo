from typing import Optional

from leetcode.linked_list.list_node import ListNode


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class RemoveNthNodeFromEndOfList:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        length_of_list = self.length_of_list(head)

        result = head

        position_to_remove = length_of_list - n
        if position_to_remove == 0:
            result = result.next
            return result

        # remove the length of list - n using prev and curr pointers
        prev, curr = head, head
        result = prev

        for i in range(0, position_to_remove):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return result

    def length_of_list(self, head):
        node = head

        count = 0
        while node is not None:
            count += 1
            node = node.next

        return count


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    result = RemoveNthNodeFromEndOfList().remove_nth_from_end(head, 2)
    print(result)

    head2 = ListNode(1)
    result2 = RemoveNthNodeFromEndOfList().remove_nth_from_end(head2, 1)
    print(result2)

    head3 = ListNode(1)
    head3.next = ListNode(2)
    result3 = RemoveNthNodeFromEndOfList().remove_nth_from_end(head3, 1)
    print(result3)
