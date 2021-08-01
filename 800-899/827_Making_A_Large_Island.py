# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
#
# Return the size of the largest island in grid after applying this operation.
#
# An island is a 4-directionally connected group of 1s.
#
#
#
# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
#
# Example 2:
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
#
# Example 3:
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
#
# Constraints:
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.


from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # time complexity O(n^2)
        # space complexity O(n^2)
        N = len(grid)

        groupidx = 2
        groups = {0: 0}

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    groupsize = 0
                    stack = [[i, j]]
                    while stack:
                        y, x = stack.pop()
                        if grid[y][x] == 1:
                            grid[y][x] = groupidx
                            groupsize += 1
                            if x > 0:
                                stack.append([y, x - 1])
                            if x < N - 1:
                                stack.append([y, x + 1])
                            if y > 0:
                                stack.append([y - 1, x])
                            if y < N - 1:
                                stack.append([y + 1, x])
                    groups[groupidx] = groupsize
                    groupidx += 1

        ans = max(groups.values() or [0])

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    used = set()
                    ps = 1
                    if j > 0:
                        ps += groups[grid[i][j - 1]]
                        used.add(grid[i][j - 1])
                    if j < N - 1:
                        if grid[i][j + 1] not in used:
                            ps += groups[grid[i][j + 1]]
                            used.add(grid[i][j + 1])
                    if i > 0:
                        if grid[i - 1][j] not in used:
                            ps += groups[grid[i - 1][j]]
                            used.add(grid[i - 1][j])
                    if i < N - 1:
                        if grid[i + 1][j] not in used:
                            ps += groups[grid[i + 1][j]]
                            used.add(grid[i + 1][j])
                    ans = max(ans, ps)

        return ans
