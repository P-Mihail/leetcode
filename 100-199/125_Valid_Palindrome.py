# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.


class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     # faster but
    #     # time complexity O(n)
    #     # space complexity O(n)
    #     s = [i for i in s.lower() if i.isalnum()]
    #     return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        # 2 pointers
        # time complexity O(n)
        # space complexity O(1)
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True
