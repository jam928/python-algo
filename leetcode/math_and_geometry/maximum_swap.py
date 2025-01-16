
# https://leetcode.com/problems/maximum-swap/description/
# T: O(N)
# S: O(N)
def maximum_swap(num: int) -> int:
    nums = list(str(num))
    n = len(nums) - 1

    max_idx = n
    left_idx = right_idx = -1

    # traverse from right to left and track the largest digit so far
    # if a smaller digit is found before a larger one, store their positions
    for i in range(n - 1, -1, -1):
        if nums[i] > nums[max_idx]:
            max_idx = i
        elif nums[i] < nums[max_idx]:
            left_idx = i
            right_idx = max_idx

    if left_idx == -1:
        return num

    # swap numbers
    temp = nums[left_idx]
    nums[left_idx] = nums[right_idx]
    nums[right_idx] = temp

    return int(''.join(nums))

if __name__ == '__main__':
    print(maximum_swap(2736)) # 7236
    # print(maximum_swap(9973)) # 9973 (No swap)