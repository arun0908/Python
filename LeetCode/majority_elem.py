# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.

def majorityElement(nums: list[int]) -> int:
    # value_map = {}
    # result, maxCount = 0,0
    # for i in nums:
    #     value_map[i] = 1 + value_map.get(i,0)
    #     result = i if value_map[i] > maxCount else result
    #     maxCount = max(value_map[i], maxCount)
    # return result

    # Optimized solution utilizing O(1) space. The algorithm or idea behind this is Boyer-Moore algorithm
    result, count = 0, 0
    for i in nums:
        if count == 0:
            result = i
        count += (1 if i == result else -1)
    return result


print(majorityElement([3, 2, 3]))  # 3
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
