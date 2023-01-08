# You have been given a sorted array arr consisting of n elements. You are given an integer k. Find the first and last occurance of the integer
# k in the arr. If there are no occurances of the element, return -1. Note: The array may consist of duplicate elements.
# Follow up : Solve the problem in O(log n) time complexity.

def firstAndLastPosition(arr, n, k):
# The solution to solve it in said time complexity would be to use binary search. Problem can be solved in two parts.
# First find the first occurance/leftmost occurance and then the last occurance/rightmost occurance.

    l , r = 0, n-1
    first_occurance = -1
    last_occurance = -1
    # Finding the leftmost occurance or the first occurance
    while l <= r:
        mid = (l + r)//2
        if arr[mid] == k:
            first_occurance = mid 
            r = mid - 1 # eventhough the element is found, we traverse through the left array to find the first occurance and store it instead.
        if arr[mid] > k:
            r = mid - 1
        if arr[mid] < k:
            l = mid + 1
    if first_occurance == -1:
        return [-1, -1]
    l , r = 0, n-1
    # Finding the rightmost occurance or the last occurance
    while l <= r:
        mid = (l + r)//2
        if arr[mid] == k:
            last_occurance = mid
            l = mid + 1 # eventhough the element is found, we traverse through the right array to find the last occurance and store it instead.
        if arr[mid] > k:
            r = mid - 1
        if arr[mid] < k:
            l = mid + 1
    return [first_occurance, last_occurance]
    # Extension : To find the total occurances of an element, we can use the same method to find the first and last occurance 
    # return ((last_occurance + first_occurance)- 1)


print(firstAndLastPosition([0,0,0,0], 4, 0))  # [0,3]
print(firstAndLastPosition([1,1,2,2,3,3], 6, 4))  # [-1,-1]

