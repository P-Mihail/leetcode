# Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest 
# uncommon subsequence does not exist, return -1.
# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc".
# Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
# 
# Example 1:
# Input: strs = ["aba","cdc","eae"]
# Output: 3
# 
# Example 2:
# Input: strs = ["aaa","aaa","aa"]
# Output: -1
# 
# Constraints:
# 1 <= strs.length <= 50
# 1 <= strs[i].length <= 10
# strs[i] consists of lowercase English letters.


from collections import Counter
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        C = Counter(strs)
        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if C[s] > 1:
                continue
            done = True

            for i in range(i):
                p = -1
                flag = True
                for ch in s:
                    p = strs[i].find(ch, p + 1)
                    if p == -1:
                        flag = False
                        break
                if flag:
                    done = False
                    break
            if done:
                return len(s)

        return -1
