# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
#
#
# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
# Example 2:
# Input: n = 25
# Output: 1389537
#
#
# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


# class Solution:
#     def tribonacci(self, n: int) -> int:
#         tn = [0, 1, 1]

#         if n < len(tn) - 1:
#             return tn[n]

#         for i in range(3, n + 1):
#             tn.append(tn[i - 3] + tn[i - 2] + tn[i - 1])

#         return tn[-1]


class Solution:
    def __init__(self):
        self.cache = [0, 1, 1]

    def tribonacci(self, n: int) -> int:
        while len(self.cache) <= n:
            self.cache.append(self.cache[-3] + self.cache[-2] + self.cache[-1])

        return self.cache[n]

