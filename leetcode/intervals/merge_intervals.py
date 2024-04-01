from typing import List

# T: O(nlogn)
# S: O(N)
# https://leetcode.com/problems/merge-intervals/
def merge(intervals: List[List[int]]) -> List[List[int]]:
    result = []

    intervals = sorted(intervals, key=lambda x: x[0])

    n = len(intervals)
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, n):
        # if the current element end is greater than the prev element
        # then add it to the list
        if intervals[i][0] > end:
            result.append([start, end])

            # reset the start and end to the current one
            start = intervals[i][0]
            end = intervals[i][1]
        else:
            end = max(end, intervals[i][1])

    # add the remaining start and end to the resulting list
    result.append([start, end])

    return result


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
print(merge([[1, 4], [4, 5]]))  # [[1,5]]
print(merge([[1, 4], [0, 0]]))  # [[0,4]]
print(merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))  # [[1,10]]
