# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Solution:
# To avoid duplicates, what would be the better option to store values:  HashSet
# Which format can values be stored in for best efficiency:  Hashmap of HashSet for columns, rows, grid of 3*3, with row
#                                                            and column no as keys
# Each row and column can be stored in the HashMap for rows and columns with their keys being row no and column no, and
# value in the cell is appended to the corresponding key-value pair of type set, which returns false if duplicate value
# is being appended.
# The HashMap for grid will contain each grid value, where each grid is represented as a combination of grid row no,
# grid column no. Say suppose, 0,0 to 2,2 fall under first grid, 0,3 to 2,5 fall under second grid and so on. But the
# way to convert row no and column no to grid row, grid column would be to perform an integer division by 3 for the row
# no and the column no in the grids.
# For Ex: row no 2, column no 2 come under grid(0,0). So the grid number is obtained by performing (2//3 , 2//3) which are
# rounded to (0,0). The same for 8,8 which equates to grid number (2,2). So 3* grids from 0,0 to 2,2 with each cell in
# them being appended to their corresponding set in the grid map and if any duplicates are found, will return False

from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    # Create respective Hashmaps of Hashsets
    col_map = defaultdict(set)
    row_map = defaultdict(set)
    grid_map = defaultdict(set)

    # Loop through each row and each column of board
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == ".":
                continue
            elif board[r][c] in row_map[r] or board[r][c] in col_map[c] or board[r][c] in grid_map[r // 3, c // 3]:
                return False
            row_map[r].add(board[r][c])
            col_map[c].add(board[r][c])
            grid_map[r //3, c//3].add(board[r][c])
    return True


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))  # True
print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))  # False



