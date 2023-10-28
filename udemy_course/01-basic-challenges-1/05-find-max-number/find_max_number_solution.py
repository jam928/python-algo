def find_max_number(arr):
    return max(*arr)


def find_max_number_2(arr):
    def find_max(arr):
        max = float('-inf')

        for e in arr:
            if e > max:
                max = e

        return max
