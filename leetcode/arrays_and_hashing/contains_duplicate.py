# https://leetcode.com/problems/contains-duplicate/
def contains_duplicate(nums) -> bool:
    nums_set = set()

    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)

    return False

print(contains_duplicate([1,2,3,1])) # True
print(contains_duplicate([1,2,3,4])) # False
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True
