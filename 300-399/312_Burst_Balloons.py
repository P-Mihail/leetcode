# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums.
# You are asked to burst all the balloons.
#
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds
#  of the array, then treat it as if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
# Example 1:
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# Example 2:
# Input: nums = [1,5]
# Output: 10
#
# Constraints:
# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100


class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1:  # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i + 1, j):  # find the last balloon
                coins = max(
                    coins,
                    nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j),
                )
            dp[i][j] = coins
            return coins

        return calculate(0, n - 1)

