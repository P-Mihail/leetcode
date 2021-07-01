# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have
# different values.
#
#
#
# Example 1:
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
#
# Example 2:
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
#
# Example 3:
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
#
# Example 4:
# Input: n = 10
# Output: true
# Explanation: The binary representation of 10 is: 1010.
#
# Example 5:
# Input: n = 3
# Output: false
#
#
# Constraints:
#
# 1 <= n <= 2^31 - 1


class Solution(object):
    def hasAlternatingBits(self, n: int) -> bool:
        while n > 0:
            if not 3 > (n & 3) > 0:
                return False
            n >>= 1
        return True
