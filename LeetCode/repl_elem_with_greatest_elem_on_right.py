# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.

def replaceElements(self, arr: list[int]) -> list[int]:
    right_max = -1
    for i in range(len(arr) - 1, -1, -1):
        new_max = max(right_max, arr[i])
        arr[i] = right_max
        right_max = new_max
    return arr
