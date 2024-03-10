def maxAcutance(image):
    """
    :type image: List[String]
    :rtype: int
    """

    converted_img = [[int(num) for num in sublist] for sublist in image]

    row_sums = [sum(row) for row in converted_img]
    col_sums = [sum(x) for x in zip(*converted_img)]

    row_col_map = {}

    for i in range(len(row_sums)):
        number_of_zeroes = len(converted_img[0]) - row_sums[i]
        number_of_ones = row_sums[i]

        s = f"row of {i}"
        row_col_map[s] = (number_of_zeroes, number_of_ones)

    for j in range(len(col_sums)):
        number_of_zeroes = len(converted_img) - col_sums[j]
        number_of_ones = col_sums[j]

        s = f"col of {j}"
        row_col_map[s] = (number_of_zeroes, number_of_ones)

    max_acutance = float('-inf')

    for i in range(len(converted_img)):
        for j in range(len(converted_img[i])):
            row = f"row of {i}"
            col = f"col of {j}"
            acutance = row_col_map[row][1] + row_col_map[col][1] - (row_col_map[row][0] + row_col_map[col][0])
            max_acutance = max(acutance, max_acutance)

    return max_acutance