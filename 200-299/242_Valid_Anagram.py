# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


from typing import Dict
from collections import defaultdict


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        c: Dict[str, int] = defaultdict(int)

        if len(s) != len(t):
            return False

        for ch in s:
            c[ch] += 1

        for ch in t:
            c[ch] -= 1
            if c[ch] < 0:
                return False

        return all(c[ch] == 0 for ch in c)
