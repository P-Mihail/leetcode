# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
# "abcde" while "aec" is not).
#
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
#
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one
# to see if t has its subsequence. In this scenario, how would you change your code?


class Solution:
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     # time complexity O(n + m)
    #     # space complexity O(1)
    #     if len(s) == 0:
    #         return True
    #
    #     ps, pt = 0, 0
    #
    #     while pt < len(t):
    #         if s[ps] == t[pt]:
    #             ps += 1
    #             if ps == len(s):
    #                 return True
    #         pt += 1
    #
    #     return False

    # def isSubsequence(self, s: str, t: str) -> bool:
    #     # time complexity O(n + m)
    #     # space complexity O(1)
    #     if len(s) == 0:
    #         return True
    #
    #     ps = 0
    #
    #     for ch in t:
    #         if s[ps] == ch:
    #             ps += 1
    #             if ps == len(s):
    #                 return True
    #
    #     return False

    def isSubsequence(self, s: str, t: str) -> bool:
        # fastest
        # time complexity O(n + m)
        # space complexity O(1)
        if len(s) == 0:
            return True

        ps, pt = -len(s), -len(t)

        while ps >= pt < 0:
            if s[ps] == t[pt]:
                ps += 1
                if ps == 0:
                    return True
            pt += 1

        return False
