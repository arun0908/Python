# Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum
# of the two numbers directly above it.
# Ex: Input: numRows = 5, Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


def generate(numRows: int) -> list[list[int]]:
    result = [[1]]
    for i in range(numRows - 1):
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    return result


print(generate(10))
