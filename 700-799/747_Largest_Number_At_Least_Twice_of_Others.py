# You are given an integer array nums where the largest integer is unique.
#
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it
# is, return the index of the largest element, or return -1 otherwise.
#
#
#
# Example 1:
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
#
# Example 3:
# Input: nums = [1]
# Output: 0
# Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.
#
#
# Constraints:
#
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.


from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        idx, m1, m2 = -1, -1, -1

        for i, n in enumerate(nums):
            if n > m1:
                idx, m1, m2 = i, n, m1
            elif n > m2:
                m2 = n

        return idx if m1 >= 2 * m2 else -1
