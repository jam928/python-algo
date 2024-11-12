import random
from typing import Optional

from leetcode.linked_list.list_node import ListNode


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.node = head

    def getRandom(self) -> int:
        curr = self.node
        result = 0
        n = 1

        while curr:
            random_number = random.random()
            if random_number < (1.0 / n):
                result = curr.val
            n += 1
            curr = curr.next

        return result

if __name__ == '__main__':
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)

    sol = Solution(ll)
    print(sol.getRandom())
    print(sol.getRandom())
    print(sol.getRandom())
    print(sol.getRandom())
    print(sol.getRandom())