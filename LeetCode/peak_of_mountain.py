# Given an array of n integers. Find the peak of the array. The peak element of the array is defined as the element which is greater than
# arr[i-1] and is greater than arr[i+1] where arr[i] is the element. It is guaranteed that there is only one peak element.

# The input array structure is such that, it keeps increasing from the start till a point and then decreases again. The topmost position is our peak
# Both the lines are monotonous in direction (either increasing or decreasing), so binary search can be used. We have two conditions here.
# In case the mid lands on the first increasing line, then we need to move our left pointer ahead. Else, we have two conditions, either the mid
# is our element or the mid lies on the second decreasing line. If we move our right pointer to mid - 1 then we might end up pushing our
# mid element onto the first increasing line in some cases where mid might be pivot. So we set r to mid.

def findPeak(arr, n):
    l, r = 0, n-1
    # We consider l < r and not equal to, because this causes an index out of bound error for mid+1. Instead we can just return left pointer
    # because, if l goes till right pointer or end, that means the peak or highest element is the end element and can be returned.
    while l < r:
        mid = (l+r) // 2
        if arr[mid] < arr[mid+1]:
            l = mid + 1
        # another approach for the same problem, but less effective.
        # elif arr[mid-1] < arr[mid] > arr[mid+1]:
        #   return arr[mid]
        # else:
        #   r -= 1
        else:
            r = mid
    return arr[l]


print(findPeak([1, 2, 3, 2, 1], 5))  # 3
print(findPeak([1, 2, 3, 4, 5, 6], 6))  # 6
