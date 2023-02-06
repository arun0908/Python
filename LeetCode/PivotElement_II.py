# Given a sorted array, where k elements in the array are rotated and placed elsehwehere in the array. You are given the array, find the pivot
# element of the array. The pivot element of the array is either the most minimum value of the array or the highest value.

# To solve this we can use binary search as, upto a point the array is monotonous, then again it is monotonous. This makes it easy to apply BS
# We identify a condition,after we plot the array as a graph with two lines where we say, if the mid lies on the first increasing line,
# then we need to shift the mid forward, as the mid element lies at the bottom of the second line, as the minimum element, and the n-1 element
# is smaller or equal to the 0th element. Now if the mid element is greater than the 0th element, then it lies on the first line and left
# index is shifted to mid + 1. If not, we move the right index to mid and not mid - 1, because we do not want to shift the array limits to the
# first line.

def pivotElement(arr):
    l, r = 0, len(arr)-1
    while l < r:
        mid = (l+r)//2
        # Check if the mid is greater than 1st element and move the left pointer.
        if arr[mid] >= arr[0]:
            l = mid + 1
        else:
            r = mid
    return arr[l]

# An extension to the above problem is, given a sorted and rotated array, whose unkown count of elements have been rotated. Find the element k
# in the new array and return the index if present, else return -1.


def findElement(arr, k):
    pivot_index = pivotElement(arr)
    # We find out the pivot index first, then we can say if the element is greater than the pivot element, but less than the last element of
    # the array, then the element lies in the second part, else in the first part before the pivot index
    if arr[pivot_index] <= k <= arr[len(arr)-1]:
        pass
        # apply binary search from pivot index as l to the end of the array
    else:
        pass
        # apply binary search from start of the array to the pivot index - 1


print(pivotElement([7, 9, 1, 2, 3]))
print(pivotElement([2, 5, -3, 0]))
