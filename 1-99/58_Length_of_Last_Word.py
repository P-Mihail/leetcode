# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the
# last word does not exist, return 0.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
#
# Example 1:
# Input: s = "Hello World"
# Output: 5

# Example 2:
# Input: s = " "
# Output: 0
#
# Constraints:
#
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '.


class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     # bad as answer, but fast and simple
    #     return len(s.strip().split(" ")[-1])

    def lengthOfLastWord(self, s: str) -> int:
        # time complexity O(n) 1 pass
        # space complexity O(1)
        ans = 0

        for i in range(1, len(s) + 1):
            if s[-i] == " ":
                if ans != 0:
                    return ans
            else:
                ans += 1

        return ans
