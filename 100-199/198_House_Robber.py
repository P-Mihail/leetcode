# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from
# robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken
# into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400


from functools import lru_cache
from typing import List


class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     @lru_cache(None)
    #     def helper(idx: int) -> int:
    #         if idx >= len(nums):
    #             return 0
    #         elif idx == len(nums) - 1:
    #             return nums[-1]
    #         else:
    #             return max(helper(idx + 1), nums[idx] + helper(idx + 2))

    #     return helper(0)

    def rob(self, nums: List[int]) -> int:
        rob, not_rob = 0, 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)
