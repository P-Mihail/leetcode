# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than
# 25% of the time, return that integer.
#
#
# Example 1:
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
#
# Example 2:
# Input: arr = [1,1]
# Output: 1
#
#
# Constraints:
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5


from typing import List
import bisect


class Solution:
    # def findSpecialInteger(self, arr: List[int]) -> int:
    #     q = len(arr) // 4
    #     p = 0
    #     while p < len(arr):
    #         if arr[p] == arr[p + q]:
    #             return arr[p]
    #         else:
    #             p = bisect.bisect_left(arr, arr[p + q], lo=p, hi=p + q)

    def findSpecialInteger(self, arr: List[int]) -> int:
        q = len(arr) // 4
        for x in [q, 2 * q, 3 * q, 4 * q]:
            p = bisect.bisect_left(arr, arr[x], lo=x - q, hi=x)
            if arr[p] == arr[p + q]:
                return arr[p]
        return -1
