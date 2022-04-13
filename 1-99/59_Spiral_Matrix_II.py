# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#
# Example 1:
#
# 1 2 3
# 8 9 4
# 7 6 5
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
# Example 2:
# Input: n = 1
# Output: [[1]]
#
# Constraints:
# 1 <= n <= 20

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        xy = {"x": 0, "y": 0}

        direction = "R"

        init = [
            ["R", "x", n, 1, "B"],
            ["B", "y", n, 1, "L"],
            ["L", "x", -1, -1, "T"],
            ["T", "y", 0, -1, "R"],
        ]
        d = {
            x[0]: {k: x[i + 1] for i, k in enumerate(["xy", "edge", "dxy", "next_dir"])}
            for x in init
        }

        for i in range(1, n ** 2 + 1):
            ans[xy["y"]][xy["x"]] = i

            if xy[d[direction]["xy"]] + d[direction]["dxy"] == d[direction]["edge"]:
                d[direction]["edge"] -= d[direction]["dxy"]
                direction = d[direction]["next_dir"]

            xy[d[direction]["xy"]] += d[direction]["dxy"]

        return ans
