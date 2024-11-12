from typing import List

# https://leetcode.com/problems/find-all-duplicates-in-an-array/


def find_duplicates(nums: List[int]) -> List[int]:
    result = []

    for num in nums:
        num = abs(num)

        if nums[num - 1] < 0:
            result.append(num)

        nums[num - 1] = -nums[num - 1]

    return result

if __name__ == '__main__':
    print(find_duplicates([4,3,2,7,8,2,3,1])) #  [2,3]
    print(find_duplicates([1,1,2])) #  [1]
    print(find_duplicates([1])) # []