# You are given a sorted unique integer array nums.
#
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of
# nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in
# nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b
#
#
# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
# Example 3:
# Input: nums = []
# Output: []
#
# Example 4:
# Input: nums = [-1]
# Output: ["-1"]
#
# Example 5:
# Input: nums = [0]
# Output: ["0"]
#
#
# Constraints:
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.


from typing import List


class Solution:
    # def summaryRanges(self, nums: List[int]) -> List[str]:
    #     sp = 0
    #     ans = []
    #
    #     for i in range(len(nums) - 1):
    #         if nums[i + 1] - 1 != nums[i]:
    #             if sp == i:
    #                 ans.append(f"{nums[sp]}")
    #             else:
    #                 ans.append(f"{nums[sp]}->{nums[i]}")
    #             sp = i + 1
    #
    #     if len(nums) > 0:
    #         if sp == len(nums) - 1:
    #             ans.append(f"{nums[sp]}")
    #         else:
    #             ans.append(f"{nums[sp]}->{nums[-1]}")
    #
    #     return ans

    def summaryRanges(self, nums: List[int]) -> List[str]:
        sp = 0
        ans = []

        for i in range(len(nums)):
            if (i == len(nums) - 1) or (nums[i + 1] - 1 != nums[i]):
                if sp == i:
                    ans.append(f"{nums[sp]}")
                else:
                    ans.append(f"{nums[sp]}->{nums[i]}")
                sp = i + 1

        return ans
