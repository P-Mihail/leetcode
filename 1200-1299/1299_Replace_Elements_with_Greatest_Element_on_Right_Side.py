# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
#
# After doing so, return the array.
#
# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#
# Example 2:
# Input: arr = [400]
# Output: [-1]
#
# Constraints:
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5


from typing import List


class Solution(object):
    def replaceElements(self, arr: List[int]) -> List[int]:
        # time complexity: O(n)
        # space complexity: O(1)
        largest = -1

        for i in range(1, len(arr) + 1):
            pv = arr[-i]
            arr[-i] = largest

            if pv > largest:
                largest = pv

        return arr
