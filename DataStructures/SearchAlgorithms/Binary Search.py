"""You're going to write a binary search function. You should use an iterative approach - meaning
using loops. Your function should take two inputs: a Python list to search through, and the value
you're searching for. Assume the list only has distinct elements, meaning there are no repeated values, and
elements are in a strictly increasing order. Return the index of value, or -1 if the value doesn't exist in the list."""


# Iterative Method
def binary_search(input_array, value):
    start_index = 0
    end_index = len(input_array)-1
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2
        if value > input_array[mid_index]:
            start_index = mid_index + 1
        elif value < input_array[mid_index]:
            end_index = mid_index - 1
        else:
            return mid_index
    return -1


# Recursive Method
def binary_search_recur(input_array, start_index, end_index, value):
    mid_index = (start_index + end_index)//2
    if value == input_array[mid_index]:
        return mid_index
    if value > input_array[mid_index]:
        return binary_search_recur(input_array, mid_index + 1, end_index, value)
    elif value < input_array[mid_index]:
        return binary_search_recur(input_array, start_index, mid_index - 1, value)
    else:
        return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
