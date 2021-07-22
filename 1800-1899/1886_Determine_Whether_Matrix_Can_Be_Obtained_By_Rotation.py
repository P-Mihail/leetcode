# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating
# mat in 90-degree increments, or false otherwise.
#
#
# Example 1:
# 0 1    1 0
# 1 0    0 1
# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
#
# Example 2:
# 0 1     1 0
# 1 1     0 1
# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.
#
# Example 3:
# 0 0 0     1 1 1
# 0 1 0     0 1 0
# 1 1 1     0 0 0
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
#
#
# Constraints:
# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 <= n <= 10
# mat[i][j] and target[i][j] are either 0 or 1.


from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        r0 = r1 = r2 = r3 = True
        for i in range(n):
            for j in range(n):
                if r0 and target[i][j] != mat[i][j]:
                    r0 = False
                if r1 and target[i][j] != mat[j][n - i - 1]:
                    r1 = False
                if r2 and target[i][j] != mat[n - i - 1][n - j - 1]:
                    r2 = False
                if r3 and target[i][j] != mat[n - j - 1][i]:
                    r3 = False

                if r0 or r1 or r2 or r3:
                    continue
                else:
                    return False

        return True
