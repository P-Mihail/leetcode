# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
#
#
#
# Example 1:
#  1 2 3 4
#  5 1 2 3
#  9 5 1 2
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
#
# Example 2:
# 1 2
# 2 2
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.
#
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99
#
# Follow up:
# What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the
# matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into the memory at once?


from typing import Dict, List


class Solution:
    #     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #         # time complexity O(M*N)
    #         # space complexity O(M)
    #         r = matrix[0][:-1]

    #         for row in matrix[1:]:
    #             if r == row[1:]:
    #                 r = row[:-1]
    #             else:
    #                 return False

    #         return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # time complexity O(M*N)
        # space complexity O(M+N)
        d: Dict[int, int] = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j in d and d[i - j] != matrix[i][j]:
                    return False
                else:
                    d[i - j] = matrix[i][j]

        return True
