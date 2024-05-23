import collections
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    output = []
    l = r = 0
    q = collections.deque()  # contain indices

    while r < len(nums):

        # pop smaller values that are less than the current number
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        q.append(r)

        # remove left val from window if left index is out of bounds from the window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output


print(max_sliding_window(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))  # [3,3,5,5,6,7]
print(max_sliding_window(nums=[1], k=1))  # [1]
