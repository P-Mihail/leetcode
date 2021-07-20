# Given an array nums of integers, we must modify the array in the following way: we choose an i and replace nums[i]
# with -nums[i], and we repeat this process k times in total.  (We may choose the same index i multiple times.)
#
# Return the largest possible sum of the array after modifying it in this way.
#
#
# Example 1:
# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose indices (1,) and nums becomes [4,-2,3].
#
# Example 2:
# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
#
# Example 3:
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
#
#
# Note:
# 1 <= nums.length <= 10000
# 1 <= k <= 10000
# -100 <= nums[i] <= 100


from typing import List
from heapq import heapify, heapreplace


class Solution:
    # def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
    #     # time complexity O(n log n)
    #     # space complexity O(log n)
    #     nums.sort()
    #
    #     for i in range(min(k, len(nums))):
    #         if nums[i] < 0:
    #             nums[i] *= -1
    #             k -= 1
    #         else:
    #             break
    #
    #     ans = sum(nums)
    #
    #     if k % 2:
    #         ans -= 2 * min(nums)
    #
    #     return ans

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # time complexity O(n + k log n)
        # space complexity O(1)
        heapify(nums)

        while k > 0 and nums[0] < 0:
            heapreplace(nums, -nums[0])
            k -= 1
        if k % 2:
            heapreplace(nums, -nums[0])

        return sum(nums)
