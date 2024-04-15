from typing import List

# T: O(N)
# S: O(N)
# https://leetcode.com/problems/plus-one/

def plus_one(digits: List[int]) -> List[int]:
    # convert the array to string
    s = ""
    for digit in digits:
        s += str(digit)

    # add to 1 to the string
    result = int(s) + 1

    lst = []
    # convert it back to list
    for c in str(result):
        lst.append(int(c))

    return lst

print(plus_one(digits = [1,2,3])) # [1,2,4]
print(plus_one(digits = [4,3,2,1])) # [4,3,2,2]
print(plus_one(digits = [9])) # [1,0]