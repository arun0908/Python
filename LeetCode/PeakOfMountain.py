# Given an array of n integers. Find the peak of the array. The peak element of the array is defined as the element which is greater than
# arr[i-1] and is greater than arr[i+1] where arr[i] is the element. It is guaranteed that there is only one peak element.

def findPeak(arr, n):
    l , r = 0, n-1
    while l < r:
        mid = (l+r) //2
        if arr[mid] < arr[mid+1]:
            l = mid + 1
        else:
            r = mid
    return l

print(findPeak([2,3,4,1,-4], 5))  # 4
print(findPeak([1,2,3,4,5,6], 6))  # 6