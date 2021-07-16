# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = []
# Output: []
#
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            if len(nums) < 2 or nums[0] * 2 > target or nums[-1] * 2 < target:
                return []

            ans: List[List[int]] = []
            s = set()
            for i in range(len(nums)):
                if len(ans) == 0 or ans[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        ans.append([target - nums[i], nums[i]])
                    s.add(nums[i])
            return ans

        nums.sort()

        ans = []

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for s in twoSum(nums[i + 1 :], -nums[i]):
                    ans.append([nums[i]] + s)

        return ans
