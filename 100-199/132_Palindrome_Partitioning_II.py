# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#
# Example 1:
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
# Example 2:
# Input: s = "a"
# Output: 0
#
# Example 3:
# Input: s = "ab"
# Output: 1
#
#
# Constraints:
# 1 <= s.length <= 2000
# s consists of lower-case English letters only.


class Solution:
    def minCut(self, s: str) -> int:
        def ispal(s):
            return s == s[::-1]

        dp = [-1] + [float("inf")] * len(s)

        for j in range(1, len(s) + 1):
            dp[j] = min(
                dp[i - 1] + 1
                for i in range(1, j + 1)
                if s[i - 1] == s[j - 1] and ispal(s[i - 1 : j])
            )

        return dp[-1]
