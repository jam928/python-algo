import heapq
from typing import List

# https://leetcode.com/problems/minimum-interval-to-include-each-query/

def min_interval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    pq = []
    cache = {}
    intervals.sort()
    for q in sorted(queries):

        i = 0
        # add the intervals that are smaller than or equal to the current q
        while i < len(intervals) and intervals[i][0] <= q:
            l = intervals[i][0]
            r = intervals[i][1]
            heapq.heappush(pq, (r - l + 1, intervals[i][1]))
            i += 1

        # remove the intervals in the queue that its end time is less than q
        while pq and pq[0][1] < q:
            heapq.heappop(pq)

        cache[q] = pq[0][0] if pq else -1

    result = [cache[q] for q in queries]

    return result

if __name__ == '__main__':
    print(min_interval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5])) # [3,3,1,4]
    print(min_interval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22])) # [2,-1,4,6]