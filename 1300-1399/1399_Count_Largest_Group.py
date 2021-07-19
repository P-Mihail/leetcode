# Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.
#
# Return how many groups have the largest size.
#
#
# Example 1:
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
#
# Example 2:
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
#
# Example 3:
# Input: n = 15
# Output: 6
#
# Example 4:
# Input: n = 24
# Output: 5
#
# Constraints:
# 1 <= n <= 10^4


from typing import Dict


class Solution:
    # def countLargestGroup(self, n: int) -> int:
    #     def sumdig(x: int) -> int:
    #         ans = 0
    #         while x > 0:
    #             x, m = divmod(x, 10)
    #             ans += m
    #         return ans
    #
    #     counter = {}
    #
    #     for i in range(1, n + 1):
    #         s = sumdig(i)
    #         counter[s] = counter.get(s, 0) + 1
    #
    #     return len([1 for v in counter.values() if v == max(counter.values())])

    def countLargestGroup(self, n: int) -> int:
        counter: Dict[int, int] = {}

        for i in range(1, n + 1):
            s = sum(map(int, str(i)))
            counter[s] = counter.get(s, 0) + 1

        values = counter.values()
        return len([1 for v in values if v == max(values)])
