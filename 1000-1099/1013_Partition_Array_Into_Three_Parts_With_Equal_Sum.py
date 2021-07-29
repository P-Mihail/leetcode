# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] ==
# arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
#
#
# Example 1:
# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
# Example 2:
# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
#
# Example 3:
# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#
# Constraints:
# 3 <= arr.length <= 5 * 10^4
# -10^4 <= arr[i] <= 10^4


from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        ts = sum(arr)

        if ts % 3 != 0:
            return False

        s = ts // 3

        part_counter, cur_part_sum, pointer = 0, 0, 0
        while pointer < len(arr):
            cur_part_sum += arr[pointer]
            if cur_part_sum == s:
                part_counter += 1
                cur_part_sum = 0
                if part_counter == 2 and pointer < len(arr) - 1:
                    return True
            pointer += 1

        return False
