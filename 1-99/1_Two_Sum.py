# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


from typing import List, Dict


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One-pass Hash Table
        # Time complexity: O(n)
        # Space complexity: O(n)
        mem: Dict[int, int] = {}
        for i, n in enumerate(nums):
            if target - n in mem:
                return [i, mem[target - n]]
            else:
                mem[n] = i
        return [-1, -1]