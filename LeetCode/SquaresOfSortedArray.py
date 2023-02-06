# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

# The trick here would be to consider two pointers at the ends and check which is greater and append it and return the reverse of resultant array
def sortedSquares(nums: list[int]) -> list[int]:
    result = []
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l]*nums[l] > nums[r] * nums[r]:
            result.append(nums[l]*nums[l])
            l += 1
        else:
            result.append(nums[r]*nums[r])
            r -= 1
    return result[::-1]


print(sortedSquares([-4, -1, 0, 3, 10]))  # [0,1,9,16,100]
print(sortedSquares([-7, -3, 2, 3, 11]))  # [4,9,9,49,121]
