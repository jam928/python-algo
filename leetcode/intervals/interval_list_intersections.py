from typing import List


# https://leetcode.com/problems/interval-list-intersections/description/
# T: O(M+N)
# S: O(1)

def interval_intersection(first_list: List[List[int]], second_list: List[List[int]]) -> List[List[int]]:
    i = 0
    j = 0
    m = len(first_list)
    n = len(second_list)

    result = []

    while i < m and j < n:
        x1 = first_list[i][0]
        y1 = first_list[i][1]

        x2 = second_list[j][0]
        y2 = second_list[j][1]

        # verify if both pairs overlap
        if ((x1 <= x2 and x2 <= y1) or (x2 <= x1 and x1 <= y2)):
            # add the overlapping pairs
            result.append([max(x1, x2), min(y1, y2)])

        if y1 < y2:
            i += 1
        else:
            j += 1

    return result


print(interval_intersection(first_list=[[0, 2], [5, 10], [13, 23], [24, 25]], second_list=[[1, 5], [8, 12], [15, 24],
                                                                                           [25,
                                                                                            26]]))  # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

print(interval_intersection(first_list=[[1, 3], [5, 9]], second_list=[]))  # []
