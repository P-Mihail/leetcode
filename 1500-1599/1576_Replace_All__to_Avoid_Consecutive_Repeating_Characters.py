# Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into
# lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify
# the non '?' characters.
#
# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
#
# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution,
# return any of them. It can be shown that an answer is always possible with the given constraints.
#
#
# Example 1:
# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid
# modification as the string will consist of consecutive repeating characters in "zzs".
#
# Example 2:
# Input: s = "ubv?w"
# Output: "ubvaw"
# Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will
# consist of consecutive repeating characters in "ubvvw" and "ubvww".
#
# Example 3:
# Input: s = "j?qg??b"
# Output: "jaqgacb"
#
# Example 4:
# Input: s = "??yw?ipkj?"
# Output: "acywaipkja"
#
#
# Constraints:
# 1 <= s.length <= 100
# s contains only lower case English letters and '?'.


class Solution:
    def modifyString(self, s: str) -> str:
        ans = []

        for i, ch in enumerate(s):
            if ch != "?":
                ans.append(ch)
            else:
                prev_ch = ans[-1] if i > 0 else ""
                next_ch = s[i + 1] if i < len(s) - 1 else ""
                if "a" != prev_ch and "a" != next_ch:
                    ans.append("a")
                elif "b" != prev_ch and "b" != next_ch:
                    ans.append("b")
                else:
                    ans.append("c")

        return "".join(ans)
