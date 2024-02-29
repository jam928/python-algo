# O: (n+m)
# S: (max(n,m))
def storage_optimization(n, m, h, v):
    return get_max(n + 1, h) * get_max(m + 1, v)


def get_max(length, bars):
    seperators = set([])

    # add the seperators in to grid
    for i in range(1, length):
        seperators.add(i)

    # remove the seperators in grid
    for i in bars:
        seperators.remove(i)

    # if the number seperators is less than 1 then the max would just the whole length of the grid
    if len(seperators) < 1:
        return length

    seperators = list(seperators)
    max_length = seperators[0]
    for i in range(1, len(seperators)):
        max_length = max(max_length, seperators[i] - seperators[i - 1])

    # calc max_length for the last one
    max_length = max(max_length, length - seperators[-1])

    return max_length


print(storage_optimization(6, 6, [4], [2]))  # 4

print("Run0: opening(1,4 x 2,4), expected: 6, result:", storage_optimization(5, 5, [2, 3], [3]))
print("Run1: opening(3,10 x 0,7), expected: 49, result:",
      storage_optimization(10, 10, [4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 8, 9, 10]))
print("Run2: opening(6,8 x 0,11), expected: 22, result:",
      storage_optimization(10, 10, [7], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Run3: opening(0,1 x 0,1), expected: 1, result:", storage_optimization(10, 10, [], []))
print("Run4: opening(0,11 x 0,11), expected: 121, result:",
      storage_optimization(10, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
