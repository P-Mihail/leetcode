# You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.
# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:
#
# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Remove x from the array nums.
# Return the maximum score after performing m operations.
#
# Example 1:
# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
#
# Example 2:
# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
#
# Constraints:
# n == nums.length
# m == multipliers.length
# 1 <= m <= 10^3
# m <= n <= 10^5
# -1000 <= nums[i], multipliers[i] <= 1000


from typing import List
from functools import lru_cache


class Solution:
    # def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    #     # Top-down Implementation
    #     # Time Complexity: O(m^2)
    #     # Space Complexity: O(m^2)
    #     @lru_cache(2000)
    #     def dp(pl, i):
    #         if i == lm:
    #             return 0
    #         mul = multipliers[i]
    #         return max(
    #             mul * nums[pl] + dp(pl + 1, i + 1),
    #             mul * nums[ln - 1 + pl - i] + dp(pl, i + 1),
    #         )

    #     ln, lm = len(nums), len(multipliers)
    #     return dp(0, 0)

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Bottom-up Implementation
        # Time Complexity: O(m^2)
        # Space Complexity: O(m^2)
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(
                    mult * nums[left] + dp[i + 1][left + 1],
                    mult * nums[right] + dp[i + 1][left],
                )
        return dp[0][0]
