# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
# Constraints:
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


from itertools import zip_longest


class Solution(object):
    # def addBinary(self, a: str, b: str) -> str:
    #     # pythonic
    #     return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a: str, b: str) -> str:
        ans, o = [], 0

        for x, y in zip_longest(a[::-1], b[::-1], fillvalue="0"):
            o, z = divmod(int(x) + int(y) + o, 2)
            ans.append(str(z))

        return ("1" if o == 1 else "") + "".join(ans[::-1])
