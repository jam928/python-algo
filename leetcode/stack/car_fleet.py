from typing import List


# Time Complexity: O(n log n)
# Space Complexity: O(n)

# https://leetcode.com/problems/car-fleet/description/

def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    # zip the position and speed to a pair tuple
    pairs = zip(position, speed)

    # utilize stack to remove the cars once they reach the same speed
    stack = []

    # sort the pairs in reverse order
    sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)

    for pair in sorted_pairs:
        # calcuate the time of the current car that will get to the target
        time = (target - pair[0]) / (pair[1] * 1.0)
        previous_time = float('inf') if len(stack) == 0 else stack[-1]
        stack.append(time)

        if len(stack) >= 2 and stack[-1] <= previous_time:
            stack.pop()

    return len(stack)


print(car_fleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))  # 3
print(car_fleet(target=10, position=[3], speed=[3]))  # 1
print(car_fleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))  # 1
