# In a array nums of size 2 * n, there are n + 1 unique elements, and exactly one of these elements is repeated n times.
#
# Return the element repeated n times.
#
# Example 1:
# Input: nums[1,2,3,3]
# Output: 3
#
# Example 2:
# Input: nums[2,1,2,5,3,2]
# Output: 2
#
# Example 3:
# Input: nums[5,1,5,2,5,3,5,4]
# Output: 5
#
#
# Note:
# 4 <= nums.length <= 10000
# 0 <= nums[i] < 10000
# nums.length is even


from typing import List


class Solution(object):
    # def repeatedNTimes(self, nums: List[int]) -> int:
    #     # simple way
    #     # time complexity O(n)
    #     # space complexity O(1)
    #     numset = set()
    #
    #     for n in nums:
    #         if n in numset:
    #             return n
    #         numset.add(n)

    def repeatedNTimes(self, nums: List[int]) -> int:
        # time complexity O(n)
        # space complexity O(1)
        for k in range(1, 4):
            for i in range(len(nums) - k):
                if nums[i] == nums[i+k]:
                    return nums[i]
        return -1
