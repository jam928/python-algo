from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> List[int]:
    # Add elements to set while iterating thru target
    nums_dict = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement], index]
        nums_dict.update({num: index})

    return []
