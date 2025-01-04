from typing import Optional, List

from leetcode.linked_list.list_node import ListNode

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

def nodes_between_critical_points(head: Optional[ListNode]) -> List[int]:
    prev = head
    curr = head.next
    critical_points = []
    pos = 1

    while curr.next:
        # check if its a local min or local max
        # if so add to critical points
        if (prev.val > curr.val and curr.val < curr.next.val) or (prev.val < curr.val and curr.val > curr.next.val):
            critical_points.append(pos)
        prev = curr
        curr = curr.next
        pos += 1

    # if there's less than 2 critical points in the array then we must return [-1,-1]
    if len(critical_points) < 2:
        return [-1, -1]

    min_dist = float('inf')
    max_dist = critical_points[-1] - critical_points[0]  # max will always be end - start of the critical points array

    for i in range(1, len(critical_points)):
        min_dist = min(min_dist, critical_points[i] - critical_points[i - 1])

    return [min_dist, max_dist]