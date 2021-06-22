# Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return
# the maximum number.
#
# Example 1:
# Input: nums = [3,2,1]
# Output: 1
#
# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
#
# Example 3:
#
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#
# Constraints:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
# Follow up: Can you find an O(n) solution?


from typing import List, Union


class Solution(object):
    # def thirdMax(self, nums: List[int]) -> Union[int, float]:
    #     # time compexity O(n), 1 pass
    #     # space complexity O(1)
    #     top = [float("-inf")] * 3
    #     for n in nums:
    #         if n not in top:
    #             if n > top[0]:
    #                 top = [n, top[0], top[1]]
    #             elif n > top[1]:
    #                 top = [top[0], n, top[1]]
    #             elif n > top[2]:
    #                 top = [top[0], top[1], n]
    #     return top[0] if top[2] == float("-inf") else top[2]

    def thirdMax(self, nums: List[int]) -> Union[int, float]:
        # time compexity O(n), 1 pass
        # space complexity O(1)
        top = [float("-inf")] * 3
        for n in nums:
            if n > top[0]:
                top = [n, top[0], top[1]]
            elif top[0] > n > top[1]:
                top = [top[0], n, top[1]]
            elif top[1] > n > top[2]:
                top = [top[0], top[1], n]
        return top[0] if top[2] == float("-inf") else top[2]
