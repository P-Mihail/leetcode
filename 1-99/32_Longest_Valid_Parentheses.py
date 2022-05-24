# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
# Example 3:
# Input: s = ""
# Output: 0
#
# Constraints:
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # time complexity O(n)
        # space complexity O(1)
        lbc, rbc, ans = 0, 0, 0

        for b in s:
            if b == "(":
                lbc += 1
            else:
                rbc += 1
            if rbc == lbc:
                ans = max(ans, rbc)
            elif rbc > lbc:
                lbc = rbc = 0

        lbc = rbc = 0

        for b in s[::-1]:
            if b == "(":
                lbc += 1
            else:
                rbc += 1
            if lbc == rbc:
                ans = max(ans, lbc)
            elif lbc > rbc:
                lbc = rbc = 0

        return 2 * ans

