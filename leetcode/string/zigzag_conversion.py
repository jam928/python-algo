class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [[] for _ in range(numRows)]

        currentRow = 0
        goingDown = False

        for c in s:
            rows[currentRow].append(c)

            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown

            currentRow += 1 if goingDown else - 1

        result = []

        for row in rows:
            result.extend(row)

        return ''.join(result)

if __name__ == '__main__':

    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows)) # PAHNAPLSIIGYIR

    s = "PAYPALISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))  # PINALSIGYAHRPI

    s = "A"
    numRows = 1
    print(Solution().convert(s, numRows)) # A