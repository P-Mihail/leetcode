# Given an integer n, add a dot (".") as the thousands separator and return it in string format.
#
#
# Example 1:
# Input: n = 987
# Output: "987"
#
# Example 2:
# Input: n = 1234
# Output: "1.234"
#
# Example 3:
# Input: n = 123456789
# Output: "123.456.789"
#
# Example 4:
# Input: n = 0
# Output: "0"
#
# Constraints:
# 0 <= n < 2^31


class Solution:
    # def thousandSeparator(self, n: int) -> str:
    #     # pythonic
    #     return f"{n:,}".replace(",", ".")

    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        ans = s[0]

        for i in range(1, len(s)):
            if i % 3 == len(s) % 3:
                ans += f".{s[i]}"
            else:
                ans += s[i]

        return ans
