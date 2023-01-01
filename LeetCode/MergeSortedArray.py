def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # The trick here is to start from the end, as we can fill up the zeros first and then keep the nums1 array same

    # Consider an element which stores the value of the last pointer
    
    last = m + n - 1 # Or we can even consider len(nums)-1 as nums1 is of length m + n 
    # Looping through both arrays while their lengths are greater than 0
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        # In case element in nums2 is greater than nums1 or is equal we will replace with element in nums2
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1
    # In case elements are left over in m, we can let it be as nums1 is already sorted and in order according to logic
    # If elements in n are left over, we need to insert them in nums1
    while n > 0:
        nums1[last] = nums2[n-1]
        n, last = n-1, last-1
    # For de-bugging
    print(nums1)


print(merge([1,2,3,0,0,0],3,[2,5,6],3))  # [1,2,2,3,5,6]
