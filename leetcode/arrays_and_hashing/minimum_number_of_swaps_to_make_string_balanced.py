# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/

def min_swaps(s: str) -> int:
    opened = closed = 0
    swaps = 0

    for bracket in s:
        if bracket == '[':
            opened += 1
        else:
            closed += 1

        # if the number of closed brackets is greater than open increment swaps
        # decrement closed and increment open
        if closed > opened:
            swaps += 1
            closed -= 1
            opened += 1

    return swaps

if __name__ == '__main__':
    print(min_swaps("][][")) # 1
    print(min_swaps("]]][[[")) # 2
    print(min_swaps("[]")) # 0