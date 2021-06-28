# Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest
# contiguous segment of 0s in s. Return false otherwise.
#
# For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment
# of 0s has length 3.
# Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same
# applies if there are no 1s.
#
#
#
# Example 1:
# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.
#
# Example 2:
# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.
#
# Example 3:
# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.
#
# Constraints:
# 1 <= s.length <= 100
# s[i] is either '0' or '1'.


class Solution(object):
    # def checkZeroOnes(self, s: str) -> bool:
    #     # time complexity O(n)
    #     # size complexity O(1)
    #     longest_0, longest_1 = 0, 0
    #     curlongest_0, curlongest_1 = 0, 0
    #
    #     for char in s:
    #         if char == "0":
    #             curlongest_0 += 1
    #             curlongest_1 = 0
    #         else:
    #             curlongest_0 = 0
    #             curlongest_1 += 1
    #
    #         longest_0 = max(longest_0, curlongest_0)
    #         longest_1 = max(longest_1, curlongest_1)
    #
    #     return longest_1 > longest_0

    def checkZeroOnes(self, s: str) -> bool:
        # time complexity O(n)
        # size complexity O(1)
        longest = {"0": 0, "1": 0}

        curchar, curlen = s[0], 0

        for char in s:
            if curchar == char:
                curlen += 1
            else:
                curchar = char
                curlen = 1

            longest[curchar] = max(longest[curchar], curlen)

        return longest["1"] > longest["0"]
