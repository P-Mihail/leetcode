# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.
#
#
# Example 1:
# Input: num = 16
# Output: true
#
# Example 2:
# Input: num = 14
# Output: false
#
#
# Constraints:
# 1 <= num <= 2^31 - 1


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lp = 1
        rp = num

        while lp <= rp:
            m = (lp + rp) // 2
            m2 = m ** 2
            if m2 == num:
                return True
            elif m2 > num:
                rp = m - 1
            else:
                lp = m + 1

        return False
