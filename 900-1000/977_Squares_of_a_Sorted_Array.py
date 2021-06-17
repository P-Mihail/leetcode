# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
# in non-decreasing order.
#
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


from typing import List
# import collections

class Solution(object):
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     # O(n) but slower
    #     left_point, right_point = 0, len(nums) - 1
    #     ans = collections.deque()
    #     while left_point <= right_point:
    #         if abs(nums[left_point]) > nums[right_point]:
    #             ans.appendleft(nums[left_point] ** 2)
    #             left_point += 1
    #         else:
    #             ans.appendleft(nums[right_point] ** 2)
    #             right_point -= 1
    #     return list(ans)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # faster but O(n log n)
        ans = [n**2 for n in nums]
        ans.sort()
        return ans
