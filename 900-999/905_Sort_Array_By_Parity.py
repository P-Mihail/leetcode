# Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by
# all the odd elements of nums.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
# Constraints:
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000


from typing import List


class Solution(object):
    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    #     # simple way 1
    #     # time complexity O(n log n)
    #     # space complexity O(n)
    #     nums.sort(key = lambda x: x % 2)
    #     return nums
    #
    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    #     # simple way 2
    #     # time complexity O(n)
    #     # space complexity O(n)
    #     return ([x for x in A if x % 2 == 0] +
    #             [x for x in A if x % 2 == 1])

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # in-place, two pointer, one pass!
        # time complexity O(n)
        # space complexity o(1)
        left_point, right_point = 0, len(nums) - 1

        while left_point < right_point:
            if nums[left_point] % 2 == 0:
                left_point += 1
                continue
            if nums[right_point] % 2 == 1:
                right_point -= 1
                continue
            nums[left_point], nums[right_point] = nums[right_point], nums[left_point]

        return nums
