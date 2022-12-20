# The next greater element of some element x in an array is the first greater element that is to the right of x in the
# same array.You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element
# of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1. Return an array answer
# of length nums1.length such that ans[i] is the next greater element as described above.

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    # O(m + n) solution where m is length of nums1 and n of nums2
    # for the most efficient solution we use stack. we consider the fact that if an element is present in nums1 we
    # append it to the stack. We check if the next element is greater than the top element in stack, if not we append it
    # The next element in nums2 if it is grater than the top element, then it is greater than previous elements in stack
    # ,and we append them to the result array based on the idx of those elements in nums1, and we pop elements from stack

    result = [-1] * len(nums1)
    idx_map = { val:idx for idx,val in enumerate(nums1) }
    stack = []
    for i in range(len(nums2)):
        while stack and nums2[i] > stack[-1]:
            idx = idx_map[stack[-1]]
            result[idx] = nums2[i]
            stack.pop()
        if nums2[i] in idx_map:
            stack.append(nums2[i])

    # Basic approach where we loop through nums2 and check every other element if it is greater than it, and we append
    # if we find it, based on the index of the element in nums1.

    # for i in range(len(nums2)):
    #     if nums2[i] not in idx_map:
    #         continue
    #     for j in range(i+1 , len(nums2)):
    #         if nums2[j] > nums2[i]:
    #             idx = idx_map[nums2[i]]
    #             result[idx] = nums2[j]
    #             break
    return result


print(nextGreaterElement([4,1,2],[1,3,4,2])) # [-1,3,-1]
print(nextGreaterElement([2,4], [1,2,3,4])) # [3,-1]
print(nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7])) # [7,7,7,7,7]