from typing import List

# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

def divide_array(nums: List[int], k: int) -> List[List[int]]:
    nums.sort()
    result = []
    n = len(nums) // 3

    for i in range(n):
        # [x,y,z] if z - x > k return []
        if nums[i * 3 + 2] - nums[i * 3] > k:
            return []
        result.append(nums[i * 3:i * 3 + 3])
    return result

if __name__ == '__main__':
    print(divide_array(nums = [1,3,4,8,7,9,3,5,1], k = 2)) # [[1,1,3],[3,4,5],[7,8,9]]
    print(divide_array(nums = [2,4,2,2,5,2], k = 2)) # []