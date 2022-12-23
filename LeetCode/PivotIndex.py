#Given an array of integers nums, calculate the pivot index of this array.The pivot index is the index where the sum of
# all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This
# also applies to the right edge of the array. Return the leftmost pivot index. If no such index exists, return -1.

# Solution
# We can use a brute force approach here, and we can iterate through the entire array. As we iterate, we store the leftmost
# sum and the rightmost sum at every step and compare them. the rightmost sum can be expressed as the difference between
# the left sum and the total and the current value through the iteration.

def pivotIndex(nums: list[int]) -> int:
    leftSum = 0
    total = sum(nums)
    for i in range(len(nums)):
        rightSum = total-leftSum-nums[i]
        if leftSum == rightSum:
            return i
        else:
            leftSum += nums[i]
    return -1

print(pivotIndex([1,7,3,6,5,6]))  # 3
print(pivotIndex([1,2,3]))  # -1
print(pivotIndex([2,1,-1]))  # 0