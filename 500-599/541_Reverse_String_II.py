# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of
# the string.
#
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to
# k characters, then reverse the first k characters and left the other as original.
#
#
# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#
# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"
#
#
# Constraints:
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^4


class Solution:
    # def reverseStr(self, s: str, k: int) -> str:
    #     ans = ""
    #
    #     for i in range(len(s) // (2 * k) + 1):
    #         ans += s[i * 2 * k : i * 2 * k + k][::-1]
    #         ans += s[i * 2 * k + k : (i + 1) * 2 * k]
    #
    #     return ans

    def reverseStr(self, s: str, k: int) -> str:
        ans = list(s)

        for i in range(len(s) // (2 * k) + 1):
            ans[i * 2 * k : i * 2 * k + k] = ans[i * 2 * k : i * 2 * k + k][::-1]

        return "".join(ans)
