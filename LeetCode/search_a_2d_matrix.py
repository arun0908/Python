"""
You are given an m x n integer matrix matrix with the following two properties:
    1. Each row is sorted in non-decreasing order.
    2. The first integer of each row is greater than the last integer of the
    previous row.
    3. Given an integer target, return true if target is in matrix or false
    otherwise.
You must write a solution in O(log(m * n)) time complexity.
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search matrix for element using binary search
    """
    # Optimized approach using binary search, by first finding which row does
    # the element exist using binary search, then applying binary search to
    # find the element in resulting row

    top, bottom = 0, len(matrix)-1
    while top <= bottom:
        value_row = (top+bottom)//2
        if target < matrix[value_row][0]:
            bottom = value_row - 1
        elif target > matrix[value_row][-1]:
            top = value_row + 1
        else:
            break
    if not top <= bottom:
        return False
    row = (top + bottom)//2
    left, right = 0, len(matrix[row])-1
    while left <= right:
        mid = (left+right)//2
        if target < matrix[row][mid]:
            right = mid - 1
        elif target > matrix[row][mid]:
            left = mid + 1
        else:
            return True
    return False

    # initial approach
    # if len(matrix) == 1:
    #     if len(matrix[0]) == 1:
    #         if target == matrix[0][-1]:
    #             return True
    #         else:
    #             return False
    # result = False
    # for i in range(len(matrix)):
    #     if target > matrix[i][-1]:
    #         continue
    #     else:
    #         if target == matrix[i][-1]:
    #             return True
    #         else:
    #             l,r = 0,len(matrix[i])-1
    #             while l<r:
    #                 mid = l+r//2
    #                 if target == matrix[i][mid]:
    #                     result = True
    #                     return result
    #                 if target > matrix[i][mid]:
    #                     l = mid + 1
    #                 elif target < matrix[i][mid]:
    #                     r = mid-1
    # return False

    # Solution using python's inbuilt search algorithm-Timsort

    # for row in matrix:
    #     if target in row:
    #         return True
    # return False


print(search_matrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
