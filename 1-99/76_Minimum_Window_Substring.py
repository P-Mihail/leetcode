# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
# character in t (including duplicates) is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.
#
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?


from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        uniqch = 0
        chinwin = {}
        pl = pr = 0
        ans = (len(s) + 1, None, None)
        while pr < len(s):
            if s[pr] in ct:
                chinwin[s[pr]] = chinwin.get(s[pr], 0) + 1
                if chinwin[s[pr]] == ct[s[pr]]:
                    uniqch += 1
                    while pl <= pr and uniqch == len(ct):
                        if s[pl] in ct:
                            if pr - pl + 1 < ans[0]:
                                ans = (pr - pl + 1, pl, pr)
                            chinwin[s[pl]] -= 1
                            if chinwin[s[pl]] < ct[s[pl]]:
                                uniqch -= 1
                        pl += 1
            pr += 1
        return "" if ans[0] == len(s) + 1 else s[ans[1]: ans[2] + 1]
