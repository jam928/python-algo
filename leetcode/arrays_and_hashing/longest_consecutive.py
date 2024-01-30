# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Keep track of the longest consecutive sequence
# Add elements to set
# On each iteration in the list
# Try to expand left and right according if the elements exists in set
# Update current longest with the longest var
def longest_consecutive_sequence(nums):
    longest = 1

    nums_set = set(nums)

    for num in nums:
        current_longest = 1

        right_extend = num + 1
        while right_extend in nums_set:
            current_longest += 1
            nums_set.remove(right_extend)
            right_extend += 1

        left_extend = num - 1
        while left_extend in nums_set:
            current_longest += 1
            nums_set.remove(left_extend)
            left_extend -= 1

        longest = max(current_longest, longest)

    return longest
