# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
#
# Example 2:
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.


from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hm = {0: -1}
        ans = c = 0
        for i, n in enumerate(nums):
            if n == 0:
                c += 1
            else:
                c -= 1
            if c not in hm:
                hm[c] = i
            else:
                ans = max(ans, i - hm[c])
        print(hm)
        return ans
