# Given a string s, return the length of the longest substring between two equal characters, excluding the two
# characters. If there is no such substring return -1.
#
# A substring is a contiguous sequence of characters within a string.
#
#
# Example 1:
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
#
# Example 2:
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
#
# Example 3:
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
#
# Example 4:
# Input: s = "cabbac"
# Output: 4
# Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".
#
#
# Constraints:
# 1 <= s.length <= 300
# s contains only lowercase English letters.


from typing import Dict


class Solution:
    # def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    #     hm = {}
    #     ans = -1
    #
    #     for i in range(len(s)):
    #         if s[i] in hm:
    #             hm[s[i]][1] = i
    #             ans = max(ans, hm[s[i]][1] - hm[s[i]][0] - 1)
    #         else:
    #             hm[s[i]] = [i, i]
    #
    #     return ans

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hm: Dict[str, int] = {}
        ans = -1

        for i in range(len(s)):
            if s[i] in hm:
                ans = max(ans, i - hm[s[i]] - 1)
            else:
                hm[s[i]] = i

        return ans
