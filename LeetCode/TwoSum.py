# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order. Ex: Input: nums = [2,7,11,15], target = 9 Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def twoSum(nums: list[int], target: int) -> list[int]:
    # Brute force method. This solution loops twice over input array giving us a time complexity of O(n^2)
    # result = []
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if (nums[i] + nums[j]) == target:
    #             result.append(i)
    #             result.append(j)
    #             return result

    # This is a one pass method, meaning looping once over the input array but using a dict/hash map to give O(n) time
    result = {}  # store value : index pairs
    for i, n in enumerate(nums):  # enumerate function gives an object cont. pairs of counter and the value in the array
        temp = target - n
        if temp in result:
            return [result[temp], i]
        result[n] = i

    # If a sorted array is given another approach is using two pointers to traverse through the list, giving O(n) time
    # l, r = 0, len(nums)-1
    # while l < r:
    #     if nums[l] + nums[r] > target:
    #         r -= 1
    #     if nums[l] + nums[r] < target:
    #         l -= 1
    #     else:
    #         return[l, r]


