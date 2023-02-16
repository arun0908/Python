# Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element,
# or false otherwise. If the array is already strictly increasing, return true.
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).


def canBeIncreasing(nums: list[int]) -> bool:
    # count = 0
    # for i in range(0,len(nums)-1):
    #     if nums.count(nums[i]) != 1:
    #         return False
    #     elif nums[i] > nums[i+1]:
    #         count += 1
    # return count < 2
    for i in range(len(nums)):
        var = nums.pop(i)
        if nums == sorted(set(nums)):
            return True
        else:
            nums.insert(i, var)
    return False


print(canBeIncreasing([1, 2, 10, 5, 7]))  # True
print(canBeIncreasing([2, 3, 1, 2]))  # False
print(canBeIncreasing([1, 1, 1, 1]))  # False
