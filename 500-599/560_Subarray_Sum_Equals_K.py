# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
#
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
#
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1}
        cs = ans = 0

        for n in nums:
            cs += n

            if cs - k in hm:
                ans += hm[cs - k]

            if cs in hm:
                hm[cs] = hm[cs] + 1
            else:
                hm[cs] = 1

        return ans
