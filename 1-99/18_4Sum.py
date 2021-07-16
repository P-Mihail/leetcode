# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
# such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
# Constraints:
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9


from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # time complexity O(n^3)
        # space complexity O(n)
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

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            if len(nums) < k or nums[0] * k > target or nums[-1] * k < target:
                return []
            if k == 2:
                return twoSum(nums, target)
            ans = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for s in kSum(nums[i + 1:], target - nums[i], k - 1):
                        ans.append([nums[i]] + s)
            return ans

        nums.sort()
        return kSum(nums, target, 4)
