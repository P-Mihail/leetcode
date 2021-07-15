# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.
#
#
# Example 1:
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#
# Example 2:
# Input: nums = [4,2,3,4]
# Output: 4
#
# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000


from typing import List


class Solution:
    # def triangleNumber(self, nums: List[int]) -> int:
    #     # time complexity O(n^2)
    #     # space complexity O(log n)
    #     ans = 0
    #     nums.sort()
    #     for i in range(len(nums) - 2):
    #         if nums[i] == 0:
    #             continue
    #         k = i + 2
    #         for j in range(i + 1,len(nums)-1):
    #             M = nums[i] + nums[j] - 1
    #             while k < len(nums) and nums[k] <= M:
    #                 k += 1
    #             ans += min(k, len(nums)) - (j + 1)
    #     return ans

    def triangleNumber(self, nums):
        # time complexity O(n^2)
        # space complexity O(log n)
        nums.sort()
        res = 0
        for i in range(len(nums) - 1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
