# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Solution: The solution for this would be to consider a prefix, which would be the product of all the elements before
#           the current element and store it in a resultant array. Then we can compute the suffix of an element as the
#           product of the elements after it and then multiply it with the prefix of the current value. the value of
#           prefix is already present in the element, so it is multiplied with postfix.

def productExceptSelf(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    prefix = 1
    for i in range(1,len(nums)):
       result[i] = prefix
       prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix
        postfix *= nums[i]
    return result



print(productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]