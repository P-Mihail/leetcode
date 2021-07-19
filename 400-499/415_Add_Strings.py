# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You
# must also not convert the inputs to integers directly.
#
#
# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
# Constraints:
# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.


from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = 0
        ans = ""

        for x, y in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            m, s = divmod(ord(x) + ord(y) + m - 2 * ord("0"), 10)
            ans = f"{s}{ans}"

        return ("1" if m == 1 else "") + ans
