# Quick sort works on the concept of a pivot. If we consider a number in the input list, the numbers to the left of it are smaller than it,
# the numbers to the right of it are greater than it. Quick sort works on this consideration. We recursively sort the array on the pivot
# as the elements to the left of pivot are smaller than it, but not sorted and same for the right side.

# We consider a method for quick sort. Once we get a pivot position fron the partition method, we recursively sort the array, till each side is sorted
def quicksort(arr, l, r):
    # We consider this till the left index is smaller than the right index, once it is greater, we break it, as it is already sorted after that.
    if l < r:
        pivot_index = partition(arr, l, r)
        quicksort(arr, l, pivot_index-1)
        quicksort(arr, pivot_index+1, r)

# Method for partition, where we sort an element and partition the left and right side of the element and sort them recursively


def partition(arr, l, r) -> int:
    # The pivot index is considered as the left most index of the array
    pivot = l
    while l < r:
        # We first check, if any element after the pivot element is greater than it, because after placing the pivot element in the right place
        # we need the elements to the left of it to be smaller and right of it to be greater, which is the idea of quick sort.
        # We add the check if l < len(arr) to prevent list out of bound exceptions
        while l < len(arr) and arr[l] <= arr[pivot]:
            l += 1
        # We then see if any element from the right side is smaller than our pivot element for swapping it
        while arr[r] > arr[pivot]:
            r -= 1
        # Once we find the elements acc. to above logic, we check if the l index is < than r and swap them. If we swap them once they are greater
        # than each other, we will not be able to swap the pivot element.
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]

    # Swap the pivot element with the right index, as the element on right is smaller than pivot and needs to be swapped.
    arr[pivot], arr[r] = arr[r], arr[pivot]
    # we return the index of the sorted pivot, so that we can the partition array and sort it recursively.
    return r

    # Lumoto Partitioning
    # pivot = arr[r]
    # p_index = l

    # for i in range(l, r):
    #     if arr[i] <= pivot:
    #         swap(i, p_index, arr)
    #         p_index += 1

    # swap(p_index, r, arr)

    # return p_index


if __name__ == "__main__":
    arr = [11, 9, 29, 7, 2, 15, 28]
    quicksort(arr, 0, len(arr)-1)
    print(arr)
