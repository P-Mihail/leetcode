# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
# and return its sum.
#
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^5
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer
# approach, which is more subtle.


from typing import List


class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # time complexity O(n)
        # space complexity O(1)
        max_sum_until_i = max_sum = nums[0]

        for i in range(1, len(nums)):
            if max_sum_until_i > 0:
                max_sum_until_i += nums[i]
            else:
                max_sum_until_i = nums[i]

            max_sum = max(max_sum_until_i, max_sum)

        return max_sum
