# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
# 
# Example 1:
# Input: s = "hello"
# Output: "holle"
# 
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
# 
# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = []
        vowels = set('aeiouAEIOU')
        pr = len(s)
        for ch in s:
            if ch in vowels:
                pr -= 1
                while s[pr] not in vowels:
                    pr -= 1
                ans.append(s[pr])
            else:
                ans.append(ch)
        return "".join(ans)
