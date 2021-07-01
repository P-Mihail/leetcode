# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
# 1's in the binary representation of i.
#
#
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
# Constraints:
# 0 <= n <= 10^5
#
#
# Follow up:
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and
# possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


from typing import List


class Solution(object):
    # def countBits(self, n: int) -> List[int]:
    #     # time complexity O(n) 1 pass
    #     # space complexity O(n)
    #     ans = [0]
    #     k = 1
    #
    #     while k <= n:
    #         for i in range(k):
    #             ans.append(ans[-k + i] + 1)
    #             if len(ans) == n + 1:
    #                 break
    #         k *= 2
    #
    #     return ans

    def countBits(self, num: int) -> List[int]:
        # more clear
        # time complexity O(n) 1 pass
        # space complexity O(n)
        counter = [0]
        for i in range(1, num + 1):
            counter.append(counter[i // 2] + i % 2)
        return counter
