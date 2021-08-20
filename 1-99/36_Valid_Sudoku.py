# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the 
# following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# 
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# 
# Example 1:
# 5 3 _ _ 7 _ _ _ _
# 6 _ _ 1 9 5 _ _ _
# _ 9 8 _ _ _ _ 6 _
# 8 _ _ _ 6 _ _ _ 3
# 4 _ _ 8 _ 3 _ _ 1
# 7 _ _ _ 2 _ _ _ 6
# _ 6 _ _ _ _ 2 8 _
# _ _ _ 4 1 9 _ _ 5
# _ _ _ _ 9 _ _ 7 9
#
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# 
# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# 
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [[0]*9 for _ in range(3)]

        for r in range(9):
            for c in range(9):
                ch = board[r][c]

                if ch == ".":
                    continue

                n = (1 << int(ch)-1)
                b = (r//3)*3 + c//3
                if rows[r] & n or cols[c] & n or boxes[b] & n:
                    return False

                rows[r] |= n
                cols[c] |= n
                boxes[b] |= n

        return True
