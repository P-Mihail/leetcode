# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array
# contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
# Example 3:
# Input: digits = [0]
# Output: [1]
#
# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9


from typing import Deque, List
from collections import deque


class Solution(object):
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     # inplace
    #     # time complexity O(n)
    #     # space complexity O(1)
    #     for i in range(len(digits) - 1, -1, -1):
    #         digits[i] += 1
    #         if digits[i] == 10:
    #             digits[i] = 0
    #             if i == 0:
    #                 digits.insert(0, 1)
    #                 break
    #         else:
    #             break
    #     return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        # time complexity O(n)
        # space complexity O(n)
        ans: Deque[int] = deque()
        rem = 1

        for i in range(len(digits) - 1, -1, -1):
            ans.appendleft(digits[i] + rem)
            if ans[0] == 10:
                ans[0] = 0
            else:
                rem = 0

        if rem == 1:
            ans.appendleft(1)

        return list(ans)
