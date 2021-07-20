# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
#
# Example 1:
# Input: s = "aba"
# Output: true
#
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
# Example 3:
# Input: s = "abc"
# Output: false
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        pl, pr = 0, len(s) - 1

        while pl < pr:
            if s[pl] != s[pr]:
                return isPalindrome(s[pl + 1 : pr + 1]) or isPalindrome(s[pl:pr])
            else:
                pl += 1
                pr -= 1

        return True
