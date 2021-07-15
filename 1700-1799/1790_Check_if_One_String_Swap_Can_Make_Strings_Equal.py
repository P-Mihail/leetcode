# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a
# string (not necessarily different) and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the
# strings. Otherwise, return false.
#
# Example 1:
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
#
# Example 2:
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
#
# Example 3:
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.
#
# Example 4:
# Input: s1 = "abcd", s2 = "dcba"
# Output: false
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        tmp = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c += 1
                if c > 2:
                    return False
                tmp += [s1[i], s2[i]]

        if c == 1 or (c == 2 and (tmp[0] != tmp[3] or tmp[1] != tmp[2])):
            return False

        return True
