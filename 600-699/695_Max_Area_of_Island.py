# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.
#
# Example 1:
# Input: grid = [
#   [0,0,1,0,0,0,0,1,0,0,0,0,0],
#   [0,0,0,0,0,0,0,1,1,1,0,0,0],
#   [0,1,1,0,1,0,0,0,0,0,0,0,0],
#   [0,1,0,0,1,1,0,0,1,0,1,0,0],
#   [0,1,0,0,1,1,0,0,1,1,1,0,0],
#   [0,0,0,0,0,0,0,0,0,0,1,0,0],
#   [0,0,0,0,0,0,0,1,1,1,0,0,0],
#   [0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
#
# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0


# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.


from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(x0, y0):
            res = 0
            stack = [[y0, x0]]
            grid[y0][x0] = -1
            while stack:
                y, x = stack.pop()
                res += 1
                if x > 0 and grid[y][x - 1] == 1:
                    grid[y][x - 1] = -1
                    stack.append([y, x - 1])
                if y > 0 and grid[y - 1][x] == 1:
                    grid[y - 1][x] = -1
                    stack.append([y - 1, x])
                if x < len(grid[0]) - 1 and grid[y][x + 1] == 1:
                    grid[y][x + 1] = -1
                    stack.append([y, x + 1])
                if y < len(grid) - 1 and grid[y + 1][x] == 1:
                    grid[y + 1][x] = -1
                    stack.append([y + 1, x])
            return res

        ans = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    ar = area(x, y)
                    ans = max(ans, ar)

        return ans
