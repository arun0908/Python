def insertion_sort(arr, n) -> list:
    # insertion sort works by considering a sorted portion of the array, and
    # an unsorted portion of the array we take the left side as the swapped
    # part and we find an element which is to be arranged in the descending
    # order and push it to the left side, i.e. the sorted side.

    if n == 0:
        return []
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


print(insertion_sort([10, 2, 5, 4, 8, 9], 6))
print(insertion_sort([0, 1, 3, 2, 4, 5, 1], 7))
