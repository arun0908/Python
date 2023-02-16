# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.


def sumOfUnique(nums: list[int]):
    sum = 0
    for i in nums:
        if nums.count(i) == 1:
            sum += i
    return sum
    # map = {}
    # sum = 0
    #     map[i] = 1 + map.get(i,0)
    # for j in map:
    #     if map[j] == 1:
    #         sum += j
    # return sum


print(sumOfUnique([1, 2, 3, 2]))  # 4
print(sumOfUnique([1, 1, 1, 1]))  # 0
