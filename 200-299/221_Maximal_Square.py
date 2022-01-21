# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Example 1:
#   ["1","0","1","0","0"]
#   ["1","0","1","1","1"]
#   ["1","1","1","1","1"]
#   ["1","0","0","1","0"]
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
#
# Example 2:
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#
# Example 3:
# Input: matrix = [["0"]]
# Output: 0
#
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.


from typing import List


class Solution:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     # Top-down Implementation
    #     # recursive
    #     @lru_cache(maxsize=None)
    #     def dp(y, x):
    #         if x < 0 or y < 0:
    #             return 0, 0

    #         if matrix[y][x] == "0":
    #             return 0, max(dp(y - 1, x)[1], dp(y, x - 1)[1])
    #         else:
    #             sqs = 1 + min(dp(y - 1, x - 1)[0], dp(y, x - 1)[0], dp(y - 1, x)[0])
    #             return sqs, max(dp(y - 1, x)[1], dp(y, x - 1)[1], sqs)

    #     return dp(len(matrix) - 1, len(matrix[0]) - 1)[1] ** 2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Bottom-up Implementation
        # iter
        ans = 0
        prev_row = [0] * (len(matrix[0]) + 1)

        for i in range(len(matrix)):
            curr_row = [0] * (len(matrix[0]) + 1)
            for j in range(len(matrix[i])):
                if matrix[i][j] == "0":
                    curr_row[j + 1] = 0
                else:
                    curr_row[j + 1] = 1 + min(curr_row[j], prev_row[j + 1], prev_row[j])
                    ans = max(ans, curr_row[j + 1])
            prev_row = curr_row

        return ans ** 2
