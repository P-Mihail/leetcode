# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
# backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#
# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#
# Example 3:
# Input: s = "a##c", t = "#a#c"
# Output: true
# Explanation: Both s and t become "c".
#
# Example 4:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
#
# Constraints:
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
#
#
# Follow up: Can you solve it in O(n) time and O(1) space?


from itertools import zip_longest


class Solution:
    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     # time complexity O(m+n)
    #     # space complexity O(m+n)
    #     def build(s: str) -> str:
    #         ans = []
    #         for c in s:
    #             if c != "#":
    #                 ans.append(c)
    #             elif ans:
    #                 ans.pop()
    #         return "".join(ans)
    #
    #     return build(s) == build(t)

    def backspaceCompare(self, s: str, t: str) -> bool:
        # time complexity O(m+n)
        # space complexity O(1)
        def helper(s: str):
            skip = 0
            for x in s[::-1]:
                if x == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in zip_longest(helper(s), helper(t)))
