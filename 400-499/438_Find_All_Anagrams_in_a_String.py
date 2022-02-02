# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
# Constraints:
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.


from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = Counter(p)
        tc = defaultdict(int)

        pl = pr = n = 0
        ans = []

        while pr < len(s):
            ch = s[pr]
            if ch in c:
                tc[ch] += 1
                n += 1
                while tc[ch] > c[ch]:
                    n -= 1
                    tc[s[pl]] -= 1
                    pl += 1
                if n == len(p):
                    ans.append(pl)
                    tc[s[pl]] -= 1
                    pl += 1
                    n -= 1
                pr += 1
            else:
                pl = pr = pr + 1
                tc = defaultdict(int)
                n = 0

        return ans
