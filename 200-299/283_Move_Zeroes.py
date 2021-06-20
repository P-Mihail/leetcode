# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: null
# Result: [1,3,12,0,0]
#
# Example 2:
# Input: nums = [0]
# Output: null
# Result: [0]
#
# Constraints:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1


from typing import List


class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1
