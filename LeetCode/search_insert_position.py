# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums: list[int], target: int) -> int:
    # Brute force approach
    # if target < nums[0]:
    #     return 0
    # elif target > nums[len(nums) - 1]:
    #     return len(nums)
    # elif target in nums:
    #     return nums.index(target)
    # else:
    #     for i in range(len(nums) - 1):
    #         if nums[i] < target < nums[i + 1]:
    #             return i + 1

    # Binary search with time complexity O(log n) approach
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


print(searchInsert([1, 3, 5, 6], 5))  # 2
print(searchInsert([1, 3, 5, 6], 2))  # 1
print(searchInsert([1, 3, 5, 6], 7))  # 4
print(searchInsert([1], 0))  # 0
