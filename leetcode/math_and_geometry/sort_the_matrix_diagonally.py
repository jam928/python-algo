from typing import List


# T: O(m * n log(min(m,n)))
# S: O(min(m,n))
# https://leetcode.com/problems/sort-the-matrix-diagonally/description/

def diagonal_sort(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])

    # no need to sort if only one column or one row based
    if m == 1 or n == 1:
        return mat

    # sort each column
    for j in range(n):
        sort(mat, 0, j, m, n)

    # sort each row
    for i in range(m):
        sort(mat, i, 0, m, n)

    return mat


def sort(mat, i, j, m, n):
    values = []

    # loop through diagonal
    while i < m and j < n:
        values.append(mat[i][j])

        i += 1
        j += 1

    values.sort()

    # subtract i & j because out of range
    i -= 1
    j -= 1

    # fill diagonal in reversed order
    while values:
        mat[i][j] = values.pop()
        i -= 1
        j -= 1


if __name__ == '__main__':
    print(diagonal_sort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))  # [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    print(diagonal_sort(
        mat=[[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4],
             [84, 28, 14, 11, 5,
              50]]))  # [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
