from typing import List

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/insert-interval/
def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    i = 0

    # add all the intervals ending before newInterval start
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # merge all overlapping intervals to be consider as newinterval
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    # add the union of intervals we got from the previous run
    result.append(new_interval)

    # add the remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result


print(insert(intervals=[[1, 3], [6, 9]], new_interval=[2, 5])) # [[1,5],[6,9]]
print(insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval=[4, 8])) # [[1,2],[3,10],[12,16]]
