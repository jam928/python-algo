from typing import List


# https://leetcode.com/problems/kth-largest-element-in-an-array/description/


def find_kth_largest(nums: List[int], k: int) -> int:
    return sorted(nums)[-k]


print(find_kth_largest(nums=[3, 2, 1, 5, 6, 4], k=2))  # 5
print(find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))  # 4
