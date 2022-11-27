# Merge sort array using divide and conquer method
# Divide the array into sub arrays and then join them
def merge_sort(array):
    if len(array) <= 1:
        return
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_arrays(left, right, array)


# Sort two arrays and merge them
def merge_sorted_arrays(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = 0
    j = 0
    k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


# Given an array of and asked to merge sort them
arr = [5, 2, 6, 3, 1, 4, 21]
merge_sort(arr)
print(arr)

