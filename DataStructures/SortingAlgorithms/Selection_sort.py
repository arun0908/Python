def selection_sort(arr, n) -> list:
    # In selection sort we sort the array from the start to the end. We select
    # the smallest element from the array first and then swap it with the
    # initial index, unlike bubble sort, where weperform multiple swaps and we
    # traverse in the reverse order.

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


print(selection_sort([10, 2, 5, 4, 8, 9], 6))
