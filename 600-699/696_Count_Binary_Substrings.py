# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all
# the 0's and all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
#
#
# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10",
# "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
#
# Example 2:
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
#
#
# Constraints:
# 1 <= s.length <= 10^5
# s[i] is either '0' or '1'.


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zc, oc = (0, 1) if s[0] == "1" else (1, 0)
        ans = 0

        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] == "0":
                    zc += 1
                else:
                    zc = 1
                if oc > 0:
                    oc -= 1
                    ans += 1
            else:
                if s[i - 1] == "1":
                    oc += 1
                else:
                    oc = 1
                if zc > 0:
                    zc -= 1
                    ans += 1

        return ans
