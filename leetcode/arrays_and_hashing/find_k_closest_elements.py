from typing import List

# https://leetcode.com/problems/find-k-closest-elements/

def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    index = binary_search(arr, x)

    l = r = index
    for i in range(k - 1):
        if l == 0:
            r += 1
        elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
            l -= 1
        else:
            r += 1

    return arr[l:r + 1]


# find index of x or the closest val to x
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    closest = nums[0]
    closest_idx = 0
    while left <= right:
        mid = (left + right) // 2

        # Update the closest number with tie-breaking for smaller numbers
        if (abs(nums[mid] - target) < abs(closest - target) or (
                abs(nums[mid] - target) == abs(closest - target) and nums[mid] < closest)):
            closest = nums[mid]
            closest_idx = mid

        if nums[mid] == target:
            return mid  # Exact match found
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return closest_idx

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    print(find_closest_elements(arr, k, x)) # [1,2,3,4]

    arr = [1, 1, 2, 3, 4, 5]
    k = 4
    x = -1
    print(find_closest_elements(arr, k, x)) # [1,1,2,3]