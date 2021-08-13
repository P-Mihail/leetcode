# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
# You must do it in place.
# 
# Example 1:
# Input: matrix = [
# [1,1,1],
# [1,0,1],
# [1,1,1]]
# Output: [
# [1,0,1],
# [0,0,0],
# [1,0,1]]
# 
# Example 2:
# Input: matrix = [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]]
# Output: [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]]
# 
# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
# 
# Follow up:
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = not all(matrix[0])
        first_col_has_zero = False
        
        for row in matrix:
            if row[0] == 0:
                first_col_has_zero = True
                break
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0
                    
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                    
        if first_row_has_zero:
            matrix[0] = [0] * n
        
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0
