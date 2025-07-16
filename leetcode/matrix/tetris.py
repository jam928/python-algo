def updateGrid(result, figure, count):
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] != 0:
                continue
            if figure == 'A':
                result[i][j] = count
                return
            elif figure == 'B' and j + 2 < len(result[i]) and result[i][j + 1] == 0 and result[i][j + 2] == 0:
                result[i][j] = count
                result[i][j + 1] = count
                result[i][j + 2] = count
                return
            elif figure == 'C' and i + 1 < len(result) and j + 1 < len(result[i]) and result[i][j + 1] == 0 and result[i+1][j] == 0 and result[i+1][j + 1] == 0:
                result[i][j] = count
                result[i][j+1] = count
                result[i+1][j] = count
                result[i+1][j + 1] = count
                return
            elif figure == 'D' and i + 2 < len(result) and j + 1 < len(result[i]) and result[i+1][j] == 0 and result[i+2][j] == 0 and result[i+1][j + 1] == 0:
                result[i][j] = count
                result[i+1][j] = count
                result[i+1][j+1] = count
                result[i+2][j] = count
                return
            elif figure == 'E' and i + 1 < len(result) and j - 1 >= 0 and j + 1 < len(result[i]) and result[i][j-1] == 0 and result[i+1][j] == 0 and result[i+1][j + 1] == 0:
                result[i][j] = count
                result[i+1][j-1] = count
                result[i+1][j] = count
                result[i+1][j+1] = count
                return


def tetris(n,m,figures):
    result = [[0 for _ in range(n)] for _ in range(m)]

    count = 1
    for figure in figures:
        updateGrid(result, figure, count)
        count += 1

    return result

def pretty_print_matrix(matrix):
    if not matrix:
        print("Empty matrix")
        return

    # Determine maximum width for each column
    num_cols = len(matrix[0])
    col_widths = [0] * num_cols
    for row in matrix:
        for i, item in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(item)))

    # Print the matrix with aligned columns
    for row in matrix:
        formatted_row = []
        for i, item in enumerate(row):
            formatted_row.append(str(item).rjust(col_widths[i]))
        print(" ".join(formatted_row))

if __name__ == '__main__':
    figures = ['D', 'B', 'A', 'C']
    result = tetris(4, 4, figures)
    pretty_print_matrix(result)