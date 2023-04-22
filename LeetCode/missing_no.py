# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
# missing from the array.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

def missingNumber(nums: list[int]) -> int:
    n = int((len(nums)*(len(nums)+1))/2)
    return n-sum(nums)


print(missingNumber([3, 0, 1]))  # 2
print(missingNumber([0, 1]))  # 2
