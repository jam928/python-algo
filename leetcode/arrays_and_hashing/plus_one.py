from typing import List

# https://leetcode.com/problems/plus-one/description/

def plus_one(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1

        if digits[i] < 10:
            return digits

        digits[i] = 0

    arr = [0 for _ in range(len(digits) + 1)]
    arr[0] = 1

    return arr

print(plus_one([1,2,3])) # [1,2,4]
print(plus_one([4,3,2,1])) # [4,3,2,2]
print(plus_one([9])) # [1,0]