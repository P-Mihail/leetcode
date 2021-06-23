# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.


from typing import List


class Solution(object):
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     # time complexity O(S * len(strs)), S = sum of all characters in all strings.
    #     # space complexity O(len(strs))
    #     i = 0
    #     for s in zip(*strs):
    #         if len(set(s)) == 1:
    #             i += 1
    #         else:
    #             break
    #     return strs[0][:i]
    #
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     # sorting and comparing first and last
    #     # fastest
    #     # time complexity in worst case (n equal strings with length m) O(S log n), n - len(strs), S = sum of all
    #     # characters in all strings
    #     strs.sort()
    #
    #     for i in range(len(strs[0])):
    #         if strs[0][i] != strs[-1][i]:
    #             return strs[0][:i]
    #
    #     return strs[0]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scanning
        # time complexity O(S), S = sum of all characters in all strings.
        # space complexity O(1)
        ans = ""

        for i in range(len(strs[0])):
            ch = strs[0][i : i + 1]
            if all(s[i : i + 1] == ch for s in strs):
                ans += ch
            else:
                return ans

        return ans
