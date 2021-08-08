# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are
# a boomerang.
#
# A boomerang is a set of three points that are all distinct and not in a straight line.
#
#
# Example 1:
# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
#
# Example 2:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: false
#
#
# Constraints:
# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100


from typing import List
from itertools import combinations
from math import sqrt


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def dist(x1, y1, x2, y2):
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        d = sorted([dist(*p1, *p2) for p1, p2 in combinations(points, 2)])

        return d[0] != 0 and d[0] + d[1] - d[2] > 1e-5
