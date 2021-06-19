# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#   arr.length >= 3
#   There exists some i with 0 < i < arr.length - 1 such that:
#   arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#   arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
#
# Constraints:
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4


from typing import List


class Solution(object):
    # def validMountainArray(self, arr: List[int]) -> bool:
    #     # O(n)
    #     # use flag of increasing
    #     f = False
    #     for i in range(1, len(arr)):
    #         if arr[i - 1] == arr[i]:
    #             return False
    #         if (arr[i - 1] < arr[i]) == f:
    #             if f or i == 1:
    #                 return False
    #             else:
    #                 f = True
    #     return f

    def validMountainArray(self, arr: List[int]) -> bool:
        # O(n)
        # a little bit faster
        pointer = 0

        while pointer + 1 < len(arr) and arr[pointer] < arr[pointer + 1]:
            pointer += 1

        if pointer == 0 or pointer == len(arr) - 1:
            return False

        while pointer + 1 < len(arr):
            if arr[pointer] <= arr[pointer + 1]:
                return False
            pointer += 1

        return True
