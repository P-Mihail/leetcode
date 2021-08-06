# Count the number of prime numbers less than a non-negative number, n.
#
#
# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
# Example 2:
# Input: n = 0
# Output: 0
#
# Example 3:
# Input: n = 1
# Output: 0
#
#
# Constraints:
# 0 <= n <= 5 * 10^6


class Solution:
    def countPrimes(self, n: int) -> int:
        visited = [0] * n
        ans = 0

        for i in range(2, n):
            if visited[i]:
                continue
            ans += 1
            visited[i * i : n : i] = [1] * ((n - i * i - 1) // i + 1)

        return ans
