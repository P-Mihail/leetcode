# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible
# palindrome partitioning of s.
#
# A palindrome string is a string that reads the same backward as forward.
#
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
#
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def dfs(s, path):
            if s == "":
                ans.append(path.copy())
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[i - 1 :: -1]:
                    path.append(s[:i])
                    dfs(s[i:], path)
                    path.pop()

        dfs(s, [])
        return ans
