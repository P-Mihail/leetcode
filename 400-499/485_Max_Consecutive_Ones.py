# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
#
# Example 2:
# Input: nums = [1, 0, 1, 1, 0, 1]
# Output: 2
#
# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.


from typing import List


class Solution(object):
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, curr = 0, 0
        for n in nums:
            if n == 1:
                curr += 1
                if curr > ans:
                    ans = curr
            else:
                curr = 0
        return ans
