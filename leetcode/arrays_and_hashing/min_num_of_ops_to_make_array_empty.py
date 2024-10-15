from collections import defaultdict
from typing import List

# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/


def min_operations(nums: List[int]) -> int:
    freq_map = defaultdict(int)

    for num in nums:
        freq_map[num] += 1

    count = 0

    for freq in freq_map.values():
        if freq == 1:
            return -1
        count += (freq // 3)
        if freq % 3 != 0:
            count += 1  # add any remaining freq / 3

    return count

if __name__ == '__main__':
    print(min_operations([1, 2, 3, 4, 5])) # -1
    print(min_operations([2,3,3,2,2,4,2,3,4])) # 4
    print(min_operations([2,1,2,2,3,3])) # -1