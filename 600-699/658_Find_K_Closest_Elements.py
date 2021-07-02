# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result
# should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
#
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
# Constraints:
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4


import bisect
from typing import List


class Solution:
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     # time complexity O(n log(n) + k log(k)), n = len(arr)
    #     # space complexity = O(n)
    #     return sorted(sorted(arr, key=lambda a: abs(a - x))[:k])

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # time complexity O(log(n) + k), n = len(arr)
        # space complexity O(1)
        i = bisect.bisect_left(arr, x)
        li, ri = i - 1, i

        while ri - li - 1 < k:
            if li == -1:
                ri += 1
            elif ri == len(arr) or abs(arr[li] - x) <= abs(arr[ri] - x):
                li -= 1
            else:
                ri += 1

        return arr[li + 1 : ri]
