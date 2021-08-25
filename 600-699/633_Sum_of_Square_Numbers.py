# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
# 
# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# Example 2:
# Input: c = 3
# Output: false
# 
# Example 3:
# Input: c = 4
# Output: true
# 
# Example 4:
# Input: c = 2
# Output: true
# 
# Example 5:
# Input: c = 1
# Output: true
# 
# Constraints:
# 0 <= c <= 2^31 - 1


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        max_a = int(c ** 0.5)

        for a in range(max_a, max_a // 2 - 1, -1):
            b2 = c - a * a
            if b2 == int(b2 ** 0.5) ** 2:
                return True

        return False
