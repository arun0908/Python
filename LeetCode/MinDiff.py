# Minimum Difference Between Highest and Lowest of K scores:
# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.

def minimumDifference(nums: list[int], k: int) -> int:
        # Sort the input so that, the difference between the max and min of k elements from array is calculated
        nums.sort()
        # Consider a sliding window, with inital position at 0 and the rightmost position at k elements.
        l , r = 0 , k-1
        # res is set to float("inf") for considering minimum value
        res = float("inf")
        while r < len(nums):
            # compare min of result and the max and min element between the range of k elements
            res = min(res, nums[r]-nums[l])
            l , r = l+1, r+1
        return res


print(minimumDifference([9,4,1,7], 2))  # 2
print(minimumDifference([90]))  # 0
