# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
#
# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.


from typing import List, Tuple
from collections import deque


class Solution:
    # def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    #     # bfs with queue
    #     # time complexity O(n)
    #     # space complexity O(n)
    #     ans = [[None] * len(mat[0]) for _ in range(len(mat))]
    #     q = deque()
    #
    #     for i in range(len(mat)):
    #         for j in range(len(mat[0])):
    #             if mat[i][j] == 0:
    #                 ans[i][j] = 0
    #                 q.append((i, j))
    #
    #     while q:
    #         i, j = q.popleft()
    #         t = ans[i][j] + 1
    #
    #         if i > 0 and ans[i - 1][j] is None:
    #             ans[i - 1][j] = t
    #             q.append((i - 1, j))
    #
    #         if i < len(mat) - 1 and ans[i + 1][j] is None:
    #             ans[i + 1][j] = t
    #             q.append((i + 1, j))
    #
    #         if j > 0 and ans[i][j - 1] is None:
    #             ans[i][j - 1] = t
    #             q.append((i, j - 1))
    #
    #         if j < len(mat[0]) - 1 and ans[i][j + 1] is None:
    #             ans[i][j + 1] = t
    #             q.append((i, j + 1))
    #
    #     return ans

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # bfs with hashset
        # time complexity O(n)
        # space complexity O(n)
        ans = [[None] * len(mat[0]) for _ in range(len(mat))]
        hs = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    hs.add((i, j))

        t = 1
        while hs:
            new_hs = set()
            for i, j in hs:
                if i > 0 and ans[i - 1][j] is None:
                    ans[i - 1][j] = t
                    new_hs.add((i - 1, j))
                if i < len(mat) - 1 and ans[i + 1][j] is None:
                    ans[i + 1][j] = t
                    new_hs.add((i + 1, j))
                if j > 0 and ans[i][j - 1] is None:
                    ans[i][j - 1] = t
                    new_hs.add((i, j - 1))
                if j < len(mat[0]) - 1 and ans[i][j + 1] is None:
                    ans[i][j + 1] = t
                    new_hs.add((i, j + 1))
            hs = new_hs
            t += 1

        return ans
