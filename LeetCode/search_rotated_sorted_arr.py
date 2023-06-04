"""
There is an integer array nums sorted in ascending order (with distinct values)
Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k],
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
[4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return
the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
"""


def search(nums: list[int], target: int) -> int:
    """
    Find the given target element in the rotated sorted array.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the target is equal to the mid element.
        if nums[mid] == target:
            return mid

        # Checking the left sorted subarray
        if nums[left] <= nums[mid]:

            # If either the given target is greater than the middle element
            # in the left sorted array or the leftmost element in the left
            # sorted array is greater than the target element, we search to the
            # right of the middle position
            if nums[mid] < target or nums[left] > target:
                left = mid + 1
            # If either the target is less than the middle element and the
            # leftmost element of the left sorted array is less than the target
            # we search to the left of the middle element
            else:
                right = mid - 1
        # Checking the right sorted subarray
        else:

            # If the given target is less than the middle element
            # in the right sorted array or the rightmost element in the right
            # sorted array is less the target, then we search to the left of
            # the middle element
            if nums[mid] > target or nums[right] < target:
                right = mid - 1
            # If the given target is greater than the middle element
            # in the right sorted array or the rightmost element in the right
            # sorted array is greater the target, then we search to the right of
            # the middle element
            else:
                left = mid + 1
    return -1
