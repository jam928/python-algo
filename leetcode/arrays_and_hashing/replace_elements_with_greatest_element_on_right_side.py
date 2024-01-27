from typing import List


# Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

def replace_elements(arr: List[int]) -> List[int]:
    # If the length of the array is 1 then result will just be [-1]
    if len(arr) == 1:
        return [-1]

    # For the last two elements it will be -1 and the last element of the array respectively
    result = []
    result.append(-1)
    result.append(arr[len(arr) - 1])
    # Current max is now the last element of the array
    current_max = arr[len(arr) - 1]
    for i in range(len(arr) - 3, -1, -1):
        # update the current max if its less than the current element of the its neighbor
        current_max = max(current_max, arr[i + 1])
        result.append(current_max)

    result = result[::-1]
    return result


print(replace_elements([17, 18, 5, 4, 6, 1]))  # [18,6,6,6,1,-1]
print(replace_elements([400]))  # -1
