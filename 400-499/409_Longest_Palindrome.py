# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that
# can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
#
# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
# Example 2:
# Input: s = "a"
# Output: 1
#
# Example 3:
# Input: s = "bb"
# Output: 2
#
#
# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        a, b = 0, 0

        for n in freq.values():
            a += n // 2
            b += n % 2

        return 2 * a + (1 if b > 0 else 0)
