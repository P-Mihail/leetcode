# Given an integer n, return true if it is a power of four. Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4x.
#
#
# Example 1:
# Input: n = 16
# Output: true
#
# Example 2:
# Input: n = 5
# Output: false
#
# Example 3:
# Input: n = 1
# Output: true
#
# Constraints:
# -2^31 <= n <= 2^31 - 1
#
#
# Follow up: Could you solve it without loops/recursion?


from math import log


class Solution:
    # def isPowerOfFour(self, n: int) -> bool:
    #     # loop
    #     if n <= 0:
    #         return False
    #
    #     while n > 1:
    #         if n & 3 != 0:
    #             return False
    #         n >>= 2
    #
    #     return True

    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log(num, 4).is_integer()
