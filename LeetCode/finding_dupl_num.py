"""
Given an array of integers nums containing n + 1 integers where each integer
is in the range [1, n] inclusive. There is only one repeated number in nums,
return this repeated number. You must solve the problem without modifying the
array nums and uses only constant extra space.
"""


def find_duplicate(nums: list[int]) -> int:
    """
    Find the duplicate value in the given list
    """
    # First Approach

    # slow, fast = 0, 1
    # for i in range(0, len(nums)):
    #     if nums[slow] == nums[fast]:
    #         return nums[slow]
    #     slow += 1
    #     fast += 2
    #     if fast > len(nums)-1:
    #         fast = fast - len(nums)

    # Final Approach using Floyd's cycle finding algorithm
    tortoise, hare = 0, 0

    # Finding the point of intersection of the tortoise and the hare
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Initializing another tortoise and finding the start of cycle or
    # duplicate value
    tortoise2 = 0
    while True:
        tortoise = nums[tortoise]
        tortoise2 = nums[tortoise2]
        if tortoise == tortoise2:
            return tortoise


print(find_duplicate([1, 3, 4, 2, 2]))  # 2
print(find_duplicate([3, 1, 3, 4, 2]))  # 3
