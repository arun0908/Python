def bubble_sort(input_array):
    if len(input_array) <= 0:
        return -1
    else:
        end_index = len(input_array) - 1
        is_swapped = False
        while end_index > 0:
            for i in range(end_index):
                if input_array[i] > input_array[i+1]:
                    is_swapped = True
                    temp = input_array[i]
                    input_array[i] = input_array[i+1]
                    input_array[i+1] = temp
            if not is_swapped:
                return input_array
            end_index -= 1
    return input_array

    # Alternate code
    # if len(arr) <= 0:
    #   return []
    # n = len(arr)
    # swapped = false
    # for i in range(n-1,0,-1):
    #   for j in range(i):
    #       if arr[j] > arr[j+1]:
    #           arr[j], arr[j+1] = arr[j+1], arr[j]
    #           swapped = true
    #   if swapped == false:
    #       break
    # return arr


print(bubble_sort([1, 2, 5, 3, 7, 4, 9, 6]))
