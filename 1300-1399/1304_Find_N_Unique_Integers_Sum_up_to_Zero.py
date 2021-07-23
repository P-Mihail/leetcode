# Given an integer n, return any array containing n unique integers such that they add up to 0.
#
# Example 1:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
#
# Example 2:
# Input: n = 3
# Output: [-1,0,1]
#
# Example 3:
# Input: n = 1
# Output: [0]
#
#
# Constraints:
#
# 1 <= n <= 1000


from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] if n % 2 else []

        for i in range(n // 2):
            ans += [i + 1, -i - 1]

        return ans
