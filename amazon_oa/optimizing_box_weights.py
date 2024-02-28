from collections import deque


def minimal_heaviest_set_A(weights):
    # sort the array to easily add the largest weights into subset A
    weights.sort()

    # Add all weights to B and starting adding the heavyist to A till A weights are greater than B
    b_weights = list(weights)
    a_weights = deque()

    b_total_weights = sum(b_weights)
    a_total_weights = 0

    for i in range(len(weights) - 1, -1, -1):
        # append weight at i to A and subtract from B
        b_weights.remove(weights[i])
        a_weights.appendleft(weights[i])

        b_total_weights -= weights[i]
        a_total_weights += weights[i]

        # if the total weights of A greater than B return list of A weights
        if a_total_weights > b_total_weights:
            return list(a_weights)

    return list(weights)


print(minimal_heaviest_set_A([]))  # []
print(minimal_heaviest_set_A([0]))  # [0]
print(minimal_heaviest_set_A([1]))  # [1]
print(minimal_heaviest_set_A([1, 0]))  # [1]
print(minimal_heaviest_set_A([0, 0, 1, 0, 0, -1]))  # [1]
print(minimal_heaviest_set_A([-1, -2, -3]))  # [-1]
print(minimal_heaviest_set_A([3, 2, 6, 5, 7]))  # [6,7]
print(minimal_heaviest_set_A([5, 10, 6, 6, 2]))  # [6,10]
print(minimal_heaviest_set_A([2, 3, 2]))  # [2,3]
print(minimal_heaviest_set_A([2, 3, 2, 3]))  # [3,3]
print(minimal_heaviest_set_A([18, -3, -2, 19, 2, 0, 15, -9]))  # [18,19]
