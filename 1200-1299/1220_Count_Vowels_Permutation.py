# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
#
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
#
# Example 2:
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
#
# Example 3:
# Input: n = 5
# Output: 68
#
#
# Constraints:
#
# 1 <= n <= 2 * 10^4


class Solution(object):
    def countVowelPermutation(self, n: int) -> int:
        # time complexity O(n)
        # space complexity O(1)
        # char - aeiou
        # idx  - 01234
        count = [1] * 5
        mod = 1000000007

        for _ in range(n - 1):
            count = [
                (count[1] + count[2] + count[4]) % mod,
                (count[0] + count[2]) % mod,
                (count[1] + count[3]) % mod,
                count[2] % mod,
                (count[2] + count[3]) % mod,
            ]

        return sum(count) % mod
