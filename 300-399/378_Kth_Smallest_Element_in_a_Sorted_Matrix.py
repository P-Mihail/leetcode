# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest
# element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
#
# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
#
# Example 2:
# Input: matrix = [[-5]], k = 1
# Output: -5
#
# Constraints:
#
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n^2


from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # time complexity O(n log n), n = len(matrix) ** 2
        # space complexity O(n)
        flatten = []
        for r in matrix:
            flatten += r

        flatten.sort()

        return flatten[k - 1]
