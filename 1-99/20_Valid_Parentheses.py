# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([)]"
# Output: false
#
# Example 5:
# Input: s = "{[]}"
# Output: true
#
# Constraints:
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'


class Solution(object):
    # def isValid(self, s: str) -> bool:
    #     # stack
    #     # time complexity: O(n)
    #     # space complexity: O(n)
    #     brackets = {")": "(", "}": "{", "]": "["}
    #     open_brackets = []
    #
    #     for b in s:
    #         if b not in brackets:
    #             open_brackets.append(b)
    #         elif len(open_brackets) == 0 or open_brackets.pop() != brackets[b]:
    #             return False
    #
    #     return len(open_brackets) == 0

    def isValid(self, s: str) -> bool:
        # stack
        # time complexity: O(n)
        # space complexity: O(n)
        m = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in m.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or c != m[stack.pop()]:
                    return False
        return len(stack) == 0
