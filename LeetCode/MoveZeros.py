# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# We solve this by a modification of quick sort, where we sort an array in place and without modifying it. We consider the left and right indexes
# at same position and instead of moving 0's to the right, we move the non 0 values to the left. 

# This is similar to the lumoto partition technique of quick sort
def moveZeroes(nums: list[int]) -> None:
    # consider the left and right indexes as 0. 
    l = 0
    # loop through the array.
    for r in range(len(nums)):
        # if any element is not 0, we increment our l and r index and proceed. If we find 0, we increment only the r index and once we find a
        # non zero element we swap left and right and keep repeating it.
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([-1,-2,-3,0,0,1,2,3]))