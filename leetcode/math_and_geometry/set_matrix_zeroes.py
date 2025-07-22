from typing import List


# T: O(NM)
# S: O(1)
# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        is_first_row_zero = False

        # set the first row and first column as the zero placeholder
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    continue
                # set the column at j from the first row as zero
                matrix[0][j] = 0

                if i > 0:
                    matrix[i][0] = 0  # set the row at i first column as zero
                else:
                    is_first_row_zero = True

        # now iterate from the second row and second column and check if the first row or column is zero
        for i in range(1, m):
            for j in range(1, n):
                # if the element at first column is zero or first element in the row is zero
                # set the current element 0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # set the first col all zeros if the first element is zero
        if matrix[0][0] == 0:
            for i in range(0, m):
                matrix[i][0] = 0

        # set the first row all zeros if the is_first_row_zero is true
        if is_first_row_zero:
            for i in range(0, n):
                matrix[0][i] = 0


if __name__ == '__main__':
    s = Solution()
    arr = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeros(arr)

    assert arr == [[1,0,1],[0,0,0],[1,0,1]]
    arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeros(arr)
    assert arr == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
