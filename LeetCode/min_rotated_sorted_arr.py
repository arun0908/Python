"""
Suppose an array of length n sorted in ascending order is rotated between 1
and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum
element of this array. You must write an algorithm that runs in O(log n) time.
"""


def find_min(nums: list[int]) -> int:
    """
    Find the minimum in the sorted rotated array using binary search
    """
    left, right = 0, len(nums) - 1
    result = nums[0]

    while left <= right:
        # Checking if the sub-array is already sorted by comparing the left
        # element with the right element of the sub-array and returning the
        # min of the left element and the result
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break

        mid = (left + right) // 2
        result = min(result, nums[mid])

        # Checking if the mid position is in the left part of the array by
        # comparing it with the leftmost element. If ever the mid lies in the
        # rightmost or leftmost array, that means it is sorted and we cannot
        # proceed further.
        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return result


print(find_min([3, 4, 5, 1, 2]))  # 1
print(find_min([4, 5, 6, 7, 0, 1, 2]))  # 0
