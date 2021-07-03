# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is
# no larger than k.
#
# It is guaranteed that there will be a rectangle with a sum no larger than k.
#
#
#
# Example 1:
# 1 | 0 1|
# 0 |-2 3|
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k
# (k = 2).
#
# Example 2:
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
#
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -10^5 <= k <= 10^5
#
# Follow up: What if the number of rows is much larger than the number of columns?


from typing import List
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(n - 1):
                row[i + 1] += row[i]
        maxSum = float("-inf")
        for i in range(n):
            for j in range(i, n):
                cur = 0
                prefixSums = [float("inf")]
                for r in range(m):
                    bisect.insort(prefixSums, cur)
                    cur += matrix[r][j] - (matrix[r][i - 1] if i > 0 else 0)
                    tmp = bisect.bisect_left(prefixSums, cur - k)
                    maxSum = max(maxSum, cur - prefixSums[tmp])
        return int(maxSum)
