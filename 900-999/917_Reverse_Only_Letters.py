# Given a string s, return the "reversed" string where all characters that are not a letter stay in the same place, and
# all letters reverse their positions.
#
#
#
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
#
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
# Note:
# s.length <= 100
# 33 <= s[i].ASCIIcode <= 122
# s doesn't contain \ or "


class Solution(object):
    def reverseOnlyLetters(self, s: str) -> str:
        # 2 pointers
        # time complexity O(n)
        # space complexity O(n)
        pright = len(s) - 1
        ans = list(s)

        for pleft in range(len(s)):
            if s[pleft].isalpha():
                while not s[pright].isalpha():
                    pright -= 1
                ans[pleft] = s[pright]
                pright -= 1

        return "".join(ans)