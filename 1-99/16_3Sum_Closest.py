# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
# target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Constraints:
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4


from typing import List
import bisect


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # time complexity O(n^2 log n)
        # space complexity O(log n)
        nums.sort()
        diff = target - sum(nums[:3])

        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                s = target - nums[i] - nums[j]
                k = bisect.bisect(nums, s, j + 1)

                if k < len(nums) and abs(s - nums[k]) < abs(diff):
                    diff = s - nums[k]
                if k > j + 1 and abs(s - nums[k - 1]) < abs(diff):
                    diff = s - nums[k - 1]
            if diff == 0:
                break

        return target - diff
