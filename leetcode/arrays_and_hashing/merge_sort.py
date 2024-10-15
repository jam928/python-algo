from typing import List

# https://leetcode.com/problems/sort-an-array/description/

class MergeSort:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    # Merge sort function (recursively divides the list and merges)
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        # Find the middle of the list
        mid = len(arr) // 2

        # Recursively split the list into two halves
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])

        # Merge the sorted halves
        return self.merge(left_half, right_half)

    # Merge function to combine two halves
    def merge(self, left, right):
        merged = []
        left_index = right_index = 0

        # Compare each element of the two halves and merge them in sorted order
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # If there are any remaining elements in the left or right half, append them
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

if __name__ == '__main__':
    mergesort = MergeSort()
    print(mergesort.sortArray([5,2,3,1]))
