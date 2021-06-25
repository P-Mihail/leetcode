# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
# and Java's indexOf().
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0
#
# Constraints:
# 0 <= haystack.length, needle.length <= 5 * 10^4
# haystack and needle consist of only lower-case English characters.


class Solution(object):
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if len(needle) == 0:
    #         return 0
    #
    #     for i in range(len(haystack) - len(needle) + 1):
    #         if all(haystack[i + j] == needle[j] for j in range(len(needle))):
    #             return i
    #
    #     return -1

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1
