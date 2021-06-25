# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
# the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0
#
# Example 5:
# Input: nums = [1], target = 0
# Output: 0
#
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4


from typing import List
import bisect


class Solution(object):
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     # Using bisect module
    #     # time complexity O(n log n)
    #     # space complexity O(1)
    #     return bisect.bisect_left(nums, target)

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     # binary search by hand
    #     # time complexity O(n log n)
    #     # space complexity O(1)
    #     p0, p1 = 0, len(nums) - 1
    #
    #     while p0 <= p1:
    #         median = (p0 + p1) // 2
    #         if nums[median] == target:
    #             return median
    #         elif nums[median] > target:
    #             p1 = median - 1
    #         else:
    #             p0 = median + 1
    #
    #     return p0

    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search by hand (faster)
        # time complexity O(n log n)
        # space complexity O(1)
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
