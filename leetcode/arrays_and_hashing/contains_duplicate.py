# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

#Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
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
