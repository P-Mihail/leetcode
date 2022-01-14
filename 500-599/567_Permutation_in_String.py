# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
# Constraints:
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = {}

        for ch in s1:
            c[ch] = c.get(ch, 0) + 1

        hm = {}
        sublen = 0

        for i, ch in enumerate(s2):
            hm[ch] = hm.get(ch, 0) + 1

            while hm[ch] > c.get(ch, 0):
                hm[s2[i - sublen]] -= 1
                sublen -= 1

            sublen += 1
            if sublen == len(s1):
                return True

        return False
