from typing import List

# T: O(nlogn)
# S: O(1)
# https://leetcode.com/problems/non-overlapping-intervals/


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    # sort intervals by last index
    intervals = sorted(intervals, key=lambda x: x[1])

    end = intervals[0][1]

    over_lapping_count = 0

    for i in range(1, len(intervals)):
        # if the current interval start is less than end then we must delete this interval
        # thus increasing the overlapping count
        if intervals[i][0] < end:
            over_lapping_count += 1
        else:
            # update the end to the current one for the next check
            end = intervals[i][1]

    return over_lapping_count


print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))  # 2
print(erase_overlap_intervals([[1, 2], [2, 3]]))  # 0
print(erase_overlap_intervals([[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]))  # 4
