# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M
# ( i.e. N = 2 * M).
#
# More formally check if there exists two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
#
# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
#
# Example 2:
# Input: arr = [7,1,14,11]
# Output: true
#
# Example 3:
# Input: arr = [3,1,7,11]
# Output: false
#
# Constraints:
# 2 <= arr.length <= 500
# -10^3 <= arr[i] <= 10^3


from typing import List


class Solution(object):
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for i in arr:
            if 2 * i in s or (i % 2 == 0 and i // 2 in s):
                return True
            s.add(i)
        return False
