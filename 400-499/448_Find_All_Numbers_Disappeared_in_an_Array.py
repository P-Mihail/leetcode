# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
# range [1, n] that do not appear in nums.
#
#
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
#
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
# Constraints:
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
#
#
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as
# extra space.


from typing import List


class Solution(object):
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     # fast, byt use extra space
    #     n = len(nums)
    #     nums = set(nums)
    #     return [i for i in range(1, n + 1) if i not in nums]

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] > 0:
                p = nums[i] - 1
                while nums[p] > 0:
                    nums[p], p = -nums[p], nums[p] - 1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
