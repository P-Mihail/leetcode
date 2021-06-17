# Given an array nums of integers, return how many of them contain an even number of digits.
#
# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
#
# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1
#
# Constraints:
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5


from typing import List


class Solution(object):
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                ans += 1
        return ans
