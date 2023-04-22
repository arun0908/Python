# Given an integer array nums and an integer k, return true if there are
# two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


def containsNearbyDuplicate(nums: list[int], k: int):
    # =================================================
    # for i in range(len(nums)):
    #    for j in range(i+1, len(nums)):
    #        if nums[i] == nums[j]:
    #            if (abs(i-j)) <= k:
    #                return True
    # =================================================
    # map = defaultdict(list)
    # for i in range(len(nums)):
    #    map[nums[i]].append(i)
    # for c in map.values():
    #    for i in range(len(c)-1):
    #        if abs(c[i] - c[i+1]) <= k:
    #            return True
    # ==================================================
    map = {}
    for i, num in enumerate(nums):
        if num not in map:
            map[num] = i
        else:
            if abs(i-map[num]) <= k:
                return True
            else:
                map[num] = i


print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # false
print(containsNearbyDuplicate([1, 2, 3, 1], 3))  # true
print(containsNearbyDuplicate([1, 0, 1, 1], 1))  # true
