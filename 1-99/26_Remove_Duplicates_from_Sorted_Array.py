# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
# in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
# first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra
# memory.
#
# Example 1:
# Input: nums = [1,1,2]
# Output: 2
# Result: nums = [1,2,_]
#
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5
# Result: nums = [0,1,2,3,4,_,_,_,_,_]
#
# Constraints:
# 0 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.


from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i, n in enumerate(nums):
            if nums[j] != n:
                j += 1
                nums[j] = n
        return j + 1
