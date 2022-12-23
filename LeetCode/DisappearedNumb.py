# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
# range [1, n] that do not appear in nums.

# Solution
# The solution to this problem is pretty simple. It is mentioned that the list contains integers from 1 to the length of
# the list or n, i.e. if len of list was 4 the list would contain positive integers from [1,2,3,4]. As the list already
# contains them, we use a trick to mark the elements in their respective indexes with a negative value, and the indexes
# which have a positive value, indicate that the (index + 1) num (list indexes start from 0) is not present in the
# list, and they can be returned.

def findDisappearedNumbers(nums: list[int]) -> list[int]:
    for i in nums:
        idx = abs(i) - 1
        nums[idx] = -1* abs(nums[idx])
    result = []
    for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
    return result


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5,6]
print(findDisappearedNumbers([1,1]))  # [2]